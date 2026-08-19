# 시험 대비 문제은행

GitHub Pages로 바로 호스팅할 수 있는 정적 사이트. 강의별(1-1, 1-2, 2-1, 2-2, 3-1, 3-2 ...) 문제를 풀고, 보기를 클릭하는 즉시 정답/해설이 표시된다.

## 구조

```
index.html          강의 목록 (data/manifest.json 을 읽어서 카드 렌더링)
quiz.html            문제풀이 페이지 (?ch=1-2 같은 쿼리로 챕터 지정)
assets/              공용 CSS/JS
source/              원본 마크다운 (N_M문제.md / N_M해설.md 쌍)
data/                source/*.md 를 파싱해서 만든 JSON (사이트가 실제로 읽는 데이터)
scripts/build_data.py  source/*.md -> data/*.json + data/manifest.json 변환 스크립트
```

## 새 챕터(1-1, 2-1, 2-2, 3-1, 3-2) 추가하는 법

1. `source/` 안에 아래 두 파일을 같은 형식으로 넣는다. 파일명 규칙: `{n}_{m}문제.md`, `{n}_{m}해설.md` (예: `1_1문제.md`, `1_1해설.md`)
2. 마크다운 포맷은 기존 `source/1_2문제.md` / `source/1_2해설.md` 를 그대로 따라야 한다. 파서가 인식하는 패턴:
   - 문제 파일
     - `# PART N. 객관식/단답형/서술형 ...` — 파트 구분
     - `# X. 이름` 또는 `## X. 이름` (X는 A, B, C...) — 섹션 구분
     - `### 번호.` 또는 `### 번호. ★` — 문제 번호 (별 개수 = 난이도)
     - `① ② ③ ④` 로 시작하는 줄 — 객관식 보기 (없으면 단답/서술형으로 처리)
   - 해설 파일
     - `### 번호. ②` 처럼 번호 뒤에 정답 기호가 오면 객관식 정답으로 인식
     - `### 번호.` / `## 번호.` 뒤에 오는 본문 전체가 단답형/서술형 모범답안이 된다
     - 문제 번호는 문제 파일과 해설 파일에서 반드시 일치해야 매핑된다
3. 변환 스크립트를 실행한다.
   ```bash
   python3 scripts/build_data.py
   ```
   `data/{n}-{m}.json` 이 생성/갱신되고 `data/manifest.json` 에 자동으로 등록된다 (이미 "준비중"으로 있던 카드가 자동으로 활성화됨).
4. 로컬에서 확인:
   ```bash
   python3 -m http.server 8000
   # http://localhost:8000/index.html
   ```

## GitHub Pages 배포

1. 이 폴더를 깃 저장소로 만들고 GitHub 원격 저장소에 push
2. 저장소 Settings → Pages → Source를 `main` 브랜치 `/ (root)` 로 설정
3. `https://<계정>.github.io/<저장소이름>/` 으로 접속하면 `index.html` 이 뜬다
