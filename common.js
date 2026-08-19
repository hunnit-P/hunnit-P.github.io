// 여러 페이지에서 공용으로 쓰는 유틸

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
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
