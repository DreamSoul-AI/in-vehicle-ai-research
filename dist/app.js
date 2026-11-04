'use strict';

const state = { products: [], visible: [], selected: new Set() };
const $ = id => document.getElementById(id);
const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const asText = value => Array.isArray(value) ? value.map(x => String(x).replace(/[。；]+$/g,'')).join('；') : String(value ?? '未披露');
const short = (value, length = 115) => { const s = asText(value); return s.length > length ? s.slice(0, length) + '…' : s; };
const safeUrl = value => { try { const url = new URL(value, location.href); return ['http:', 'https:'].includes(url.protocol) ? url.href : '#'; } catch { return '#'; } };
const evidenceLabels = { local_llm: '本地语言 / 多模态模型', local_task: '本地任务型模型', hybrid: '端云混合', unknown: '本地模型待核', cloud: '联网功能对照' };
const segmentLabels = { aftermarket: '后装产品与软件', oem: '原厂车型', b2b: '企业方案', reference: '开发与邻接参考' };
const tagClass = p => ['local_llm','local_task'].includes(p.evidence) ? 'local' : p.evidence === 'hybrid' ? 'mixed' : 'unknown';
const sourceLink = source => `<a href="${escapeHtml(safeUrl(source.url))}" target="_blank" rel="noopener noreferrer">${escapeHtml(source.title)} ↗</a>`;

function imageMarkup(p, detail = false) {
  if (p.image?.local || p.image?.url) {
    const src = p.image.local || safeUrl(p.image.url);
    return `<img src="${escapeHtml(src)}" alt="${escapeHtml(p.name)}，${escapeHtml(p.image.credit || '官方资料配图')}" ${detail ? '' : 'loading="lazy"'}>`;
  }
  return `<div class="product-image-fallback" aria-label="此样本未收录官方图片"><span class="chip-icon" aria-hidden="true">${p.segment === 'oem' ? 'CAR' : 'AI'}</span><span>${escapeHtml(segmentLabels[p.segment])} · 未收录官方图</span></div>`;
}

function cardMarkup(p) {
  return `<article class="product-card" id="product-${escapeHtml(p.id)}">
    <div class="product-image">${imageMarkup(p)}<span class="category">${escapeHtml(segmentLabels[p.segment])}</span></div>
    <div class="product-copy"><div class="product-badges"><span class="tag ${tagClass(p)}">${escapeHtml(evidenceLabels[p.evidence])}</span><span class="tag neutral">${escapeHtml(p.stageLabel)}</span></div>
    <h3>${escapeHtml(p.name)}</h3><p class="product-maker">${escapeHtml(p.maker)}</p>
    <div class="product-price">${escapeHtml(p.price.card || p.price.display)}</div><p class="price-scope">${escapeHtml(short(p.price.scope, 85))}</p>
    <dl><dt>载体</dt><dd>${escapeHtml(short(p.compute, 85))}</dd><dt>模型</dt><dd>${escapeHtml(short(p.model, 90))}</dd><dt>离线</dt><dd>${escapeHtml(short(p.offline, 115))}</dd></dl>
    <div class="product-bottom"><button class="detail-button" data-detail="${escapeHtml(p.id)}">详细证据 ↗</button><label class="check"><input type="checkbox" data-select="${escapeHtml(p.id)}" ${state.selected.has(p.id) ? 'checked' : ''}>加入对比</label></div></div></article>`;
}

function applyFilters() {
  const query = $('search').value.trim().toLowerCase();
  const segment = $('segment').value;
  const evidence = $('evidence').value;
  state.visible = state.products.filter(p => {
    if (segment !== 'all' && p.segment !== segment) return false;
    if (evidence === 'core' && !p.coreEligible) return false;
    if (!['all','core'].includes(evidence) && p.evidence !== evidence) return false;
    if ($('available').checked && !p.obtainable) return false;
    return !query || [p.name,p.maker,p.compute,p.model,asText(p.functions),asText(p.offline)].join(' ').toLowerCase().includes(query);
  });
  $('result-count').textContent = `显示 ${state.visible.length} / ${state.products.length} 个研究样本 · 按证据与交付条件比较`;
  $('product-grid').innerHTML = state.visible.map(cardMarkup).join('');
  $('empty').hidden = state.visible.length > 0;
  $('comparison-body').innerHTML = state.visible.map(p => `<tr><td><b>${escapeHtml(p.name)}</b><small>${escapeHtml(p.stageLabel)} · ${escapeHtml(segmentLabels[p.segment])}</small></td><td>${escapeHtml(short(p.compute,140))}<small>${escapeHtml(short(p.model,130))}</small></td><td>${escapeHtml(asText(p.offline))}</td><td><b>${escapeHtml(p.price.display)}</b><small>${escapeHtml(p.price.scope)}</small></td><td>${p.sources.slice(0,2).map(sourceLink).join('<br>')}<br><button class="detail-button" data-detail="${escapeHtml(p.id)}">更多依据</button></td></tr>`).join('');
  bindImageErrors();
}

