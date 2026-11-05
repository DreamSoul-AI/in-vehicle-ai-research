"""Render concise decision views; evidence remains in the full research report."""
from html import escape


def validate_decision(data):
    score = data["score"]
    assert len(score["dimensions"]) == 5
    assert len(score["platforms"]) == 7
    for stage in ["voice", "panel"]:
        weights = score["stages"][stage]["weights"]
        assert len(weights) == 5 and sum(weights) == 100
        for platform in score["platforms"]:
            assert all(platform.get(field) for field in ["company", "companyLegal", "companyRole", "companyUrl"])
            assert platform["companyUrl"].startswith("https://")
            values = platform[stage]["scores"]
            if values is not None:
                assert len(values) == 5 and all(isinstance(value, int) and 1 <= value <= 5 for value in values)
                assert len(platform[stage]["reasons"]) == 5
            assert len(platform[stage]["tag"]) <= 9
    market = data["market"]
    assert market["eu"]["stock"] == 255999373
    assert abs(market["eu"]["petrol"] + market["eu"]["diesel"] - 87.6) < 0.001
    assert all(0 <= value <= 100 for value in market["defaults"].values())
    sample = market["channelExample"]
    assert sample["shops"] * sample["qualifiedLeadsPerMonth"] * sample["conversionPercent"] / 100 * sample["months"] == sample["annualUnits"]


def weighted_score(values, weights):
    if values is None:
        return None
    return sum(value * weight for value, weight in zip(values, weights)) / (5 * sum(weights)) * 100


def market_estimates(market, assumptions):
    base = market["eu"]["stock"] * (market["eu"]["petrol"] + market["eu"]["diesel"]) / 100
    gap = base * assumptions["gap"] / 100
    serviceable = gap * assumptions["compatible"] / 100
    annual = serviceable * assumptions["purchase"] / 100
    return base, gap, serviceable, annual


def volume(value):
    if value >= 100000000:
        return f"{value / 100000000:.2f}亿"
    if value >= 10000:
        return f"{value / 10000:,.1f}万"
    return f"{value:,.0f}"


def score_rows(score, stage):
    weights = score["stages"][stage]["weights"]
    platforms = sorted(score["platforms"], key=lambda item: weighted_score(item[stage]["scores"], weights) if item[stage]["scores"] else -1, reverse=True)
    result = []
    for item in platforms:
        value = weighted_score(item[stage]["scores"], weights)
        meter = '<span class="score-na">关联项</span>' if value is None else f'<span class="score-number">{value:.0f}</span><span class="score-track"><i style="width:{value}%"></i></span>'
        cells = ["—"] * 5 if value is None else [str(value) for value in item[stage]["scores"]]
        company = '<td class="score-company"><a href="' + escape(item["companyUrl"], quote=True) + '" title="' + escape(item["companyLegal"], quote=True) + '" target="_blank" rel="noopener noreferrer">' + escape(item["company"]) + '</a></td>'
        result.append('<tr><th scope="row"><button class="score-platform" data-score-platform="' + escape(item["id"]) + '">' + escape(item["name"]) + '</button><small>' + escape(item["type"]) + '</small></th>' + company + '<td>' + meter + '</td>' + ''.join('<td class="score-dimension">' + value + '</td>' for value in cells) + '<td><span class="score-tag">' + escape(item[stage]["tag"]) + '</span></td></tr>')
    return ''.join(result)


