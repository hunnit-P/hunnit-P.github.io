// 여러 페이지에서 공용으로 쓰는 유틸

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// **bold**, `code`, 줄바꿈만 가볍게 처리한다 (원본 md의 깨진 LaTeX 표기는
// 그대로 텍스트로 보여준다 - 별도 수식 렌더링은 하지 않음).
function formatText(raw) {
  if (!raw) return "";
  let s = escapeHtml(raw);
  s = s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/\n/g, "<br>");
  return s;
}

async function loadJson(path) {
  const res = await fetch(path, { cache: "no-store" });
  if (!res.ok) throw new Error(`${path} 로드 실패 (${res.status})`);
  return res.json();
}

const CIRCLED = ["①", "②", "③", "④"];

// data/*.json 은 인라인 수식을 \(...\), 블록 수식을 \[...\] 로 담고 있다.
// KaTeX auto-render가 로드돼 있으면 해당 구간을 실제 수식으로 렌더링한다.
function renderMath(el) {
  if (!window.renderMathInElement) return;
  renderMathInElement(el, {
    delimiters: [
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
    ],
    throwOnError: false,
  });
}
