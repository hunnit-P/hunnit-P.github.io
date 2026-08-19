#!/usr/bin/env python3
"""
source/{chapter}문제.md + source/{chapter}해설.md 를 파싱해서
data/{chapter}.json 을 생성하고 data/manifest.json 을 갱신한다.

문제.md 포맷 규칙
  # PART N. <객관식|단답형|서술형> ...   -> 파트 구분
  ## X. 이름                            -> 섹션 구분 (X: A,B,C...)
  ### N.  또는  ### N. ★ / ★★ / ★★★     -> 문제 번호 + 난이도(별 개수)
  ① ② ③ ④ 로 시작하는 줄               -> 객관식 보기
  그 외 텍스트                          -> 문제 본문 또는 보기 뒤에 오면 참고 노트
  ## 이 N문제를 공부하는 방법 (숫자 없는 ## 헤더) -> 이후 전부 studyGuide 로 수집

해설.md 포맷 규칙
  ## N. <제목/★>  또는  ### N. <①~④> <★...>  -> 문제 번호 (+ 객관식 정답 기호)
  그 외 텍스트                                 -> 해설/모범답안 본문
  숫자 없는 #/##/### 헤더가 나오면(문제 파싱 이후) -> 이후 전부 appendix 로 수집
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "source"
DATA_DIR = ROOT / "data"

CIRCLED = ["①", "②", "③", "④"]

PART_RE = re.compile(r"^#\s*PART\s*\d+\.\s*(.+)$")
# 섹션 헤더는 원본에서 '#'과 '##'가 혼용되어 있어 둘 다 허용한다.
SECTION_RE = re.compile(r"^#{1,2}\s+([A-Z])\.\s+(.+)$")
GENERIC_H2_RE = re.compile(r"^##\s+(.+)$")
QUESTION_RE = re.compile(r"^###\s+(\d+)\.\s*(.*)$")


def part_key(title: str) -> str:
    if "객관식" in title:
        return "mc"
    if "단답형" in title:
        return "short"
    if "서술형" in title:
        return "essay"
    return "mc"


def strip_hardbreak(s):
    # 일부 소스는 줄 끝에 markdown hard-break용 '\'를 붙여둔다 (문단이 하나로
    # 합쳐지지 않도록 강제 줄바꿈시키는 용도). 렌더링에는 필요 없으므로 제거.
    return s[:-1].rstrip() if s.endswith("\\") else s


def clean_lines(lines):
    # 앞뒤 빈 줄 제거, 내부 개행은 보존
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(lines).strip()


def parse_questions(md_path: Path):
    lines = md_path.read_text(encoding="utf-8").splitlines()

    questions = []
    current_part = None
    current_section = None  # (key, name)
    current_q = None
    collecting_guide = False
    guide_lines = []

    def flush():
        nonlocal current_q
        if current_q is None:
            return
        q = current_q
        stem = clean_lines(q["stem_lines"])
        choices = [c.strip() for c in q["choices"]]
        note = clean_lines(q.get("note_lines", []))
        item = {
            "id": q["id"],
            "part": q["part"],
            "section": q["section"],
            "star": q["star"],
            "stem": stem,
            "choices": choices,
        }
        if note:
            item["note"] = note
        questions.append(item)
        current_q = None

    for raw in lines:
        line = raw.rstrip("\n")

        if collecting_guide:
            guide_lines.append(line)
            continue

        m_part = PART_RE.match(line)
        if m_part:
            flush()
            current_part = part_key(m_part.group(1))
            current_section = None
            continue

        m_section = SECTION_RE.match(line)
        if m_section:
            flush()
            current_section = {"key": m_section.group(1), "name": m_section.group(2).strip()}
            continue

        m_generic_h2 = GENERIC_H2_RE.match(line)
        if m_generic_h2 and current_part is not None:
            # 숫자 없는 '## ' 헤더 = 문제 구간 종료, 이후는 스터디 가이드
            flush()
            collecting_guide = True
            guide_lines.append(line)
            continue

        m_q = QUESTION_RE.match(line)
        if m_q:
            flush()
            qid = int(m_q.group(1))
            rest = m_q.group(2)
            star = rest.count("★")
            current_q = {
                "id": qid,
                "part": current_part,
                "section": current_section,
                "star": star,
                "stem_lines": [],
                "choices": [],
                "note_lines": [],
            }
            continue

        if current_q is None:
            continue

        stripped = line.strip()
        if stripped == "---":
            continue
        if stripped == "":
            continue
        if stripped[0] in CIRCLED:
            current_q["choices"].append(strip_hardbreak(stripped[1:].strip()))
            continue

        choices = current_q["choices"]
        if choices and len(choices) < 4:
            # 보기 하나가 길어서 줄바꿈(markdown hard-break '\')된 경우:
            # 다음 줄에 ①~④ 표시가 없으면 직전 보기의 이어지는 내용이다.
            choices[-1] = (choices[-1] + " " + strip_hardbreak(stripped)).strip()
            continue

        if current_q["choices"]:
            current_q["note_lines"].append(strip_hardbreak(line))
        else:
            current_q["stem_lines"].append(strip_hardbreak(line))

    flush()
    guide_text = clean_lines(guide_lines) if guide_lines else ""
    return questions, guide_text


ANSWER_HEADER_RE = re.compile(r"^#{1,3}\s+(\d+)\.\s*(.*)$")


def parse_answers(md_path: Path):
    lines = md_path.read_text(encoding="utf-8").splitlines()

    # 숫자 없는 '#'/'##'/'###' 헤더는 두 가지 역할을 한다: 문제 구간
    # 중간에 끼어드는 장식용 제목(예: "# 다중선형회귀", "## 단답형 정답")
    # 이거나, 맨 마지막 문제 뒤에 오는 진짜 부록("## 시험 직전 핵심 요약")
    # 이다. 마지막 문제 번호 헤더의 위치를 미리 찾아, 그 이후에 나오는
    # 것만 부록으로 취급하고 그 전의 것은 조용히 건너뛴다.
    last_q_idx = -1
    for idx, raw in enumerate(lines):
        if ANSWER_HEADER_RE.match(raw.rstrip("\n")):
            last_q_idx = idx

    answers = {}
    current_id = None
    current_letter = None
    body_lines = []
    collecting_appendix = False
    appendix_lines = []

    def flush():
        nonlocal current_id, current_letter, body_lines
        if current_id is None:
            return
        answers[current_id] = {
            "answer_letter": current_letter,
            "explanation": clean_lines(body_lines),
        }
        current_id = None
        current_letter = None
        body_lines = []

    for idx, raw in enumerate(lines):
        line = raw.rstrip("\n")

        if collecting_appendix:
            appendix_lines.append(line)
            continue

        m = ANSWER_HEADER_RE.match(line)
        if m:
            flush()
            current_id = int(m.group(1))
            rest = m.group(2).strip()
            current_letter = rest[0] if rest and rest[0] in CIRCLED else None
            body_lines = []
            continue

        if re.match(r"^#{1,3}\s+\S", line):
            # 수식(백슬래시 포함) 줄이 우연히 '#'으로 시작하는 경우
            # (예: "# \sum_{...}")는 본문 내용이므로 살려서 담는다.
            if "\\" in line and current_id is not None:
                body_lines.append(re.sub(r"^#+\s+", "", line))
                continue
            if current_id is not None and idx > last_q_idx:
                flush()
                collecting_appendix = True
                appendix_lines.append(line)
            continue

        if current_id is None:
            continue

        if line.strip() == "---":
            continue

        body_lines.append(line)

    flush()
    appendix_text = clean_lines(appendix_lines) if appendix_lines else ""
    return answers, appendix_text


LETTER_INDEX = {c: i for i, c in enumerate(CIRCLED)}

HANGUL_RE = re.compile(r"[가-힣]")
EQUALS_BAR_RE = re.compile(r"^=+$")
MATH_SIGNAL_RE = re.compile(r"[\\^_]")
WORD_RE = re.compile(r"[A-Za-z]{3,}")


def join_math_block(lines):
    """
    '[' ... ']' 사이에 있던 줄들을 하나의 LaTeX 식으로 합친다.
    원본이 markdown setext 제목으로 깨지면서 'LHS\\n====\\n\\nRHS' 형태로
    풀려버린 '=' 기호를 복원하고, \\frac{a}\\n{b} 처럼 단순히 줄바꿈만 된
    경우는 그대로 이어붙인다.
    """
    result = ""
    pending_eq = False
    started = False
    for raw in lines:
        stripped = raw.strip()
        if EQUALS_BAR_RE.match(stripped) and len(stripped) >= 3:
            pending_eq = True
            continue
        if stripped == "":
            if started:
                pending_eq = True
            continue
        if not started:
            result = stripped
            started = True
        else:
            result += (" = " if pending_eq else "") + stripped
            pending_eq = False
    return result


SQRT_PAREN_RE = re.compile(r"(?<!\\)\bsqrt\(([^()]*)\)")
FUNC_NAME_RE = re.compile(
    r"(?<!\\)\b(tanh|sigma|sigmoid|softmax|argmax|exp|log|ln|cos|sin)\b"
)
FUNC_MACRO = {
    "tanh": "\\tanh",
    "sigma": "\\sigma",
    "exp": "\\exp",
    "log": "\\log",
    "ln": "\\ln",
    "cos": "\\cos",
    "sin": "\\sin",
    "sigmoid": "\\operatorname{sigmoid}",
    "softmax": "\\operatorname{softmax}",
    "argmax": "\\operatorname{argmax}",
}


def fix_bare_math_functions(s):
    """
    일부 소스는 \\tanh, \\sigma 대신 백슬래시 없이 tanh, sigma, sqrt(d_k) 처럼
    적어놓는다. 그대로 두면 KaTeX가 이걸 이름 있는 함수가 아니라 그냥 붙어있는
    변수들의 곱(예: 's*q*r*t')으로 렌더링해 sqrt(d_k)가 루트 기호 없이 깨진다.
    자주 쓰이는 함수 이름을 LaTeX 명령으로 보정한다. 이미 '\\'가 붙어있으면
    건드리지 않는다.
    """
    s = SQRT_PAREN_RE.sub(lambda m: "\\sqrt{" + m.group(1) + "}", s)
    s = FUNC_NAME_RE.sub(lambda m: FUNC_MACRO[m.group(1)], s)
    return s


def convert_inline_parens(line):
    """
    괄호로 감싼 인라인 수식 '(...)' 을 KaTeX가 인식하는 '\\(...\\)' 로 바꾼다.
    중첩 괄호(예: '((X^TX)^{-1}X^Ty)')는 깊이를 추적해 가장 바깥쪽 괄호만 변환한다.
    다음은 수식이 아니라 용어 설명/병기이므로 그대로 둔다:
      - 한글이 포함된 괄호 (예: '(과적합)')
      - 수식 기호(\\, ^, _)가 하나도 없으면서 3글자 이상 영단어가 들어있는 괄호
        (예: '(Foundation Model)', '(VLM)', '(SoM)') - 이런 걸 수식으로 렌더링하면
        영단어가 붙어버리는 이탤릭 수식체로 뭉개진다.
    """
    result = []
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if ch == "(":
            depth = 1
            j = i + 1
            while j < n and depth > 0:
                if line[j] == "(":
                    depth += 1
                elif line[j] == ")":
                    depth -= 1
                j += 1
            if depth == 0:
                inner = line[i + 1 : j - 1]
                looks_like_math = bool(inner) and not HANGUL_RE.search(inner) and (
                    MATH_SIGNAL_RE.search(inner) or not WORD_RE.search(inner)
                )
                if looks_like_math:
                    result.append("\\(" + fix_bare_math_functions(inner) + "\\)")
                else:
                    result.append(line[i:j])
                i = j
                continue
        result.append(ch)
        i += 1
    return "".join(result)


def normalize_math(text):
    """
    텍스트 안의 '[' 단독 줄 ~ ']' 단독 줄 구간은 디스플레이 수식(\\[...\\])으로,
    그 밖의 줄에 있는 '(...)' 인라인 수식은 \\(...\\) 로 변환한다.
    """
    if not text:
        return text
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "[":
            j = i + 1
            block_lines = []
            while j < len(lines) and lines[j].strip() != "]":
                block_lines.append(lines[j])
                j += 1
            out.append("\\[" + fix_bare_math_functions(join_math_block(block_lines)) + "\\]")
            i = j + 1
        else:
            out.append(convert_inline_parens(lines[i]))
            i += 1
    return "\n".join(out)


def build_chapter(chapter_id: str, problem_path: Path, answer_path: Path):
    questions, guide_text = parse_questions(problem_path)
    answers, appendix_text = parse_answers(answer_path)

    sections = []
    seen = set()

    merged = []
    for q in questions:
        a = answers.get(q["id"], {})
        item = dict(q)
        if q["section"] and q["section"]["key"] not in seen:
            seen.add(q["section"]["key"])
            sections.append(q["section"])

        item["stem"] = normalize_math(item["stem"])
        item["choices"] = [normalize_math(c) for c in item["choices"]]
        if item.get("note"):
            item["note"] = normalize_math(item["note"])

        if q["part"] == "mc":
            letter = a.get("answer_letter")
            item["answerIndex"] = LETTER_INDEX.get(letter, None)
            item["explanation"] = normalize_math(a.get("explanation", ""))
        else:
            item["answerText"] = normalize_math(a.get("explanation", ""))
        merged.append(item)

    counts = {
        "mc": sum(1 for q in merged if q["part"] == "mc"),
        "short": sum(1 for q in merged if q["part"] == "short"),
        "essay": sum(1 for q in merged if q["part"] == "essay"),
    }

    chapter = {
        "id": chapter_id,
        "sections": sections,
        "counts": counts,
        "questions": merged,
        "studyGuide": normalize_math(guide_text),
        "appendix": normalize_math(appendix_text),
    }
    return chapter


def _nfc(s):
    return unicodedata.normalize("NFC", s)


def main():
    DATA_DIR.mkdir(exist_ok=True)

    # macOS(APFS)는 한글 파일명을 NFD(자모 분리형)로 저장하는 경우가 많아서,
    # 파이썬 문자열 리터럴(NFC)로 만든 glob 패턴이 조용히 매칭에 실패할 수
    # 있다. 실제 디렉토리 항목을 그대로 훑고 NFC로 정규화해 비교한다.
    files_by_nfc_name = {_nfc(p.name): p for p in SOURCE_DIR.iterdir() if p.is_file()}
    problem_files = sorted(
        (p for name, p in files_by_nfc_name.items() if name.endswith("문제.md")),
        key=lambda p: _nfc(p.name),
    )

    manifest_chapters = []

    for problem_path in problem_files:
        chapter_id_raw = _nfc(problem_path.name).replace("문제.md", "")
        chapter_id = chapter_id_raw.replace("_", "-")
        answer_path = files_by_nfc_name.get(_nfc(f"{chapter_id_raw}해설.md"))
        if answer_path is None:
            print(f"[skip] {chapter_id}: 해설 파일 없음 ({chapter_id_raw}해설.md)")
            continue

        chapter = build_chapter(chapter_id, problem_path, answer_path)
        out_path = DATA_DIR / f"{chapter_id}.json"
        out_path.write_text(
            json.dumps(chapter, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        section_names = " · ".join(s["name"] for s in chapter["sections"])
        counts = chapter["counts"]
        total = counts["mc"] + counts["short"] + counts["essay"]
        print(
            f"[ok] {chapter_id}: 총 {total}문항 "
            f"(객관식 {counts['mc']} / 단답 {counts['short']} / 서술 {counts['essay']})"
        )

        manifest_chapters.append(
            {
                "id": chapter_id,
                "title": section_names or chapter_id,
                "counts": counts,
                "available": True,
            }
        )

    # source에 파일이 아직 없는 예정 챕터도 목록에 노출 (준비중)
    planned = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2"]
    have = {c["id"] for c in manifest_chapters}
    for cid in planned:
        if cid not in have:
            manifest_chapters.append(
                {"id": cid, "title": "", "counts": {"mc": 0, "short": 0, "essay": 0}, "available": False}
            )

    order = {cid: i for i, cid in enumerate(planned)}
    manifest_chapters.sort(key=lambda c: order.get(c["id"], 999))

    manifest = {"chapters": manifest_chapters}
    (DATA_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[ok] manifest.json 갱신 ({len(manifest_chapters)}개 챕터)")


if __name__ == "__main__":
    main()