def render_scores(data):
    score = data["score"]
    dimensions = score["dimensions"]
    weights = score["stages"]["voice"]["weights"]
    columns = ''.join('<th class="score-dimension">' + escape(item["label"]) + '<small data-weight-share="' + str(index) + '">' + str(weights[index]) + '%</small></th>' for index, item in enumerate(dimensions))
    inputs = ''.join('<label>' + escape(item["label"]) + '<input type="number" min="0" max="100" step="1" value="' + str(weights[index]) + '" data-score-weight="' + str(index) + '" aria-label="' + escape(item["label"]) + '权重"></label>' for index, item in enumerate(dimensions))
    anchors = ''.join('<li><b>' + escape(item["label"]) + '</b>：' + escape(item["anchor"]) + '</li>' for item in dimensions)
    return '''<section class="decision-panel" id="platform-scores" aria-label="平台路线适配评分">
<div class="decision-heading"><span class="decision-kicker">现有平台与产品</span><h3>先看名字、公司与采用条件</h3><p>按采用现成方案的目标评分，满分100。点击名称查看理由，点击公司查看官方依据。</p></div>
<p class="cp-scope-note">本表是采用现成平台的无屏外设/面板路线参考，不覆盖LUMI类独立终端的完整方案。通用部署分按需要新增相容接收设备评估；已有CarPlay不再重复计算已有屏幕，先看 <a href="#carplay-focus">已有CarPlay接入专题</a>。</p>
<div class="decision-stage" role="group" aria-label="评分目标"><button data-score-stage="voice" aria-pressed="true">参照 · 无屏语音外设</button><button data-score-stage="panel" aria-pressed="false">第二阶段 · 智能面板</button></div>
<p class="decision-takeaway" id="score-takeaway">Apple Siri、Google Gemini按手机与语言分别验证；具体外设兼容需单独确认。</p>
<div class="score-table-wrap" tabindex="0" role="region" aria-label="路线评分表，可横向滚动"><table class="score-table"><thead><tr><th>平台 / 具体型号</th><th>公司</th><th>适配分</th>''' + columns + '''<th>采用建议</th></tr></thead><tbody id="score-rows">''' + score_rows(score, "voice") + '''</tbody></table></div>
<p class="decision-note">单项1–5分，高分更适配。研究判断，非实测排名；相差≤5分按同档理解。GAS依附系统伙伴，不单独计分。</p>
<details class="decision-details"><summary>评分标准、权重与不确定性</summary><div class="weight-controls">''' + inputs + '''</div><button class="text-button" id="score-reset">恢复该阶段默认权重</button><p id="score-input-status" role="status">默认权重合计100%；修改后自动归一化。</p><ul>''' + anchors + '''</ul><p>1分：本目标下需较多新增条件；3分：可行但有明显约束；5分：公开路径与目标高度吻合。2、4分为中间档。未知保持未知，未取得报价不计为零分。分差同档是阅读规则，不是统计置信区间。</p><p>仅比较已存在的平台与具体产品，按现成配置和公开合作入口评估，不预设本项目已开发手机软件或已取得系统权限。“可配置性”只计已有偏好、设置与厂商支持入口，旧版“流程自主”分数不直接沿用。具体手机、语言、设备和实车表现仍待验证。</p></details>
<p class="decision-links"><a href="#platform-evidence">展开平台依据 ↓</a> · <a href="#market-size">查看市场量级 ↓</a></p></section>'''