function bindImageErrors() {
  document.querySelectorAll('.product-image img').forEach(img => img.addEventListener('error', () => {
    const box = img.parentElement;
    img.remove();
    box.insertAdjacentHTML('afterbegin','<div class="product-image-fallback"><span class="chip-icon" aria-hidden="true">AI</span><span>配图暂不可用，请查看原始来源</span></div>');
  }, { once: true }));
}

function openDetail(id) {
  const p = state.products.find(item => item.id === id);
  if (!p) return;
  const functions = Array.isArray(p.functions) ? `<ul>${p.functions.map(x => `<li>${escapeHtml(x)}</li>`).join('')}</ul>` : escapeHtml(p.functions);
  $('detail-content').innerHTML = `<div class="detail-heading">${p.image?.local || p.image?.url ? imageMarkup(p,true) : ''}<div><div class="product-badges"><span class="tag ${tagClass(p)}">${escapeHtml(evidenceLabels[p.evidence])}</span><span class="tag neutral">${escapeHtml(p.stageLabel)}</span></div><h2 id="detail-title">${escapeHtml(p.name)}</h2><p>${escapeHtml(p.maker)} · ${escapeHtml(segmentLabels[p.segment])}</p></div></div>
  <dl class="detail-fields"><dt>实际状态</dt><dd>${escapeHtml(p.status)}</dd><dt>计算载体</dt><dd>${escapeHtml(p.compute)}</dd><dt>模型方案</dt><dd>${escapeHtml(p.model)}</dd><dt>主要功能</dt><dd>${functions}</dd><dt>离线边界</dt><dd>${escapeHtml(asText(p.offline))}</dd><dt>联网依赖</dt><dd>${escapeHtml(asText(p.online))}</dd><dt>公开价格</dt><dd><b>${escapeHtml(p.price.display)}</b><br>${escapeHtml(p.price.scope)}</dd></dl>
  <div class="detail-limits"><h3>如何理解这条证据</h3><p>${escapeHtml(asText(p.limits))}</p></div>
  <div class="detail-sources"><h3>原始资料</h3><ol>${p.sources.map(s => `<li>${sourceLink(s)}<small>${escapeHtml([s.date || '滚动页面',s.access ? '访问 '+s.access : '访问 2026-11-05'].join(' · '))}<br>${escapeHtml(s.scope || '')}</small></li>`).join('')}</ol>${p.image ? `<p>图片：${escapeHtml(p.image.credit)} · <a href="${escapeHtml(safeUrl(p.image.sourceUrl))}" target="_blank" rel="noopener noreferrer">原始出处 ↗</a></p>` : ''}</div>`;
  $('detail-dialog').showModal();
}

function updateSelection() {
  const selected = state.products.filter(p => state.selected.has(p.id));
  $('compare-tray').hidden = selected.length === 0;
  $('selection-label').textContent = `已选 ${selected.length} / 3 个产品`;
  $('open-compare').disabled = selected.length < 2;
  $('open-compare').title = selected.length < 2 ? '再选一个产品即可对比' : '打开所选产品对比';
  document.querySelectorAll('[data-select]').forEach(input => { input.checked = state.selected.has(input.dataset.select); });
}

function openComparison() {
  const products = state.products.filter(p => state.selected.has(p.id));
  if (products.length < 2) return;
  const rows = [['对象','kind'],['状态','status'],['载体 / 算力','compute'],['模型 / 技术','model'],['功能','functions'],['离线能力','offline'],['联网依赖','online'],['证据限制','limits']];
  $('compare-content').innerHTML = `<div class="table-wrap"><table><thead><tr><th>比较维度</th>${products.map(p=>`<th>${escapeHtml(p.name)}</th>`).join('')}</tr></thead><tbody>${rows.map(([label,key])=>`<tr><th>${label}</th>${products.map(p=>`<td>${escapeHtml(asText(p[key]))}</td>`).join('')}</tr>`).join('')}<tr><th>价格</th>${products.map(p=>`<td><b>${escapeHtml(p.price.display)}</b><small>${escapeHtml(p.price.scope)}</small></td>`).join('')}</tr><tr><th>依据</th>${products.map(p=>`<td>${p.sources.slice(0,3).map(sourceLink).join('<br>')}</td>`).join('')}</tr></tbody></table></div>`;
  $('compare-dialog').showModal();
}

