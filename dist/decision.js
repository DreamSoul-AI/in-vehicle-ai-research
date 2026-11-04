"use strict";

(() => {
  const dataNode = document.getElementById("decision-data");
  if (!dataNode) return;
  const data = JSON.parse(dataNode.textContent);
  const score = data.score;
  let stage = "voice";
  const esc = (value) => String(value).replace(/[&<>"']/g, (char) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char]));
  const numeric = (input) => {
    if (input.value.trim() === "") return null;
    const value = Number(input.value);
    return Number.isFinite(value) && input.checkValidity() ? value : null;
  };
  const sum = (values) => values.reduce((a, b) => a + b, 0);
  const total = (values, weights) => values === null ? null : sum(values.map((value, index) => value * weights[index])) / (5 * sum(weights)) * 100;
  const weights = () => [...document.querySelectorAll("[data-score-weight]")].map(numeric);
  const volume = (value) => value >= 1e8 ? (value / 1e8).toFixed(2) + "亿" : value >= 1e4 ? (value / 1e4).toLocaleString("zh-CN", {minimumFractionDigits:1, maximumFractionDigits:1}) + "万" : Math.round(value).toLocaleString("zh-CN");
  const safeLink = (url) => {
    try { const result = new URL(url); return result.protocol === "https:" ? result.href : "#"; }
    catch { return "#"; }
  };

  function updateScores() {
    const current = weights();
    const status = document.getElementById("score-input-status");
    if (current.some((value) => value === null) || sum(current) === 0) {
      status.textContent = "权重需在0–100内，且至少一项大于0；表格保留上次有效结果。";
      return;
    }
    const ranked = [...score.platforms].sort((a, b) => (total(b[stage].scores, current) ?? -1) - (total(a[stage].scores, current) ?? -1));
    document.getElementById("score-rows").innerHTML = ranked.map((item) => {
      const value = total(item[stage].scores, current);
      const number = value === null ? '<span class="score-na">关联项</span>' : '<span class="score-number">' + Math.round(value) + '</span><span class="score-track"><i style="width:' + value + '%"></i></span>';
      const cells = item[stage].scores === null ? Array(5).fill("—") : item[stage].scores;
      return '<tr><th scope="row"><button class="score-platform" data-score-platform="' + esc(item.id) + '">' + esc(item.name) + '</button><small>' + esc(item.type) + '</small></th><td class="score-company"><a target="_blank" rel="noopener noreferrer" href="' + esc(safeLink(item.companyUrl)) + '" title="' + esc(item.companyLegal) + '">' + esc(item.company) + '</a></td><td>' + number + '</td>' + cells.map((value) => '<td class="score-dimension">' + value + '</td>').join("") + '<td><span class="score-tag">' + esc(item[stage].tag) + '</span></td></tr>';
    }).join("");
    document.querySelectorAll("[data-weight-share]").forEach((node) => { node.textContent = Math.round(current[Number(node.dataset.weightShare)] / sum(current) * 100) + "%"; });
    document.getElementById("score-takeaway").textContent = stage === "voice" ? "Apple Siri、Google Gemini按手机与语言分别验证；具体外设兼容需单独确认。" : "面板比较Apple CarPlay与Google Android Auto；ATOTO S84G209P是明确的后装车机参照。";
    status.textContent = "当前权重合计" + sum(current) + "，总分按实际权重归一化；单项仍为1–5分。";
  }

  function resetWeights() {
    document.querySelectorAll("[data-score-weight]").forEach((input, index) => { input.value = score.stages[stage].weights[index]; });
    updateScores();
  }

  function detail(item) {
    const dialog = document.getElementById("score-dialog");
    const current = weights();
    const valid = !current.includes(null) && sum(current) > 0;
    const value = valid ? total(item[stage].scores, current) : null;
    const values = item[stage].scores;
    const displayValue = values === null ? "不单独计分" : !valid ? "权重待修正" : Math.round(value) + '<small> / 100</small>';
    const companyMarkup = '<p class="score-company-detail"><b>公司：</b><a target="_blank" rel="noopener noreferrer" href="' + esc(safeLink(item.companyUrl)) + '">' + esc(item.companyLegal) + '</a><br><b>对应关系：</b>' + esc(item.companyRole) + (item.companyNotes ? '<br>' + esc(item.companyNotes) : '') + '</p>';
    document.getElementById("score-detail-title").textContent = item.name + " · " + score.stages[stage].label;
    document.getElementById("score-detail-content").innerHTML = '<p class="score-detail-number">' + displayValue + '</p><p><b>采用条件：</b>' + esc(item.prerequisite) + '</p><p class="decision-note">判断依据：' + esc(item.confidence) + '；尚未进行目标组合实测。</p>' + (values === null ? '<p>GAS提供授权服务层，依附AAOS与系统伙伴，不作为独立完整方案参与总分排名。</p>' : '<dl class="score-reasons">' + score.dimensions.map((dimension, index) => '<div><dt>' + esc(dimension.label) + ' <b>' + values[index] + '/5</b></dt><dd>' + esc(item[stage].reasons[index]) + '</dd></div>').join("") + '</dl>') + '<h3>直接依据</h3><ul>' + item.sources.map((source) => '<li><a target="_blank" rel="noopener noreferrer" href="' + esc(safeLink(source.url)) + '">' + esc(source.title) + ' ↗</a></li>').join("") + '</ul><p class="decision-note">分值是目标和条件下的研究判断，非厂商认可、真实用户评价或独立性能测量。</p>';
    document.getElementById("score-detail-content").insertAdjacentHTML("afterbegin", companyMarkup);
    dialog.showModal();
  }

  function updateMarket() {
    const fields = ["gap", "compatible", "purchase"].map((key) => numeric(document.getElementById("market-" + key)));
    const status = document.getElementById("market-input-status");
    if (fields.some((value) => value === null)) { status.textContent = "三个比例需在0–100%内；结果保留上次有效输入。"; return; }
    const eu = data.market.eu;
    const base = eu.stock * (eu.petrol + eu.diesel) / 100;
    const gap = base * fields[0] / 100;
    const serviceable = gap * fields[1] / 100;
    const annual = serviceable * fields[2] / 100;
    document.getElementById("market-gap-result").textContent = volume(gap) + "辆";
    document.getElementById("market-sam-result").textContent = volume(serviceable) + "辆";
    document.getElementById("market-annual-result").textContent = volume(annual) + "台/年";
    status.textContent = "假设演算：" + fields[0] + "%入口缺口 × " + fields[1] + "%适配 × " + fields[2] + "%年度购买。比例未经调查，不是销量预测。";
  }

  function updateChannel(example = false) {
    const [shops, leads, rate] = ["shops", "leads", "rate"].map((key) => numeric(document.getElementById("channel-" + key)));
    const result = document.getElementById("channel-result");
    if ([shops, leads, rate].some((value) => value === null)) { result.textContent = "请填写有效的门店、客户数和成交率。"; return; }
    if (shops === 0 || leads === 0) { result.textContent = "渠道真实参数待填"; return; }
    const annual = shops * leads * rate / 100 * 12;
    result.textContent = volume(annual) + "台/年 · " + shops + "店 × " + leads + "人/月 × " + rate + "% × 12" + (example ? "（演算示例）" : "（输入情景，非实绩）");
  }

  document.addEventListener("click", (event) => {
    const stageButton = event.target.closest("[data-score-stage]");
    if (stageButton) {
      stage = stageButton.dataset.scoreStage;
      document.querySelectorAll("[data-score-stage]").forEach((button) => button.setAttribute("aria-pressed", String(button === stageButton)));
      resetWeights();
    }
    const platform = event.target.closest("[data-score-platform]");
    if (platform) detail(score.platforms.find((item) => item.id === platform.dataset.scorePlatform));
  });
  document.getElementById("score-reset")?.addEventListener("click", resetWeights);
  document.getElementById("score-close")?.addEventListener("click", () => document.getElementById("score-dialog").close());
  document.querySelectorAll("[data-score-weight]").forEach((input) => input.addEventListener("input", updateScores));
  document.querySelectorAll(".market-controls input").forEach((input) => input.addEventListener("input", updateMarket));
  document.querySelectorAll(".channel-controls input").forEach((input) => input.addEventListener("input", () => updateChannel()));
  document.getElementById("channel-example")?.addEventListener("click", () => {
    const sample = data.market.channelExample;
    ["shops", "leads", "rate"].forEach((key, index) => { document.getElementById("channel-" + key).value = [sample.shops, sample.qualifiedLeadsPerMonth, sample.conversionPercent][index]; });
    updateChannel(true);
  });
  document.getElementById("channel-clear")?.addEventListener("click", () => {
    document.querySelectorAll(".channel-controls input").forEach((input) => { input.value = 0; }); updateChannel();
  });
  // Links to evidence remain usable when its long-form container is collapsed.
  document.addEventListener("click", (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    const target = document.getElementById(link.hash.slice(1));
    if (!target) return;
    let parent = target;
    while (parent) { if (parent.tagName === "DETAILS") parent.open = true; parent = parent.parentElement; }
  });
  function revealHash(scroll = false) {
    const target = document.getElementById(location.hash.slice(1));
    if (!target) return;
    let parent = target;
    while (parent) { if (parent.tagName === "DETAILS") parent.open = true; parent = parent.parentElement; }
    if (scroll === true) target.scrollIntoView({behavior:"instant", block:"start"});
  }
  addEventListener("hashchange", () => revealHash());
  document.addEventListener("research-ready", () => revealHash(true), {once:true});
  revealHash(!document.getElementById("product-grid") || document.documentElement.dataset.researchReady === "true");
})();