def render_market(data):
    market = data["market"]
    eu, poland, china = market["eu"], market["poland"], market["china"]
    base, gap, serviceable, annual = market_estimates(market, market["defaults"])
    source = '<a href="' + escape(eu["url"], quote=True) + '" target="_blank" rel="noopener noreferrer">ACEA 2026报告 · 统计2024年</a>'
    fields = [("gap", "入口缺口比例"), ("compatible", "手机与任务适配率"), ("purchase", "年度购买率")]
    controls = ''.join('<label>' + label + '<span><input id="market-' + identity + '" type="number" min="0" max="100" step="0.01" value="' + str(market["defaults"][identity]) + '" aria-label="' + label + '"> %</span></label>' for identity, label in fields)
    facts = [("2.56亿", "欧盟乘用车", "2024 · EU27"), ("约2.24亿", "汽油＋柴油", "87.6% · 由占比推算"), ("12.7年", "平均车龄", "ACEA口径 · 保加利亚缺报")]
    cards = ''.join('<div class="market-fact"><small>' + label + '</small><b>' + value + '</b><span>' + note + '</span></div>' for value, label, note in facts)
    return '''<section class="decision-panel market-panel" id="market-size" aria-label="市场量级与销量情景"><div class="decision-heading"><span class="decision-kicker">市场有多大</span><h3>存量大，能卖多少要再缩一层</h3><p>以欧盟同口径数据试算；波兰只作渠道案例。</p></div><div class="market-facts">''' + cards + '''</div><p class="decision-source">''' + source + ''' · 汽油、柴油不含混动与纯电。</p>
<div class="fuel-composition" role="img" aria-label="欧盟乘用车：汽油49.2%，柴油38.4%，其他12.4%"><span style="width:49.2%"></span><span style="width:38.4%"></span><span style="width:12.4%"></span></div><div class="fuel-legend"><span>汽油 49.2%</span><span>柴油 38.4%</span><span>混动、纯电等 12.4%</span></div>
<div class="scenario-heading"><h4>把假设代进去，看看数量级</h4><span class="assumption-badge">演算示例 · 非预测</span></div><div class="market-controls">''' + controls + '''</div>
<div class="market-funnel" aria-live="polite"><div><small>汽油＋柴油基数</small><b>约2.24亿</b><span>官方占比推算</span></div><i>→</i><div><small>存在入口缺口</small><b id="market-gap-result">''' + volume(gap) + '''辆</b><span>假设比例</span></div><i>→</i><div><small>技术可服务量</small><b id="market-sam-result">''' + volume(serviceable) + '''辆</b><span>再乘适配率</span></div><i>→</i><div><small>年度购买情景</small><b id="market-annual-result">''' + volume(annual) + '''台/年</b><span>再乘购买率</span></div></div>
<p class="decision-note" id="market-input-status" role="status">三个比例均为假设；尚无入口缺口、需求和购买率调查。车辆数不是车主数。</p>
<details class="decision-details"><summary>分母、计算方法与其他市场背景</summary><p>基数＝255,999,373辆×(49.2%＋38.4%)，约2.24亿辆。燃料占比已四舍五入，因此推算量也按约数表达。缺口量＝基数×入口缺口比例；技术可服务量＝缺口量×手机与任务适配率；年度购买量＝可服务量×年度购买率。默认10%/50%/1%只是用于演示的输入，不代表保守、基准或高概率预测。</p><p>“入口缺口”指缺少足够便利的车内任务入口；不是用车龄代替无CarPlay占比。适配率包括手机、语言、接口和任务条件；购买率需结合价格与真实试售。公开数据不提供这三个比例，也未提供本项目市场份额。</p><p>中国背景：2025年末民用轿车''' + volume(china["sedans"]) + '''辆，未取得同口径燃油/互联缺口细分；与欧盟乘用车分类不同，不相加。<a href="''' + escape(china["url"], quote=True) + '''">国家统计局2025公报</a></p></details>
<div class="channel-case"><div><span class="decision-kicker">渠道案例 · 波兰</span><h4>''' + volume(poland["stock"]) + '''辆乘用车</h4><p>''' + escape(poland["year"]) + ''' · 排除归档记录口径；非每天实际在用量。平均车龄''' + str(poland["age"]) + '''年。</p><a href="''' + escape(poland["url"], quote=True) + '''">PZPM / CEP 统计依据 ↗</a></div><div><h4>渠道销量从门店能力计算</h4><div class="channel-controls"><label>有效门店数<input id="channel-shops" aria-label="有效门店数" type="number" min="0" max="100000" step="1" value="0"></label><label>每店月合格客户<input id="channel-leads" aria-label="每店月合格客户" type="number" min="0" max="100000" step="1" value="0"></label><label>成交率 %<input id="channel-rate" aria-label="渠道成交率" type="number" min="0" max="100" step="0.5" value="0"></label></div><p class="channel-result" id="channel-result" aria-live="polite">渠道真实参数待填</p><button class="text-button" id="channel-example">载入演算示例</button><button class="text-button" id="channel-clear">清空示例</button><p class="decision-note">门店×月合格客户×成交率×12；未获伙伴经营数据。需另看退货、供货和现金约束。</p></div></div></section>'''
