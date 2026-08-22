const PART_META = {
  mc: { label: "객관식", anchor: "part-mc" },
  short: { label: "단답형", anchor: "part-short" },
  essay: { label: "서술형", anchor: "part-essay" },
};

function storageKey(chapterId) {
  return `quiz-progress:${chapterId}`;
}

function loadProgress(chapterId) {
  try {
    const raw = localStorage.getItem(storageKey(chapterId));
    return raw ? JSON.parse(raw) : {};
  } catch (e) {
    return {};
  }
}

function saveProgress(chapterId, progress) {
  localStorage.setItem(storageKey(chapterId), JSON.stringify(progress));
}

function starText(n) {
  return n > 0 ? "★".repeat(n) : "";
}

function questionStatus(q, progress) {
  const p = progress[q.id];
  if (q.part === "mc") {
    if (!p || p.selected === undefined) return "unanswered";
    return p.correct ? "correct" : "wrong";
  }
  return p && p.reviewed ? "reviewed" : "unrevealed";
}

function matchesFilter(filter, q, status) {
  if (filter === "all") return true;
  if (filter === "review") {
    if (q.part === "mc") return status !== "correct";
    return status !== "reviewed";
  }
  return true;
}

function renderChoice(q, idx, text) {
  return `
    <button class="choice" data-idx="${idx}" type="button">
      <span class="mark">${CIRCLED[idx]}</span>
      <span>${formatText(text)}</span>
    </button>`;
}

function questionCardHtml(q) {
  const secTag = q.section
    ? `<span class="tag">${escapeHtml(q.section.key)}. ${escapeHtml(q.section.name)}</span>`
    : "";
  const star = q.star ? `<span class="star">${starText(q.star)}</span>` : "";
  const note = q.note ? `<div class="note">${formatText(q.note)}</div>` : "";

  let body = "";
  if (q.part === "mc") {
    body = `<div class="choices">${q.choices.map((c, i) => renderChoice(q, i, c)).join("")}</div>
      <div class="explanation-slot"></div>`;
  } else {
    body = `
      <button class="reveal-btn" type="button">모범답안 보기</button>
      <div class="answer-slot"></div>`;
  }

  return `
    <div class="card" id="q-${q.id}" data-id="${q.id}" data-part="${q.part}">
      <div class="card-head">
        <span class="qnum">${q.id}.</span>
        ${secTag}
        ${star}
        <span class="status-chip status-slot"></span>
      </div>
      <div class="stem">${formatText(q.stem)}</div>
      ${note}
      ${body}
    </div>`;
}

function renderStatusChip(card, q, progress) {
  const slot = card.querySelector(".status-slot");
  const status = questionStatus(q, progress);
  slot.className = "status-chip status-slot";
  if (status === "correct") {
    slot.classList.add("correct");
    slot.textContent = "정답";
  } else if (status === "wrong") {
    slot.classList.add("wrong");
    slot.textContent = "오답";
  } else if (status === "reviewed") {
    slot.classList.add("correct");
    slot.textContent = "확인함";
  } else {
    slot.textContent = "";
  }
}

function applyMcResult(card, q, progress) {
  const p = progress[q.id];
  const answered = !!(p && p.selected !== undefined);
  const buttons = card.querySelectorAll(".choice");
  buttons.forEach((btn) => {
    const idx = Number(btn.dataset.idx);
    btn.classList.remove("locked", "correct-choice", "wrong-choice", "picked");
    if (!answered) return;
    btn.classList.add("locked");
    if (idx === q.answerIndex) btn.classList.add("correct-choice");
    if (idx === p.selected && idx !== q.answerIndex) btn.classList.add("wrong-choice");
    if (idx === p.selected) btn.classList.add("picked");
  });
  const slot = card.querySelector(".explanation-slot");
  slot.innerHTML = answered
    ? `<div class="explanation"><span class="label">해설</span>${formatText(q.explanation || "(해설 없음)")}</div>`
    : "";
}

function applyShortEssayResult(card, q, progress) {
  const p = progress[q.id];
  const slot = card.querySelector(".answer-slot");
  const btn = card.querySelector(".reveal-btn");
  if (p && p.reviewed) {
    slot.innerHTML = `<div class="answer-text"><span class="label">모범답안</span>${formatText(q.answerText || "(모범답안 없음)")}</div>`;
    btn.textContent = "모범답안 숨기기";
  } else {
    slot.innerHTML = "";
    btn.textContent = "모범답안 보기";
  }
}

