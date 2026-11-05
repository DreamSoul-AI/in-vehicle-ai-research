"use strict";
const state = { products: [], visible: [], selected: new Set(), stages: [] };
const $ = (id) => document.getElementById(id);
const escapeHtml = (v) =>
  String(v ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
const asText = (v) =>
  Array.isArray(v)
    ? v.map((x) => String(x).replace(/[。；]+$/g, "")).join("；")
    : String(v ?? "未核实");
const short = (v, n = 105) => {
  const t = asText(v);
  return t.length > n ? t.slice(0, n) + "…" : t;
};
const safeUrl = (v) => {
  try {
    const u = new URL(v, location.href);
    return ["https:", "http:"].includes(u.protocol) ? u.href : "#";
  } catch {
    return "#";
  }
};
const phaseNames = {
  voice: "1 · 语音助手",
  panel: "2 · 智能面板",
  assist: "3 · 辅助驾驶",
  advanced: "4 · 大模型增强",
};
const phaseIcons = {
  voice: "VOICE",
  panel: "PANEL",
  assist: "ADAS",
  advanced: "AI",
};
const sourceLink = (s) =>
  `<a href="${escapeHtml(safeUrl(s.url))}" target="_blank" rel="noopener noreferrer">${escapeHtml(s.title)} ↗</a>`;
function imageMarkup(p, detail = false) {
  if (p.image?.local || p.image?.url)
    return `<img src="${escapeHtml(p.image.local || safeUrl(p.image.url))}" alt="${escapeHtml(p.name)}，${escapeHtml(p.image.credit || "原始资料配图")}" ${detail ? "" : 'loading="lazy"'}>`;
  return `<div class="product-image-fallback"><span class="chip-icon" aria-hidden="true">${phaseIcons[p.phase]}</span><span>未收录官方产品图</span></div>`;
}
function card(p) {
  return `<article class="product-card" id="product-${escapeHtml(p.id)}"><div class="product-image">${imageMarkup(p)}<span class="category">${phaseNames[p.phase]}</span></div><div class="product-copy"><div class="product-badges"><span class="tag ${p.availability === "current" ? "local" : "unknown"}">${escapeHtml(p.stageLabel)}</span><span class="tag neutral">${escapeHtml(p.form)}</span></div><h3>${escapeHtml(p.name)}</h3><p class="product-maker">${escapeHtml(p.maker)}</p><div class="product-price">${escapeHtml(p.price.card || p.price.display)}</div><p class="price-scope">${escapeHtml(short(p.price.scope, 85))}</p><dl><dt>任务</dt><dd>${escapeHtml(short(p.functions, 90))}</dd><dt>安装</dt><dd>${escapeHtml(short(p.install, 90))}</dd><dt>依赖</dt><dd>${escapeHtml(short(p.dependencies, 110))}</dd></dl><div class="product-bottom"><button class="detail-button" data-detail="${escapeHtml(p.id)}">详细资料 ↗</button><label class="check"><input type="checkbox" data-select="${escapeHtml(p.id)}" ${state.selected.has(p.id) ? "checked" : ""}>加入对比</label></div></div></article>`;
}
function applyFilters() {
  const q = $("search").value.trim().toLowerCase(),
    phase = $("phase").value,
    status = $("status-filter").value;
  state.visible = state.products.filter((p) => {
    if (phase === "starter" && !["voice", "panel"].includes(p.phase))
      return false;
    if (!["starter", "all"].includes(phase) && p.phase !== phase) return false;
    if (status !== "all" && p.availability !== status) return false;
    return (
      !q ||
      [
        p.name,
        p.maker,
        p.form,
        asText(p.functions),
        asText(p.dependencies),
        p.install,
        p.audio,
        p.model,
      ]
        .join(" ")
        .toLowerCase()
        .includes(q)
    );
  });
  $("result-count").textContent =
    `显示 ${state.visible.length} / ${state.products.length} 个分阶段样本`;
  $("product-grid").innerHTML = state.visible.map(card).join("");
  $("empty").hidden = state.visible.length > 0;
  $("comparison-body").innerHTML = state.visible
    .map(
      (p) =>
        `<tr><td><b>${escapeHtml(p.name)}</b><small>${escapeHtml(p.stageLabel)} · ${phaseNames[p.phase]}</small><button class="detail-button" data-detail="${escapeHtml(p.id)}">查看依据</button></td><td>${escapeHtml(asText(p.functions))}</td><td>${escapeHtml(asText(p.install))}<small>${escapeHtml(asText(p.audio))}</small></td><td>${escapeHtml(asText(p.dependencies))}</td><td><b>${escapeHtml(p.price.display)}</b><small>${escapeHtml(p.price.scope)}</small></td></tr>`,
    )
    .join("");
  document.querySelectorAll(".product-image img").forEach((img) =>
    img.addEventListener(
      "error",
      () => {
        img.parentElement.innerHTML =
          '<div class="product-image-fallback">配图暂不可用，请查看原始资料</div>';
      },
      { once: true },
    ),
  );
}
function openDetail(id) {
  const p = state.products.find((x) => x.id === id);
  if (!p) return;
  const fields = [
    ["产品形态", p.form],
    ["当前核查状态", p.status],
    ["主要功能", p.functions],
    ["实现方式", p.model],
    ["安装与供电", p.install],
    ["音频路径", p.audio],
    ["手机及服务依赖", p.dependencies],
    ["离线范围", p.offline],
    ["对本阶段的启示", p.lesson],
  ];
  $("detail-content").innerHTML =
    `<div class="detail-heading">${p.image ? imageMarkup(p, true) : ""}<div><span class="tag neutral">${phaseNames[p.phase]}</span><h2 id="detail-title">${escapeHtml(p.name)}</h2><p>${escapeHtml(p.maker)}</p></div></div><dl class="detail-fields">${fields.map(([k, v]) => `<dt>${k}</dt><dd>${escapeHtml(asText(v))}</dd>`).join("")}<dt>价格口径</dt><dd><b>${escapeHtml(p.price.display)}</b><br>${escapeHtml(p.price.scope)}</dd></dl><div class="detail-limits"><h3>证据与使用边界</h3><p>${escapeHtml(asText(p.limits))}</p></div><div class="detail-sources"><h3>原始资料</h3><ol>${p.sources.map((s) => `<li>${sourceLink(s)}<small>${escapeHtml(s.date || "滚动页面")} · 访问 ${escapeHtml(s.access || "2026-11-05")}<br>${escapeHtml(s.scope || "")}</small></li>`).join("")}</ol>${p.image ? `<p>配图：${escapeHtml(p.image.credit || "原始产品资料")} · <a href="${escapeHtml(safeUrl(p.image.sourceUrl))}" target="_blank" rel="noopener noreferrer">原始出处 ↗</a></p>` : ""}</div>`;
  $("detail-dialog").showModal();
}
function updateSelection() {
  const n = state.selected.size;
  $("compare-tray").hidden = n === 0;
  $("selection-label").textContent = `已选 ${n} / 3 个产品`;
  $("open-compare").disabled = n < 2;
  document.querySelectorAll("[data-select]").forEach((input) => {
    input.checked = state.selected.has(input.dataset.select);
  });
}
function openComparison() {
  const products = state.products.filter((p) => state.selected.has(p.id));
  if (products.length < 2) return;
  const fields = [
    ["产品形态", "form"],
    ["状态", "status"],
    ["功能", "functions"],
    ["实现方式", "model"],
    ["安装与供电", "install"],
    ["音频路径", "audio"],
    ["手机与服务", "dependencies"],
    ["离线范围", "offline"],
    ["阶段启示", "lesson"],
    ["证据边界", "limits"],
  ];
  $("compare-content").innerHTML =
    `<div class="table-wrap"><table><thead><tr><th>维度</th>${products.map((p) => `<th>${escapeHtml(p.name)}</th>`).join("")}</tr></thead><tbody>${fields.map(([k, v]) => `<tr><th>${k}</th>${products.map((p) => `<td>${escapeHtml(asText(p[v]))}</td>`).join("")}</tr>`).join("")}<tr><th>价格</th>${products.map((p) => `<td>${escapeHtml(p.price.display)}<small>${escapeHtml(p.price.scope)}</small></td>`).join("")}</tr><tr><th>资料</th>${products.map((p) => `<td>${p.sources.slice(0, 3).map(sourceLink).join("<br>")}</td>`).join("")}</tr></tbody></table></div>`;
  $("compare-dialog").showModal();
}
function showStage(id) {
  const p = state.stages.find((x) => x.id === id);
  if (!p) return;
  document
    .querySelectorAll("[data-stage]")
    .forEach((button) =>
      button.setAttribute("aria-pressed", String(button.dataset.stage === id)),
    );
  $("stage-detail").innerHTML =
    `<div class="stage-title"><span class="tag mixed">${escapeHtml(p.label)}</span><h3>${escapeHtml(p.title)}</h3><p>${escapeHtml(p.job)}</p></div><dl><dt>可以积累或复用</dt><dd>${escapeHtml(asText(p.reuse))}</dd><dt>本阶段新增工作</dt><dd>${escapeHtml(asText(p.add))}</dd><dt>继续推进的条件</dt><dd>${escapeHtml(p.gate)}</dd></dl><button class="detail-button" data-phase-link="${id}">查看这一阶段的产品 →</button>`;
}
async function initialize() {
  try {
    const response = await fetch("data/products.json?v=editorial-review-20261106");
    if (!response.ok) throw new Error(`数据返回 ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data.products) || !Array.isArray(data.stages))
      throw new Error("产品数据结构错误");
    state.products = data.products;
    state.stages = data.stages;
    const initial = state.products.filter((p) =>
      ["voice", "panel"].includes(p.phase),
    ).length;
    $("stats").innerHTML =
      `<div class="stat"><b>独立</b><span>首款硬件形态</span></div><div class="stat"><b>4</b><span>产品研究阶段</span></div><div class="stat"><b>${initial}</b><span>语音与面板样本</span></div>`;
    const sources = new Map();
    [
      ...(data.sources || []),
      ...state.products.flatMap((p) => p.sources),
    ].forEach((s) => {
      if (!sources.has(s.url)) sources.set(s.url, s);
    });
    $("source-list").innerHTML = [...sources.values()]
      .map(
        (s, i) =>
          `<div class="source-item"><span>${String(i + 1).padStart(2, "0")}</span><div>${sourceLink(s)}<small>${escapeHtml(s.date || "滚动页面")} · 访问 ${escapeHtml(s.access || "2026-11-05")}<br>${escapeHtml(s.scope || "")}</small></div></div>`,
      )
      .join("");
    applyFilters();
    showStage("voice");
    const id = new URLSearchParams(location.search).get("product");
    if (id) openDetail(id);
  } catch (e) {
    $("result-count").textContent = "产品资料未载入，请刷新或阅读完整调研。";
    console.error(e);
  } finally {
    document.documentElement.dataset.researchReady = "true";
    document.dispatchEvent(new Event("research-ready"));
  }
}
["search", "phase", "status-filter"].forEach((id) =>
  $(id).addEventListener(id === "search" ? "input" : "change", applyFilters),
);
$("reset").addEventListener("click", () => {
  $("search").value = "";
  $("phase").value = "starter";
  $("status-filter").value = "all";
  applyFilters();
});
document.addEventListener("click", (event) => {
  const detail = event.target.closest("[data-detail]");
  if (detail) openDetail(detail.dataset.detail);
  const stage = event.target.closest("[data-stage]");
  if (stage) showStage(stage.dataset.stage);
  const phase = event.target.closest("[data-phase-link]");
  if (phase) {
    $("phase").value = phase.dataset.phaseLink;
    $("search").value = "";
    $("status-filter").value = "all";
    applyFilters();
    location.hash = "products";
  }
  const close = event.target.closest(".close-dialog");
  if (close) close.closest("dialog").close();
});
document.addEventListener("change", (event) => {
  if (!event.target.matches("[data-select]")) return;
  const id = event.target.dataset.select;
  if (event.target.checked) {
    if (state.selected.size >= 3) {
      event.target.checked = false;
      alert("最多比较三个产品，请先取消一个已选项。");
      return;
    }
    state.selected.add(id);
  } else state.selected.delete(id);
  updateSelection();
});
$("open-compare").addEventListener("click", openComparison);
$("clear-compare").addEventListener("click", () => {
  state.selected.clear();
  updateSelection();
});
$("print").addEventListener("click", () => window.print());
document.querySelectorAll("dialog").forEach((dialog) =>
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      const r = dialog.getBoundingClientRect();
      if (
        event.clientX < r.left ||
        event.clientX > r.right ||
        event.clientY < r.top ||
        event.clientY > r.bottom
      )
        dialog.close();
    }
  }),
);
const observer = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (e.isIntersecting)
        document
          .querySelectorAll(".sidebar nav a")
          .forEach((a) =>
            a.classList.toggle("active", a.hash === "#" + e.target.id),
          );
    }),
  { rootMargin: "-15% 0px -65% 0px" },
);
document
  .querySelectorAll("main > .research-section[id]")
  .forEach((s) => observer.observe(s));
initialize();