const steps = {
  audio: ['车内拾音：先取得可靠输入','麦克风位置、回声消除、音乐和路噪决定输入质量。还要处理导航插播、通话抢占及用户打断。独立设备与复用原车麦克风的工程条件不同。'],
  asr: ['本地识别：语言支持需要变成任务表现','模型卡列出语种，只说明公开支持范围。目标设备上的地名、联系人、口音、混合语言和噪声准确性，需要单独验证。'],
  model: ['模型与记忆：资源预算看整条链','模型权重、上下文缓存、检索、音频组件和系统同时占用资源。本地记忆或规则助手不自动证明使用语言模型。'],
  tool: ['授权执行：生成意图不等于有执行权限','只接入获得授权的应用与车辆接口，校验参数、状态和执行结果。车况读取、舒适功能与车辆运动控制分别建立边界。'],
  tts: ['语音回复：听到有用结果才是体验','首段合成、播报长度与音频焦点共同影响延迟。要能及时打断、明确失败，并检查引擎、音色和依赖的商业许可。']
};
function showStep(key) {
  const [title,text] = steps[key];
  $('step-detail').innerHTML = `<h3>${title}</h3><p>${text}</p>`;
  document.querySelectorAll('[data-step]').forEach(button => button.setAttribute('aria-pressed',String(button.dataset.step===key)));
}

async function initialize() {
  try {
    const response = await fetch('data/products.json');
    if (!response.ok) throw new Error(`研究数据返回 ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data.products)) throw new Error('研究数据格式不正确');
    state.products = data.products;
    const local = state.products.filter(p=>p.coreEligible).length;
    const sources = new Map();
    state.products.forEach(p=>p.sources.forEach(s=>{if(!sources.has(s.url)) sources.set(s.url,s);}));
    $('stats').innerHTML = `<div class="stat"><b>${state.products.length}</b><span>分层研究样本</span></div><div class="stat"><b>${local}</b><span>本地模型线索</span></div><div class="stat"><b>${sources.size}</b><span>产品资料入口</span></div>`;
    $('source-list').innerHTML = [...sources.values()].map((s,i)=>`<div class="source-item"><span>${String(i+1).padStart(2,'0')}</span><div>${sourceLink(s)}<small>${escapeHtml(s.date || '滚动页面')} · 访问 ${escapeHtml(s.access || '2026-11-05')}<br>${escapeHtml(s.scope || '')}</small></div></div>`).join('');
    applyFilters();
    const target = new URLSearchParams(location.search).get('product');
    if (target) openDetail(target);
  } catch (error) {
    $('result-count').textContent = '研究数据暂未载入，请刷新或阅读完整专题。';
    $('stats').textContent = '研究数据暂未载入';
    console.error(error);
  }
}

['search','segment','evidence','available'].forEach(id=>$(id).addEventListener(id==='search'?'input':'change',applyFilters));
$('reset').addEventListener('click',()=>{$('search').value='';$('segment').value='all';$('evidence').value='core';$('available').checked=false;applyFilters();});
document.addEventListener('click',event=>{
  const detail=event.target.closest('[data-detail]'); if(detail) openDetail(detail.dataset.detail);
  const step=event.target.closest('[data-step]'); if(step) showStep(step.dataset.step);
  const close=event.target.closest('.close-dialog'); if(close) close.closest('dialog').close();
});
document.addEventListener('change',event=>{
  if(!event.target.matches('[data-select]')) return;
  const id=event.target.dataset.select;
  if(event.target.checked){if(state.selected.size>=3){event.target.checked=false;alert('最多同时比较三个产品。请先取消一个已选项。');return;}state.selected.add(id);}else state.selected.delete(id);
  updateSelection();
});
$('open-compare').addEventListener('click',openComparison);
$('clear-compare').addEventListener('click',()=>{state.selected.clear();updateSelection();});
$('print').addEventListener('click',()=>window.print());
document.querySelectorAll('dialog').forEach(dialog=>dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}}));
const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('.sidebar nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+entry.target.id));}});},{rootMargin:'-15% 0px -65% 0px'});
document.querySelectorAll('main section[id]').forEach(section=>observer.observe(section));
showStep('audio');
initialize();