async function main() {
  const params = new URLSearchParams(location.search);
  const chapterId = params.get("ch");
  const root = document.getElementById("app");

  if (!chapterId) {
    root.innerHTML = `<div class="empty-state">강의를 선택해주세요. <a href="index.html">목록으로</a></div>`;
    return;
  }

  let chapter;
  try {
    chapter = await loadJson(`data/${chapterId}.json`);
  } catch (e) {
    root.innerHTML = `<div class="empty-state">${escapeHtml(chapterId)} 데이터를 불러오지 못했어요.<br>${escapeHtml(e.message)}</div>`;
    return;
  }

  document.title = `${chapterId} · 문제풀이`;

  let progress = loadProgress(chapterId);
  let filter = "all";

  const sectionSummary = chapter.sections.map((s) => `${s.key}. ${s.name}`).join(" · ");

  root.innerHTML = `
    <div class="topbar">
      <h1>${escapeHtml(chapterId)}</h1>
      <a class="back" href="index.html">← 목록으로</a>
    </div>
    <p class="subtitle">${escapeHtml(sectionSummary)}</p>

    <div class="progress-bar">
      <div class="progress-inner">
        <span class="score" id="score-text"></span>
        <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
        <div class="controls">
          <button class="filter-btn" data-filter="all" type="button" aria-pressed="true">전체</button>
          <button class="filter-btn" data-filter="review" type="button" aria-pressed="false">복습 모드(오답·미확인)</button>
          <button class="reset-btn" id="reset-btn" type="button">진행 초기화</button>
        </div>
      </div>
    </div>

    <div class="section-nav">
      <a href="#part-mc">객관식 ${chapter.counts.mc}</a>
      <a href="#part-short">단답형 ${chapter.counts.short}</a>
      <a href="#part-essay">서술형 ${chapter.counts.essay}</a>
    </div>

    ${chapter.studyGuide ? `<details class="guide"><summary>📌 이 문제 이렇게 공부해요</summary><div class="body">${formatText(chapter.studyGuide)}</div></details>` : ""}

    <div id="parts"></div>

    ${chapter.appendix ? `<details class="appendix"><summary>🔑 시험 직전 핵심 요약</summary><div class="body">${formatText(chapter.appendix)}</div></details>` : ""}
  `;

  const partsEl = document.getElementById("parts");
  const order = ["mc", "short", "essay"];
  partsEl.innerHTML = order
    .map((part) => {
      const qs = chapter.questions.filter((q) => q.part === part);
      if (qs.length === 0) return "";
      const meta = PART_META[part];
      return `
        <div class="part-heading" id="${meta.anchor}" data-part="${part}">${meta.label} <span class="count">${qs.length}문항</span></div>
        ${qs.map(questionCardHtml).join("")}
      `;
    })
    .join("");

  partsEl.insertAdjacentHTML(
    "beforeend",
    '<div class="empty-state review-empty" hidden>복습할 오답이나 미확인 문제가 없습니다.</div>',
  );

  renderMath(root); // 학습 가이드/부록 등 카드 밖 수식 렌더링 (카드 안 수식은 renderCardState에서 처리)

  function updateScore() {
    const mcTotal = chapter.counts.mc;
    let mcAnswered = 0;
    let mcCorrect = 0;
    let reviewTotal = chapter.counts.short + chapter.counts.essay;
    let reviewed = 0;
    chapter.questions.forEach((q) => {
      const p = progress[q.id];
      if (q.part === "mc") {
        if (p && p.selected !== undefined) {
          mcAnswered++;
          if (p.correct) mcCorrect++;
        }
      } else if (p && p.reviewed) {
        reviewed++;
      }
    });
    document.getElementById("score-text").textContent =
      `객관식 ${mcAnswered}/${mcTotal} · 정답 ${mcCorrect}` +
      (reviewTotal ? ` · 단답/서술 확인 ${reviewed}/${reviewTotal}` : "");
    document.getElementById("progress-fill").style.width = mcTotal
      ? `${(mcAnswered / mcTotal) * 100}%`
      : "0%";
  }

  function applyFilter() {
    let visibleCount = 0;
    document.querySelectorAll(".card").forEach((card) => {
      const q = chapter.questions.find((x) => x.id === Number(card.dataset.id));
      const status = questionStatus(q, progress);
      const show = matchesFilter(filter, q, status);
      card.classList.toggle("hidden-by-filter", !show);
      if (show) visibleCount++;
    });
    document.querySelectorAll(".part-heading").forEach((heading) => {
      const hasVisibleCard = document.querySelector(
        `.card[data-part="${heading.dataset.part}"]:not(.hidden-by-filter)`,
      );
      heading.classList.toggle("hidden-by-filter", !hasVisibleCard);
    });
    document.querySelector(".review-empty").hidden = filter !== "review" || visibleCount > 0;
  }

  function renderCardState(card) {
    const q = chapter.questions.find((x) => x.id === Number(card.dataset.id));
    renderStatusChip(card, q, progress);
    if (q.part === "mc") applyMcResult(card, q, progress);
    else applyShortEssayResult(card, q, progress);
    renderMath(card);
  }

  document.querySelectorAll(".card").forEach((card) => {
    const qid = Number(card.dataset.id);
    const q = chapter.questions.find((x) => x.id === qid);

    if (q.part === "mc") {
      card.querySelectorAll(".choice").forEach((btn) => {
        btn.addEventListener("click", () => {
          if (progress[qid] && progress[qid].selected !== undefined) return; // 잠금
          const idx = Number(btn.dataset.idx);
          progress[qid] = { selected: idx, correct: idx === q.answerIndex };
          saveProgress(chapterId, progress);
          renderCardState(card);
          updateScore();
          applyFilter();
        });
      });
    } else {
      card.querySelector(".reveal-btn").addEventListener("click", () => {
        const current = progress[qid] && progress[qid].reviewed;
        progress[qid] = { reviewed: !current };
        saveProgress(chapterId, progress);
        renderCardState(card);
        updateScore();
        applyFilter();
      });
    }

    renderCardState(card);
  });

  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      filter = btn.dataset.filter;
      document.querySelectorAll(".filter-btn").forEach((b) => {
        const active = b === btn;
        b.classList.toggle("active", active);
        b.setAttribute("aria-pressed", String(active));
      });
      applyFilter();
    });
  });
  document.querySelector('.filter-btn[data-filter="all"]').classList.add("active");

  document.getElementById("reset-btn").addEventListener("click", () => {
    if (!confirm(`${chapterId}의 풀이 기록을 모두 초기화할까요?`)) return;
    progress = {};
    saveProgress(chapterId, progress);
    document.querySelectorAll(".card").forEach(renderCardState);
    updateScore();
    applyFilter();
  });

  updateScore();
  applyFilter();
}

main();
