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

正式研究和结构化主数据位于上级目录。当前主数据为上级的 `车载智能化 产品样本.json`，正文和大纲采用同一课题前缀。此前 `燃油车端侧 AI` 文件保留为模型专题。网页数据与主数据的区别为增加本地配图路径。厂商声明、交付状态、离线范围与研究判断分别记录，开发演示和驾驶辅助模型不视为零售座舱助手。

# 二、本地预览
本项目为静态 HTML、CSS、JavaScript，无安装和构建步骤。在此目录运行：

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

访问 `http://127.0.0.1:8000/`。数据通过 `fetch` 载入，直接使用文件协议打开不会完整工作。打印按钮调用浏览器打印，打印范围随当前筛选结果变化。

# 三、核验与维护
信息截止日为2026年11月5日。完成 JSON 字段、唯一编号、本地配图、HTML 链接、编码和 JavaScript 语法核验。浏览器检查覆盖搜索、分类筛选、产品详情、跨产品对比、产品阶段切换、全文链接及390像素移动布局。未验证竞品软件、实车表现、长期性能、非公开价格或经营数据。

修改产品记录时，先核对上级主数据、来源与日期，再更新网页副本。未公开价格不得填零，整车、组合包、软件和企业项目分别记录。来源图片仅作研究识别，不表示厂商合作或背书。

# 四、托管
主要发布入口为 GitHub Pages。源码仓库位于 `DreamSoul-AI/in-vehicle-ai-research`，保持私有，Pages 网页公开提供研究内容。

`main` 保存完整网站源码，`gh-pages` 保存从 `dist/` 提取的静态发布文件，Pages 从 `gh-pages` 分支根目录提供网页。不需要安装依赖或构建，站内资源使用相对路径以适配项目 Pages 子路径。

阶段结构改版使用 `product-stages-20261105` 作为资源与正文的统一版本参数。后续调整数据结构或交互时，同步更新 HTML 中的资源及站内正文链接、`app.js` 的数据请求参数。

完成修改和本地检查后，提交源码并发布：

```powershell
git push origin main
git subtree push --prefix dist origin gh-pages
```

等待 GitHub Pages 构建成功后，再检查在线页面及数据资源。此方式不需要新增 Actions 工作流授权。

先前的 Sites 私有预览保留，其身份记录位于 `.openai/hosting.json`，本次不更新该预览。GitHub Pages 为后续更新和分享入口。凭证不写入项目文件。

第三方品牌、图片和内容的权利归相应权利人。仓库未授予第三方素材新的复用许可，公开网页不代表素材为开源许可。
