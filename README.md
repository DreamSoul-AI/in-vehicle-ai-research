车载智能化研究网页。以小型语音助手为起点，逐步研究智能面板、辅助驾驶相关产品与后续大模型。功能、连接、安装、服务与经营条件优先。配色和信息呈现沿用桌面智能硬件研究网页。

在线阅读：[GitHub Pages](https://dreamsoul-ai.github.io/in-vehicle-ai-research/)。源码：[DreamSoul-AI/in-vehicle-ai-research](https://github.com/DreamSoul-AI/in-vehicle-ai-research)。

# 一、内容与目录
- `dist/index.html`：研究网页主入口
- `dist/app.js`、`dist/style.css`：交互与响应式样式
- `dist/data/products.json`：23个分阶段样本，默认展示16项语音和面板参照
- `dist/assets/products/`：当前产品与历史专项的官方来源配图，出处保留在产品记录中
- `dist/research.html`：当前产品与阶段路线调研
- `dist/outline.html`：当前调研大纲
- `dist/advanced.html`、`dist/data/advanced-products.json`：此前本地模型专项补充
- `dist/overview.html`：平台、技术与商业背景
- `dist/references.html`：参考资料与阅读范围
- `content/research.md`、`content/outline.md`：正式正文与大纲的网页发布副本，主页各节和完整正文从这里生成
- 平台章节前台展示100分适配评分与短标签，可切换无屏助手/智能面板并调整权重；详细两张平台表及七张卡片保留在展开区
- `content/decision.json`、`dist/data/decision.json`：评分原始值、权重、逐项理由、市场统计来源与演算参数；正式主数据位于上级 `车载智能化 评分与市场.json`
- `dist/decision.js`、`dist/decision.css`、`tools/decision_content.py`：评分、市场量级与渠道情景的静态初值和交互，页面直接嵌入同一JSON以保持口径一致
- `content/index.template.html`：页面结构及产品图鉴交互模板
- `dist/diagrams/`：9张 Mermaid 图的 SVG、PNG、图源及渲染清单，其中平台部分4张
- `build.py`、`tools/`：正文构建、图形渲染和发布文件校验

正式研究和结构化主数据位于上级目录。当前主数据为上级的 `车载智能化 产品样本.json`，正文和大纲采用同一课题前缀。此前 `燃油车端侧 AI` 文件保留为模型专题。网页数据与主数据的区别为增加本地配图路径。厂商声明、交付状态、离线范围与研究判断分别记录，开发演示和驾驶辅助模型不视为零售座舱助手。

# 二、本地预览
已提交的网页为静态 HTML、CSS、JavaScript，阅读和发布现有产物无需构建。在此目录运行：

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

访问 `http://127.0.0.1:8000/`。数据通过 `fetch` 载入，直接使用文件协议打开不会完整工作。打印按钮调用浏览器打印，打印范围随当前筛选结果变化。

## 正文与图示构建
当前工作区优先维护上级正式 Markdown，构建时使用 `--source` 和 `--outline` 同步到网页发布副本。独立检出网站仓库时可直接维护 `content/` 中的 Markdown。各节保留完整解释、表格、引用和图，首页另保留产品筛选、阶段选择和对比交互。

```powershell
python build.py --source "../车载智能化 通用调研.md" --outline "../车载智能化 通用调研大纲.md" --decision "../车载智能化 评分与市场.json" --prepare
node tools/render-diagrams.mjs --playwright "<现有 Playwright 模块路径>"
python build.py
python tools/check_site.py
```

Python 依赖版本见 `requirements-render.txt`。图形渲染使用固定 Mermaid 10.9.3、Playwright 1.62.1 及现有 Microsoft Edge，无须下载上游产品源码或运行其程序。Mermaid 文件和 MIT 许可保留在 `tools/vendor/`。已有 SVG/PNG 的普通浏览不依赖 Mermaid 或浏览器渲染工具。

构建记录每张图的源码哈希，源码变化后要求实际重新渲染，避免不同机制的图被同一段摘要替代。SVG 用于缩放，PNG 用于下载和兼容，网页提供50%至500%的大图阅读。成本公式使用原生 MathML。仅改文字且图源未变时，可直接运行 `python build.py`。

# 三、核验与维护
信息截止日为2026年11月5日。完成 JSON 字段、唯一编号、本地配图、HTML 链接、编码、JavaScript 语法和图源/渲染哈希核验。九张图均实际生成SVG与PNG，并检查文字未超出图形边界。浏览器检查覆盖图形放大与缩放、章节阅读、搜索、分类筛选、产品详情、跨产品对比、产品阶段切换及390像素移动布局。未验证竞品软件、实车表现、长期性能、非公开价格或经营数据。

修改产品记录时，先核对上级主数据、来源与日期，再更新网页副本。未公开价格不得填零，整车、组合包、软件和企业项目分别记录。来源图片仅作研究识别，不表示厂商合作或背书。

评分是针对本项目阶段目标的文档判断，非体验或性能排名。单项1–5，总分按实际权重归一化，GAS服务层不独立计分，未知许可费不填0。面板和无屏的原始分、默认权重与采用条件分别维护。正式Markdown中的简表须与JSON一同更新。

市场采用ACEA 2026报告中的2024 EU27乘用车数据，约2.24亿汽柴油车辆由已取整占比推算；波兰采用2025 PZPM更新记录，非实时在用普查。缺口、适配和购买比例无调查数据，所有结果均标为可修改的假设演算。渠道默认不填写实际规模，360台/年为明确标记的示例。网页计算不代表需求、合作方经营实绩或销量预测。

# 四、托管
主要发布入口为 GitHub Pages。源码仓库位于 `DreamSoul-AI/in-vehicle-ai-research`，保持私有，Pages 网页公开提供研究内容。

`main` 保存完整网站源码，`gh-pages` 保存从 `dist/` 提取的静态发布文件，Pages 从 `gh-pages` 分支根目录提供网页。不需要安装依赖或构建，站内资源使用相对路径以适配项目 Pages 子路径。

当前内容和图示版本为 `ratings-market-20261105`，由 `build.py` 统一写入资源与正文链接。后续结构调整时更新构建脚本的 `VERSION`，再构建静态产物。

完成修改和本地检查后，提交源码并发布：

```powershell
git push origin main
git subtree push --prefix dist origin gh-pages
```

等待 GitHub Pages 构建成功后，再检查在线页面及数据资源。此方式不需要新增 Actions 工作流授权。

先前的 Sites 私有预览保留，其身份记录位于 `.openai/hosting.json`，本次不更新该预览。GitHub Pages 为后续更新和分享入口。凭证不写入项目文件。

第三方品牌、图片和内容的权利归相应权利人。仓库未授予第三方素材新的复用许可，公开网页不代表素材为开源许可。
