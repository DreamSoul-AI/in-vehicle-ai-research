整理日期：2026年11月6日。研究面向存量燃油车的轻量智能化，比较小型语音硬件、现有车载平台与竞品，并评估智能面板、辅助驾驶和后续大模型能力的进入条件。

**建议先验证便于安装、少操作的独立车载语音硬件，包括轻量音箱和LUMI类交互终端。** 本机、手机与在线服务按任务分工；有无表情小屏、是否接入CarPlay，均由使用需求决定。首期优先验证触发、连接、反馈和任务完成的价值，本地大模型作为可选的后续能力。

依据为官方产品页、手册、平台文档及企业披露的针对性阅读。价格、销售状态和统计数据各保留日期；尚未采购、激活竞品服务或进行实车测试。详细阅读范围见第七章。

# 一、产品起点与渐进路线
## （一）首款以少操作的任务入口建立购买理由
先研究用户为何需要一个实体设备，再决定语音和任务怎样实现。Avantree CK11、Roadtrip提供手机助手外设参照，LUMI提供实体交互参照；具体能力与供货证据见第三章。

客户先按原车接口和实际困难划分。缺少蓝牙、AUX 的用户可能更需要自带扬声器，已有基础蓝牙的用户可能更需要触发与反馈，已有稳定 CarPlay 或 Android Auto 的用户则已有较完整入口。燃油类型无法代替这种细分。首期可研究“接受手机联网、希望免拆安装、尚无好用车内入口”的用户，但这仍是客群假设，需观察他们已有手机方案的不足。

购买理由要与手机直接使用比较：上车后少了哪些配置，实体按键和反馈是否更方便，任务是否更容易完成，断网或来电后能否恢复。拾音、表情和动作只有在改善具体体验时，才构成设备价值。

## （二）四阶段分别有目标与进入条件
图中是研究提出的产品扩展方向，第三阶段分为记录预警和车辆运动辅助。各箭头代表需要重新确认的能力与经营条件。

```mermaid
%% title: 产品阶段与进入条件
flowchart TB
  A[第一阶段 轻量语音硬件] -->|验证任务与复用| B[第二阶段 智能面板]
  B -->|摄像 标定与提示评测| C[第三阶段A 记录和风险提示]
  C -.->|车型接口与安全验证| D[第三阶段B 车辆运动辅助]
  A -.-> E[按增量任务价值选择大模型能力]
  B -.-> E
  C -.-> E
```

这不是技术上的强制同序。大模型可在前期出现明确需求时独立评估，记录提示也可以成为长期独立产品。前一阶段用户量、售出设备或渠道规模，都不能代替下一阶段的产品和技术证据。

| **扩展方向** | **可复用** | **新增重点** | **进入条件** |
|---|---|---|---|
| 语音硬件 → 面板 | 已验证任务、部分音频适配、支持经验 | 显示交互、安装供电、系统维护 | 固定显示确有增量价值 |
| 面板 → 记录预警 | 适用的显示、电源、交付流程 | 摄像标定、存储、感知评测 | 记录或提醒有效，限制明确 |
| 记录预警 → 运动辅助 | 适用的设备管理和服务经验 | 车型接口、实时控制、安全验证 | 具体车型和专业合作落实 |
| 已有产品 → 模型能力 | 任务、授权知识、工具、评测样例 | 许可、算力或云费、可靠性维护 | 同任务增量覆盖新增成本 |

渠道、客户和部分工程经验可以复用，车辆接口、道路数据及控制验证需要另行取得。

## （三）允许停留、合作和调整方向
每阶段都应回答三个问题：用户为什么购买，产品怎样稳定交付，实际净收入能否承担对应责任。若手机已满足需求，可以调整客群或服务。若面板增量不足，可以继续经营轻量外设。若进入驾驶辅助，专业合作可能比全部自研更合适。区域市场也按同一方法核验，波兰仅作客群、渠道、语言和交付条件待核的案例。

推进依据来自任务完成、用户复用、供应报价、支持负担和现金需求。销量、BOM与融资需求需在具体方案和报价明确后测算。

# 二、平台与载体
重点比较Apple CarPlay与Google Android Auto，并把语音助手、车内系统和具体硬件放到各自层次。先解释名称，再看接法、评分、安装和音频。

<!-- carplay-focus:start -->

## （一）平台概念与CarPlay接入专题

<section class="cp-primer" id="carplay-basics" aria-labelledby="cp-basics-title">
<p class="cp-primer-kicker">先认识这些名字</p>
<h3 id="cp-basics-title">CarPlay是什么，和Siri有什么关系？</h3>
<p><b>CarPlay是Apple（苹果公司）提供的手机与汽车互联功能。</b> 把iPhone连接到支持CarPlay的车辆或后装车机后，就能通过车屏、音响和车内控件使用支持的导航、电话、音乐等功能。</p>
<p>它是iPhone系统的互联功能，不是另装的一款手机App，也不是整车操作系统。原生及第三方应用均须符合车内使用规则；应用上架App Store或Google Play，与适配车屏是两件事。</p>
<div class="cp-concept-grid">
<article class="cp-concept"><span>手机与汽车互联 · Apple 苹果</span><h4>CarPlay</h4><p>把iPhone中支持的应用带到车内界面，方便看地图、听音乐、打电话。</p><small>使用条件：iPhone＋相容车机</small></article>
<article class="cp-concept"><span>手机与汽车互联 · Google 谷歌</span><h4>Android Auto</h4><p>让Android手机中支持的应用通过相容车屏和控件使用。</p><small>使用条件：受支持Android手机＋相容车机</small></article>
<article class="cp-concept"><span>语音助手 · Apple 苹果</span><h4>Siri</h4><p>接收你说出的请求，调用支持的电话、地图、音乐等功能；也可在iPhone上使用。</p><small>在CarPlay里，Siri提供语音交互</small></article>
<article class="cp-concept"><span>AI助手 · Google 谷歌</span><h4>Gemini</h4><p>提供对话及受支持的任务；满足手机、账号、语言和地区条件时，也可在Android Auto中使用。</p><small>助手能力与互联功能分别核查</small></article>
</div>
<div class="cp-everyday-example"><b>举个例子：你说“导航去公司”</b><p>在支持的iPhone与CarPlay组合中，各部分这样分工：</p><ol class="cp-example-flow"><li><strong>iPhone</strong><span>Siri接收语音请求<br/>地图应用提供路线</span></li><li><strong>CarPlay</strong><span>把支持的导航界面<br/>带到车内显示与操作</span></li><li><strong>车机与音响</strong><span>车屏显示地图<br/>车内音响播放导航提示</span></li></ol><small>这是分工示意，实际支持的任务、地图应用与语音入口依配置而定。</small></div>

<details class="cp-terms"><summary>后文的车机、AAOS、GAS和适配器分别是什么？</summary><dl>
<div><dt>车机 / 接收主机</dt><dd>车内负责多媒体显示、声音和相关操作的设备。“接收主机”强调它接收CarPlay或Android Auto的角色，具体由车厂或设备厂商提供。</dd></div>
<div><dt>AAOS / Google主导的开源系统</dt><dd>Android Automotive OS，直接运行在车内硬件上的汽车操作系统。它与连接手机使用的Android Auto分工不同。</dd></div>
<div><dt>GAS / Google授权服务</dt><dd>Google Automotive Services，是车厂可选择授权集成的一组Google应用与服务。采用AAOS，不代表已经包含GAS。</dd></div>
<div><dt>ATOTO S84G209P / Aotule品牌方</dt><dd>本报告选取的一款具体后装车机，需安装进车辆。它是设备型号，不是与CarPlay同类的通用平台名称。</dd></div>
<div><dt>有线改无线适配器</dt><dd>接在已有相容车机上，让手机省去插线步骤的小盒子。它需要车机原本具备相应互联能力；仅有普通USB口还不够。</dd></div>
</dl></details>
<p class="cp-primer-sources">导读依据（2026年11月6日核对）：<a href="https://www.apple.com/ios/carplay/">Apple CarPlay介绍</a>、<a href="https://developer.android.com/training/cars/platforms/android-auto">Google Android Auto介绍</a>、<a href="https://support.google.com/gemini/answer/16735982?hl=en">Google车内Gemini说明</a>、<a href="https://source.android.com/docs/automotive/start/what_automotive">AAOS与GAS定义</a>、<a href="https://www.carlinkit.com/2air">Carlinkit适配器使用条件</a>。ATOTO型号与公司依据见后文详情。</p>
</section>

<!-- hardware-access:start -->

### 独立小硬件、蓝牙和原车接口怎样选择
**先看任务是否需要原车资源，再选连接方式。** 自带麦克风与扬声器的小设备，可由本机功能、手机软件和所需服务协作；需要原车音响、车屏或车辆数据时，再分别选择接法。

| **要完成的事** | **接入点** | **关键条件** |
|---|---|---|
| 设备自己收音、播报 | 本机；按需连手机 | 任务与服务分工 |
| 借原车音响播放 | 相容蓝牙音频、AUX等 | 音源与恢复 |
| 地图或界面进入车屏 | CarPlay、Android Auto或车机应用接口 | 类别、模板与准入 |
| 外部麦克风或按键加入车机 | 指定主机接口与固件 | 输入路由与型号 |
| 读取车况或控制车辆 | 对应车辆API、适配设备或厂商合作 | 车型与读写权限 |

**蓝牙连通、取得应用接口和获得车辆权限，是不同条件。** 普通蓝牙音频可以解决部分播放或免提任务；实际使用哪个麦克风、来电后怎样恢复仍需核对。CarPlay/Android Auto提供受支持的车内应用体验，不能概括为通用车控接口。部分车况API及车厂应用的能力须逐项核查。[Android蓝牙配置](https://developer.android.com/develop/connectivity/bluetooth/profiles)、[Apple CarPlay](https://developer.apple.com/carplay/)、[车况API](https://developer.android.com/training/cars/apps/library/car-hardware-api)

```mermaid
%% title: 从任务选择独立硬件与原车接口
%% 分析示意，分支不代表已有软件、授权或兼容。
flowchart TB
    A[硬件需要哪种能力]
    A -->|任务可在本机闭环| B[本机语音与任务软件]
    A -->|需要手机任务| C[核实手机入口与权限<br/>实测触发和音频路由]
    A -->|需要原车屏界面| D[相容投射或车机应用接口<br/>按对应准入与权限适配]
    A -->|需要主机按钮或麦克风| E[核实具体型号接口<br/>必要时取得厂商合作]
    A -->|需要车辆数据或控制| F[核实车辆接口授权<br/>逐项确认读写与责任]
```

<details class="cp-terms"><summary>导航进入原车屏：地图、界面和操作由谁负责？</summary>
<p>这里讨论原车屏显示地图、路线和接受操作。若选择通过iPhone进入已有CarPlay车屏，导航应用需要按其导航类别适配并取得相应权限；Android Auto也有独立的导航模板与声明要求。</p>
<p>第三方 CarPlay 导航应用的地图由 iPhone 上的应用绘制：应用把地图绘制控制器放入 CarPlay 提供的窗口；<code>CPMapTemplate</code> 等模板承载规定的导航控件、路线预览与引导信息。路线由导航应用及其采用的地图／路线服务组织，CarPlay 框架本身不替开发者提供通用算路服务。应用能绘制地图，不意味着可以任意绘制整屏按钮、弹窗或覆盖层，其他界面应使用平台规定的模板。<a href="https://developer.apple.com/documentation/carplay/displaying-content-in-carplay">Apple：Displaying Content in CarPlay</a>、<a href="https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf">CarPlay Developer Guide，导航章节</a></p>
<p>Android Auto 的对应机制是应用在主机提供的 <code>Surface</code> 上绘制地图，<code>NavigationTemplate</code>／<code>MapWithContentTemplate</code> 等组织受约束的导航界面，并由应用向主机报告行程信息。两者的共同分工是：<strong>手机导航应用提供地图与导航内容，平台管理车内界面规则及交互，接收主机负责显示并传回支持的触控／旋钮等输入。</strong> 支持的输入方式按主机而定；这不等于新增语音外设可以直接控制地图，也不等于将导航应用完整安装到了车机上。<a href="https://developer.android.com/training/cars/apps/library/draw-maps">Google：Draw maps</a>、<a href="https://developer.android.com/training/cars/apps/navigation">Build a navigation app</a></p>
</details>

<!-- hardware-access:end -->

### 已有CarPlay时，新增设备改善什么
新增外设可以无屏，车内仍可已有CarPlay屏。应先比较原车入口，再确认新设备在触达、反馈或任务上的增量。

<div class="cp-baseline"><b>先用原车建立基线</b><span>方向盘语音键 → Apple Siri → 导航、电话、媒体 → 原车屏与音响</span><small>已是CarPlay的现有能力；再加一个语音设备的增量尚未证明。</small></div>

### CarPlay专项：外设、应用服务和接收硬件三条路径

<div class="cp-route-grid">
<article class="cp-route"><span class="cp-route-number">01 / 外设体验</span><h4>沿用 Apple Siri</h4><p>外设不加屏；验证触发、固定与音频体验。</p><strong>新增配件链路待核</strong><a href="#cp-accessory">具体怎样做 ↓</a></article>
<article class="cp-route"><span class="cp-route-number">02 / 应用服务</span><h4>CarPlay 内提供新任务</h4><p>需新增软件工作，或与获准服务提供方合作。</p><strong>非当前已具备能力</strong><a href="#cp-service">软件与许可路径 ↓</a></article>
<article class="cp-route"><span class="cp-route-number">03 / 硬件合作</span><h4>与接收主机方案合作</h4><p>把按键、麦克风和固件接口落实到具体设备。</p><strong>需厂商接口与认证核查</strong><a href="#cp-hardware">硬件角色与边界 ↓</a></article>
</div>

| **接法** | **主要接入点** | **手机新增软件** | **首期先验证** |
|---|---|---|---|
| 沿用Siri | 相容触发与音频 | 不以新增软件为前提 | 比原车入口多什么 |
| CarPlay应用服务 | iPhone应用及CarPlay框架 | 新增开发或合作 | 任务差异与类别资格 |
| 接收硬件合作 | 具体主机、接口、固件 | 取决于方案 | 接口、责任与成本 |

外设体验、应用服务和接收硬件分别对应不同接口与责任。原车Siri入口由Apple支持说明界定，第三方应用按类别授权，接收硬件按相应MFi技术要求处理。[Apple使用CarPlay](https://support.apple.com/en-us/108415)、[CarPlay开发入口](https://developer.apple.com/carplay/)、[MFi FAQ](https://mfi.apple.com/en/faqs)

```mermaid
%% title: 已有CarPlay时，小外设接在哪里
%% 分析示意；实线为已有基线，虚线为尚需验证的新增外设输入，不代表已兼容。
%% 来源 https://support.apple.com/en-us/108415
%% 来源 https://developer.apple.com/carplay/
flowchart TB
  subgraph EXISTING["已有车辆与Apple CarPlay基线"]
    START["方向盘语音键 / 车屏入口<br/>支持时使用语音唤起"] --> MIC["原车 / 接收机麦克风<br/>实际输入随配置核查"]
    MIC --> PHONE["iPhone上的Siri或支持的应用<br/>任务服务按条件联网"]
    PHONE --> OUTPUT["原车屏幕与音响<br/>显示、播报及恢复"]
  end
  EXTRA["拟议无屏小外设<br/>按键或外部拾音"] -.->|"触发与输入路由均未证"| PHONE
  EXTRA -.->|"只有主机明确提供接口时"| MIC
  VALUE["产品增量需实测<br/>少操作 / 更易触达 / 更稳恢复"]
  EXTRA --> VALUE
```

<a id="cp-accessory"></a>

### 路径一：已有CarPlay，先验证无屏小外设的增量
以“上车后去公司、给联系人打电话、继续播放”为具体任务。先用原车方向盘键、原车麦克风和Apple Siri完成同一流程，记录用户实际不方便的环节。若确有触达或反馈问题，再研究小按钮、固定方式或设备侧反馈；若目标是改善拾音，必须先确定接收主机是否提供外部麦克风输入，或手机音频会话是否能使用目标输入。

**新增配件的触发和音频路由须单独验证。** 蓝牙音箱与CarPlay接收机都可能连接手机；并用时要确认实际麦克风、输出和来电恢复。未开启CarPlay时能调用Siri，不代表开启后行为相同。

<details class="cp-detail"><summary>停车设置与日常操作，具体检查什么</summary>
<ol><li><b>停车准备：</b>记录iPhone/iOS、车型/年份、接收主机固件、有线或无线CarPlay及目标语言；不加外设先完成原车任务。</li><li><b>安装配对：</b>明确配件连接手机还是主机、占哪个USB/蓝牙或物理接口；记录电源和实际麦克风来源。</li><li><b>日常使用：</b>上车连接CarPlay → 使用已证实的触发方式 → 等待提示 → 说出任务 → 由Siri与支持的应用处理 → 通过原车界面确认结果。</li><li><b>打断恢复：</b>加入音乐播放中触发、来电、锁屏、重复按键、断网和重新上车；核对是否丢失声音、重复执行或需要重新配对。</li><li><b>继续条件：</b>相对原车基线，完整任务、操作负担或恢复确有改善，且足以承担新增设备与支持成本；若只是重复方向盘已有按钮，先停止这一客群的硬件方案。</li></ol>
</details>

Avantree Roadtrip的官方按键说明可作“外设调用手机Siri”的现成例子，不能作为它与任意CarPlay主机并用的认证。CK11指南还提示语音命令使用手机麦克风，说明外设有通话麦克风不等于已改善Siri拾音。[Roadtrip助手说明](https://support.avantree.com/hc/en-us/articles/38121800304793-Roadtrip-How-to-activate-the-voice-assistant-with-the-car-kit-Siri-Google-Assistant)、[CK11语音说明](https://support.avantree.com/hc/en-us/articles/50767188774937-How-to-Make-a-Call-by-Voice-Command)

<a id="cp-service"></a>

### 路径二：要提供平台原本没有的任务，才研究应用服务
Apple已有voice-based conversational应用类别，公开指南列其最低系统为iOS26.4；这是特定应用类别的门槛，不是所有CarPlay的统一门槛。该路径是在iPhone上运行获准的应用，通过CarPlay界面和音频交互提供其任务，**不需要另造一块屏，也不必额外卖一只音箱。** [CarPlay指南](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf)，印刷第8、13–15、27、30、67页。

项目目前没有获准CarPlay应用或已确认软件伙伴。先找出Siri和现有应用尚未满足的具体服务，再评估开发或合作投入；单纯重复导航、拨号和播放，购买理由较弱。

<details class="cp-detail"><summary>应用准入、语音会话与执行边界</summary>
<ul><li><b>准入：</b>明确应用主功能与类别，申请对应CarPlay entitlement，按模板实现、签名、测试并接受分发审核；第三方获得批准不等于本项目已获准。</li><li><b>启动：</b>用户进入相应CarPlay应用后进行语音交互；不能因有语音类别就承诺接管Siri、原车语音键或系统唤醒词。</li><li><b>录音：</b>录音须结合Voice Control模板，语音服务活动期间显示相应状态界面；只在语音功能实际使用时保持音频会话，处理权限、取消、焦点变化与中断，不能据此承诺全天后台监听。</li><li><b>任务：</b>应用只处理自身服务与获准接口内的动作。iOS27讲稿展示通过CarPlay场景URL发起导航、电话请求，但转交不证明最终完成，也不能任意控制其他应用。</li><li><b>版本：</b>iOS27将Voice Control模板扩展到更多类别，不意味着全部录音、车辆或后台特权同时开放。系统、类别和具体功能版本分别核验。</li></ul>
<p>Apple提供框架与审核；软件提供方承担具体任务、服务、会话和版本维护；车厂或主机提供车内接口。语音识别可以按任务使用现成组件、规则或云服务，这条路线本身不要求车内本地大模型。</p>
</details>

```mermaid
%% title: 可选CarPlay语音应用的完整任务流程
%% 分析示意；这是需要新增软件或合作的路线，不是已具备能力。
%% 来源 https://developer.apple.com/carplay/
%% 来源 https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf
%% 来源 https://developer.apple.com/videos/play/wwdc2026/212/
flowchart TB
  SETUP["停车准备<br/>相容iPhone / 授权应用 / 账号与必要权限"] --> ENTRY["用户打开获准的CarPlay应用<br/>不是自动接管Siri或方向盘键"]
  ENTRY --> LISTEN["Voice Control状态界面<br/>实际语音期间启用会话与录音"]
  LISTEN --> TASK["限定任务处理<br/>已有服务、规则或按需云能力"]
  TASK --> CHECK{"参数与任务执行权限明确"}
  CHECK -->|"是"| ACTION["在可用范围内执行或转交<br/>导航 / 拨号等依具体接口"]
  CHECK -->|"否"| CONFIRM["补充确认 / 说明缺失 / 取消"]
  CONFIRM -->|"补充后重新检查"| CHECK
  ACTION --> RESULT["反馈实际可观测状态<br/>请求转交不等于任务完成"]
  RESULT --> END["结束录音和音频会话<br/>中断后恢复原有音源"]
  CONFIRM -->|"取消或不能执行"| END
```

<a id="cp-hardware"></a>

### 路径三：与主机或配件方案合作，把硬件接入做实
如果卖点是外部按键、拾音或一体化安装，应先找能提供明确接口与固件责任的接收主机/设备伙伴。要求对方说明按键信号怎样传入、音频输入输出怎样选择、是否保持原CarPlay体验、哪些车型固件被支持。仅写“支持CarPlay”不足以证明这些接口开放。

采用MFi技术的CarPlay接收硬件，与普通标准蓝牙配件的要求不同；整机认证、品牌方与ODM责任需分别确认。公开MFi FAQ没有给出本项目可直接采用的完整保密规格、许可费用或合作资格，因此这条路线先做方案与商务核查。[Apple MFi FAQ](https://mfi.apple.com/en/faqs)

**有线改无线适配器是连接产品，不能直接叫语音助手。** 比如Carlinkit CPC200-2air的官网重点是把相容有线入口改为无线并保留原车操作；不能从它能传递现有语音操作，推导盒子增加了语音理解、麦克风或独立任务服务。[Carlinkit 2air](https://www.carlinkit.com/2air)

现成无屏控制器例子是**Ottocast OttoSafe Knob**（品牌Ottocast，法律公司主体待核）。官网说明可配Mini NOVA、Mini Pico、U2Air Edge及相应更新固件，旋转浏览、按压确认或返回/Home；不同页面段落的完整清单并不一致，实际套餐仍需确认。这说明新增外设可以借用原车屏，不证明它提供语音拾音、常驻Siri或外接麦克风。[Ottocast官方商品页](https://www.ottocast.com/products/ottosafe-knob)

三条路线分别交付外设体验、具体服务或接收硬件集成，成本和维护责任也不同。渠道已有CarPlay客户，仍需确认他们的实际缺口。

### Android Auto对照：相似入口，接入规则分别核验

| **问题** | **Apple CarPlay / Apple** | **Android Auto / Google** |
|---|---|---|
| 已有助手 | Siri | Gemini等，按手机与账号 |
| 已有触发 | 方向盘、车屏、支持的唤起 | 方向盘、车屏、Hey Google |
| 新语音应用 | 有语音对话类别及授权 | 通用对话类别未列 |
| 应用录音 | 类别、模板与会话限制 | 录音许可及音频焦点 |
| 额外麦克风 | 具体主机/路由待核 | 具体主机/路由待核 |

Google公开说明了既有Android Auto车辆的Gemini入口；第三方应用仍按支持类别、质量与分发条件接入。CarAudioRecord可在授权后读取车内录音，但它不是把任意蓝牙麦克风指定给系统助手的接口。不能把CarPlay的语音对话类别直接套给Android Auto。[Gemini车内帮助](https://support.google.com/gemini/answer/16735982?hl=en)、[Android车载类别](https://developer.android.com/training/cars)、[车载录音](https://developer.android.com/training/cars/apps/library/car-microphone)

### 如何选择接入路线
独立硬件先验证自身任务；需要复用CarPlay时，再从外设、应用服务、接收硬件中选择一条路径。已有CarPlay车辆以原车体验为基线，不重复计算已有屏幕的新增成本。该细分客群的付费缺口和规模仍需调查。

<!-- carplay-focus:end -->


## （二）现有平台与产品适配评分
<!-- score-summary:start -->
评分对象全部为现有平台或具体产品。公司和平台对应关系可直接追到官方资料；分数针对本项目采用现成方案的适配度，非平台性能排名。 本表保留采用现成平台的无屏外设/面板路线参考，不覆盖LUMI类独立交互终端的完整技术方案，也不预设首款必须无屏。

| **平台 / 具体型号** | **公司** | **无屏助手** | **智能面板** |
|---|---|---:|---:|
| Apple CarPlay | Apple | 64 | 74 |
| Google Android Auto | Google | 64 | 74 |
| AAOS（AOSP） | Google | 34 | 44 |
| Google GAS | Google | — | — |
| Apple Siri | Apple | 88 | 66 |
| Google Gemini | Google | 70 | 63 |
| ATOTO S84G209P | Aotule | 54 | 66 |

五维依次为部署匹配、任务复用、可配置性、接入可得、维护易度；可配置性只计已有设置、偏好与厂商支持入口。首期权重30/30/10/20/10%，面板期20/20/25/20/15%。总分＝100×各维分数与权重乘积之和÷(5×权重总和)。分差不超过5分按同档理解，未知不填0，GAS服务层不独立计总分。

CarPlay/Android Auto的部署分按需新增相容接收设备评估；已有相容系统的车辆不适用该扣分，应按原车体验另判。Siri需支持的手机、语言和外设；Gemini通用车载蓝牙按钮兼容未证；ATOTO S84G209P为双DIN拆装车机。原始分、逐维理由、公司主体与来源见 [评分与市场数据](<车载智能化 评分与市场.json>)。

<!-- score-summary:end -->

## （三）现有平台横向对比
比较共同任务：在传统车辆上使用导航、通话、媒体与简单语音入口。公司字段表示品牌、产品发行或项目主导方，实际地区服务合同与销售主体仍按相应条款核对；不同层次的对象可以组合，不是七套可互换的操作系统。

### 使用能力
名称链接指向对应平台或型号，公司链接指向官方主体依据。离线按具体任务、设备与语言核查。

| **平台 / 方案** | **主要任务与入口** | **应用在哪里运行** | **手机与屏幕条件** | **离线范围** |
|---|---|---|---|---|
| [Apple CarPlay](https://developer.apple.com/carplay/)<br>[Apple](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)<br>手机投射 | iPhone导航、音频、电话、消息；Siri及车内控件 | iPhone应用与Apple车内交互框架 | 相容iPhone与CarPlay接收设备；有线/无线按机型 | 地图、下载内容和Siri任务分别核，不保证整链离线 |
| [Google Android Auto](https://developer.android.com/training/cars/platforms/android-auto)<br>[Google](https://play.google.com/store/apps/details?id=com.google.android.projection.gearhead&hl=en)<br>手机投射 | 相容导航、媒体、通信；支持的车内语音入口 | 以Android手机应用服务提供车内界面 | 受支持Android手机与接收设备；当前要求按组合核对 | 按App和助手任务核查；数据套餐条件不等于本机离线系统 |
| [Android Automotive OS](https://source.android.com/docs/automotive/start/what_automotive)<br>[Google / AOSP](https://source.android.com/docs/setup/about)<br>车内系统基座 | 本机应用、音频与车内系统整合；服务需集成 | 车内硬件；由车厂或设备商形成具体系统 | 本机运行不靠手机投射；通信等另核 | 取决于安装的地图、语音和执行组件 |
| [Google GAS / Google built-in](https://source.android.com/docs/automotive/start/what_automotive)<br>[Google](https://developers.google.com/cars)<br>服务层与集成体验 | 获授权的Google地图、应用及车载服务 | GAS为服务集合，Google built-in为集成体验 | 依赖相应车内系统；通话、短信按官方流程配对手机 | 部分Assistant任务、预下载地图可离线；不外推全部Gemini会话 |
| [ATOTO S8 Gen4 S84G209P](https://www.atotodirect.com/de-us/products/atoto-s84g209p-9inch-double-din-car-stereo-eu)<br>[Aotule](https://www.atotodirect.com/en-gb/pages/about-atoto)<br>具体后装车机 | 本机导航、媒体、DriveChat及CarPlay/Android Auto | 该型号的Android 13 / AICE UI 13系统 | 双DIN拆装及线束适配；投射需手机，DriveChat设置用厂商SSHub | 收音机/本地媒体按功能；DriveChat明确需联网 |
| [Apple Siri](https://support.apple.com/en-ie/guide/iphone/iph0aa8c80e6/27/ios/27)<br>[Apple](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)<br>现有手机助手 | Apple支持的电话、导航、媒体等语音任务 | iPhone与Apple相关服务 | 相容iPhone、语言和设置；具体按键及拾音另核 | 受设备、语言与任务限制，不等于完整离线助手 |
| [Google Gemini](https://support.google.com/gemini/answer/14554984?hl=en)<br>[Google](https://play.google.com/store/apps/details?id=com.google.android.apps.bard&hl=en)<br>现有手机助手 | Google支持的问答及通信、地图、媒体任务 | Android手机与Google服务 | 需相容手机、Google官方软件/默认助手设置；目标车载外设待核 | 相容外设方案有联网要求；不据蓝牙连接推导离线 |

### 接入、责任与采用条件
这里分别核查现成使用入口、平台公开开发规则和设备接口，不能从“可安装应用”推导已取得系统或车辆控制权。

| **平台 / 方案** | **应用与硬件接入** | **车辆权限边界** | **费用与交付责任** | **采用判断** |
|---|---|---|---|---|
| [Apple CarPlay](https://developer.apple.com/carplay/)<br>[Apple](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)<br>手机投射 | 使用相容接收设备和已有iPhone应用；新增App类别授权与MFi接收硬件是不同路径 | 普通CarPlay不提供任意车控；车厂集成另核 | 接收设备、手机、内容与相关许可分别计 | 面板阶段的iPhone生态基线 |
| [Google Android Auto](https://developer.android.com/training/cars/platforms/android-auto)<br>[Google](https://play.google.com/store/apps/details?id=com.google.android.projection.gearhead&hl=en)<br>手机投射 | 使用相容接收设备和受支持手机应用；类别、质量与分发规则明确 | 部分车况读取依API、权限和车型；不等于通用控制 | 设备、手机、数据、内容和兼容支持另计 | 面板阶段的Android生态基线 |
| [Android Automotive OS](https://source.android.com/docs/automotive/start/what_automotive)<br>[Google / AOSP](https://source.android.com/docs/setup/about)<br>车内系统基座 | 采用已有AAOS具体系统需核车厂/设备商服务与配置 | VHAL与系统特权由具体实现及授权决定 | AOSP代码基座开放；整机、移植、维护和服务不自动免费 | 先找明确系统伙伴，不当作零售车机 |
| [Google GAS / Google built-in](https://source.android.com/docs/automotive/start/what_automotive)<br>[Google](https://developers.google.com/cars)<br>服务层与集成体验 | GAS由汽车OEM选择授权；不是给任意旧车下载的完整套件 | Google服务许可不等于全部车厂权限 | 具体商业许可和车型服务套餐待核 | 关联服务项，不独立计总分 |
| [ATOTO S8 Gen4 S84G209P](https://www.atotodirect.com/de-us/products/atoto-s84g209p-9inch-double-din-car-stereo-eu)<br>[Aotule](https://www.atotodirect.com/en-gb/pages/about-atoto)<br>具体后装车机 | 现有FindApps、ZLINK、DriveChat/SSHub；公开第三方SDK/API未核得 | 已公开摄像头与按键适配，不等于开放底盘控制 | 整机、线束/面框、拆装、可选服务及售后分别核价 | 比较具体车机，先核型号与安装 |
| [Apple Siri](https://support.apple.com/en-ie/guide/iphone/iph0aa8c80e6/27/ios/27)<br>[Apple](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)<br>现有手机助手 | 相容车辆Siri Eyes Free；Roadtrip官方另有调用Siri的旋钮步骤 | 调用手机任务，未因此取得通用车控；助手麦克风路由要验证 | 外设、手机适配与服务条件分别承担 | 首款可验证入口，限定语言与设备 |
| [Google Gemini](https://support.google.com/gemini/answer/14554984?hl=en)<br>[Google](https://play.google.com/store/apps/details?id=com.google.android.apps.bard&hl=en)<br>现有手机助手 | Google确认相容耳机及Android Auto入口；不能外推所有车载蓝牙套件 | 默认助手及任务权限有条件，不是车辆控制接口 | 官方软件、账号、联网及目标配件兼容另核 | Android候选入口，先验证车载外设 |

Apple对应Apple Inc.。Google Gemini和Android Auto的官方发行者为Google LLC；AAOS由Google主导AOSP、车厂/设备商集成，并非Google独家销售的统一成品。ATOTO官网披露品牌归属**Shenzhen Aotule Technology Co., Ltd.**，其全资子公司**HK Auto Smart Technology Co., Limited**获授权负责全球运营销售；本次未确认S84G209P具体型号的法定制造主体。[Apple商标清单](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)、[Gemini发行者](https://play.google.com/store/apps/details?id=com.google.android.apps.bard&hl=en)、[Android Auto发行者](https://play.google.com/store/apps/details?id=com.google.android.projection.gearhead&hl=en)、[AOSP项目说明](https://source.android.com/docs/setup/about)、[ATOTO公司说明](https://www.atotodirect.com/en-gb/pages/about-atoto)

<!-- platform-comparison-cards -->

### 平台与公司关系
Apple、Google提供的平台分属助手、手机互联、车内系统和服务层。ATOTO是具体后装设备：其Android 13/AICE UI 13不能直接认定为AAOS或已授权GAS。下图中虚线表示另需授权或集成。

```mermaid
%% title: 平台、具体产品与公司关系
%% 分析示意；实线表示提供、实现或投射，虚线表示授权或具体系统集成条件。
%% 来源 https://developer.apple.com/carplay/
%% 来源 https://source.android.com/docs/setup/about
%% 来源 https://source.android.com/docs/automotive/start/what_automotive
%% 来源 https://www.atotodirect.com/en-gb/pages/about-atoto
flowchart TB
  APPLE["Apple Inc."]
  GOOGLE["Google LLC<br/>主导 AOSP 项目"]
  AOTULE["Aotule 品牌方<br/>HK Auto Smart 全球运营销售"]
  subgraph PHONE["手机与相应服务"]
    SIRI["Apple Siri"]
    GEMINI["Google Gemini"]
    CP["Apple CarPlay"]
    AA["Google Android Auto"]
  end
  subgraph CAR["车内设备与系统"]
    SCREEN["相容投射接收设备<br/>逐品牌型号核对"]
    AAOS["Android Automotive OS<br/>由车厂或设备商具体集成"]
    ATOTO["ATOTO S8 Gen4 S84G209P<br/>具体 Android 替换车机"]
  end
  GAS["Google GAS<br/>授权应用与服务集合"]
  OEM["车厂 / 系统伙伴"]
  APPLE --> SIRI
  APPLE --> CP
  GOOGLE --> GEMINI
  GOOGLE --> AA
  GOOGLE --> AAOS
  GOOGLE --> GAS
  GAS -.->|"可选授权集成"| AAOS
  OEM -.-> AAOS
  CP -->|"投射交互"| SCREEN
  AA -->|"投射交互"| SCREEN
  AOTULE --> ATOTO
```

## （四）硬件载体与安装选择
| **载体** | **已研究例子** | **安装与前提** |
|---|---|---|
| 独立语音硬件 | Avantree CK11 / Roadtrip；LUMI交互终端 | 固定、供电；按任务核手机、软件与音频 |
| 独立屏 | Carpuride W903 | 支架、车充、手机与原车音频 |
| 替换车机 | ATOTO S84G209P | 双DIN拆换，面框/线束/ACC与原车功能适配 |
| 原车屏升级盒 | Ottocast P3 Pro / Carlinkit Tbox UHD | 先有相容原车有线投射接口，不能只靠USB口 |

载体是安装分类，不是统一平台。ATOTO手册提醒常电与ACC接错会影响休眠与启动；原车屏升级盒则须逐型号核原车协议及排除项。渠道应先记录车辆现有接口和保留功能，再匹配具体品牌型号。[ATOTO手册](https://www.atotodirect.com/en-gb/pages/manual-460-en)、[Carlinkit条件](https://www.carlinkit.com/uhd6225)、[W903官网](https://carpuride.com/products/carpuride-w903-portable-smart-multimedia-dashboard-console-with-front-camera)

```mermaid
%% title: 硬件载体与安装选型
%% 按车辆条件评估载体；具体型号仍需验证安装与兼容。
%% 来源 https://carpuride.com/products/carpuride-w903-portable-smart-multimedia-dashboard-console-with-front-camera
%% 来源 https://www.atotodirect.com/en-gb/pages/manual-460-en
%% 来源 https://www.carlinkit.com/uhd6225
flowchart TB
  START["比较手机与原车已有能力"] --> NEED{"需要新增什么体验"}
  NEED -->|"实体触发、语音或反馈"| VOICE["独立语音硬件 / 交互终端<br/>固定、供电与任务分工"]
  NEED -->|"持续可见的地图或状态"| SCREEN{"原车是否已有相容屏幕和协议"}
  SCREEN -->|"已有相容入口"| REUSE["先沿用原车屏与协议"]
  REUSE --> EXTRA{"仍需盒子提供的新增功能"}
  EXTRA -->|"是，且满足该盒使用条件"| BOX["比较原车屏升级盒<br/>核对协议、USB与固件"]
  EXTRA -->|"否"| VALIDATE
  SCREEN -->|"没有或不相容"| INSTALL{"是否接受拆换主机"}
  INSTALL -->|"保留原车机"| PORTABLE["独立接收屏<br/>支架、车充与音频路径"]
  INSTALL -->|"接受且车型可适配"| HEADUNIT["替换车机<br/>面框、线束、ACC、按键与原车功能"]
  VOICE --> VALIDATE["按实际车型和手机验证完整任务<br/>安装、重连、通话、播报与恢复"]
  BOX --> VALIDATE
  PORTABLE --> VALIDATE
  HEADUNIT --> VALIDATE
  VALIDATE --> DECIDE["增量收益与支持成本是否成立<br/>允许保留手机方案或当前阶段"]
```

## （五）音频播放与助手拾音
手机、外设和原车可能各有麦克风。按下设备按钮不证明Apple Siri或Google Gemini使用了外设麦克风；CK11官方排查要求手机靠近且手机麦克风无遮挡，是具体型号的反例。[CK11语音指南](https://support.avantree.com/hc/en-us/articles/50767188774937-How-to-Make-a-Call-by-Voice-Command)

| **链路** | **主要作用** | **还需核实** |
|---|---|---|
| HFP | 免提语音与电话相关控制 | 助手是否选用外设麦克风 |
| A2DP | 媒体音频播放 | 不提供反向录音保证 |
| AUX | 模拟声音送入原车音响 | 不读取原车麦克风 |
| FM | 将声音送入收音机 | 拾音、音源切换及频点干扰 |

上述职责依据[Bluetooth HFP简介](https://www.bluetooth.com/specifications/specs/hands-free-profile-1-10/)及[Android蓝牙配置](https://developer.android.com/develop/connectivity/bluetooth/profiles)。来电、音乐、导航和助手会改变音频焦点，应用录音也有权限与失焦停止条件。应在具体Apple/Google手机、固件和设备组合上验证完整任务与恢复。[Google车载麦克风](https://developer.android.com/training/cars/apps/library/car-microphone)

```mermaid
%% title: 音频与麦克风路径
%% 音频与拾音的可选路径，不代表全部链路可同时使用。
%% 虚线输入需系统选择、权限与实机核对；实线表示所选输出路径。
%% 来源 https://www.bluetooth.com/specifications/specs/hands-free-profile-1-10/
%% 来源 https://developer.android.com/develop/connectivity/bluetooth/profiles
%% 来源 https://developer.android.com/training/cars/apps/library/car-microphone
%% 来源 https://support.avantree.com/hc/en-us/articles/50767188774937-How-to-Make-a-Call-by-Voice-Command
%% 来源 https://carpuride.com/products/carpuride-w903-portable-smart-multimedia-dashboard-console-with-front-camera
flowchart LR
  subgraph INPUT["上行：请求音频从哪里来"]
    PHONE_MIC["手机麦克风"]
    DEVICE_MIC["外设或车机麦克风"]
    HFP["HFP免提语音链路<br/>须由相容设备和系统选择"]
    PROJECTION["投射或车内应用录音<br/>须权限和音频焦点"]
  end
  SESSION["当前助手 / App 音频会话<br/>确认实际输入和输出"]
  PHONE_MIC -.-> SESSION
  DEVICE_MIC -.-> HFP
  DEVICE_MIC -.-> PROJECTION
  HFP -.-> SESSION
  PROJECTION -.-> SESSION
  subgraph OUTPUT["下行：回复和媒体送往哪里"]
    OWN["设备自带扬声器"]
    BT["相容蓝牙接收端<br/>媒体可走A2DP，免提语音可走HFP"]
    AUX["AUX输出接原车输入"]
    FM["FM发射接原车收音机"]
    CAR["原车音响<br/>需正确音源与音量"]
    BT --> CAR
    AUX --> CAR
    FM --> CAR
  end
  SESSION --> OWN
  SESSION --> BT
  SESSION --> AUX
  SESSION --> FM
```

<a id="platform-choice"></a>

## （六）选定方案前的准入条件
软件分发、硬件接收与车辆权限分别核对。CarPlay接收硬件涉及相应MFi要求，标准蓝牙配件按所用技术判断；ATOTO的厂商应用入口不等于向第三方开放SDK。AAOS的VHAL与系统特权由具体实现及授权决定，Android Auto部分车况API也受权限和车型限制。[MFi FAQ](https://mfi.apple.com/en/faqs)、[ATOTO手册](https://www.atotodirect.com/en-gb/pages/manual-460-en)、[VHAL](https://source.android.com/docs/automotive/vhal)、[车况API](https://developer.android.com/training/cars/apps/library/car-hardware-api)

采用Siri或Gemini时，需先确认目标语言、任务和外设入口。Roadtrip、CK11的旧Google Assistant说明不能直接当作Gemini兼容证明；界面支持波兰语，也不能据此推定Siri支持波兰语任务。CarPlay Ultra属于车厂深度集成，普通CarPlay与后装屏不沿用其车控能力。[Roadtrip助手说明](https://support.avantree.com/hc/en-us/articles/38121800304793-Roadtrip-How-to-activate-the-voice-assistant-with-the-car-kit-Siri-Google-Assistant)、[Apple功能清单](https://www.apple.com/ios/feature-availability/)、[CarPlay Ultra说明](https://www.apple.com/newsroom/2025/05/carplay-ultra-the-next-generation-of-carplay-begins-rolling-out-today/)

确定具体手机、设备与任务后，再按第四章验证完整使用过程和失败恢复。

# 三、按阶段竞品比较
<!-- lumi-reference:start -->

## （一）LUMI：实体交互与手机协作参照
LUMI（璐觅）车载/桌面机器人提供实体交互参照：设备呈现表情、动作和语音交互，手机软件及服务承担部分工作。表情小屏与显示地图的智能面板用途不同。

| **层次** | **已取得的证据** | **保留未知** |
|---|---|---|
| 相关手机软件 | Lumi Android App；深圳云衍开发/运营 | 整机SKU与制造主体 |
| 手机协作 | 教程描述App绑定、后台聊天与媒体蓝牙 | 实际拾音与兼容范围 |
| 外部服务 | 政策披露第三方模型及输入共享 | 当前链路与完整离线能力 |
| CarPlay关系 | 未取得原生支持的正式说明 | 是否适配及并用表现 |

对应Android应用包名为`com.example.lumi_client`，小米商店列开发者为**深圳市云衍智能科技有限公司**；页面“维护中”不能直接推定硬件停产或服务停运。其隐私政策自述该公司运营Lumi App，披露蓝牙绑定智能硬件及豆包、DeepSeek等外部模型服务。政策是功能与处理声明，不能当作特定整机当前实现的实测证据。[Lumi应用资料](https://app.mi.com/details?id=com.example.lumi_client)、[Lumi隐私政策](https://yyzc.yylumi.com/privacy.html)

```mermaid
%% title: LUMI参照中的设备、手机与可选原车音频
%% 基于教程转写及政策声明的研究示意，虚线不代表实测链路。
%% 来源 https://app.mi.com/details?id=com.example.lumi_client
%% 来源 https://yyzc.yylumi.com/privacy.html
%% 来源 https://www.douyin.com/video/7629608396925350134
flowchart TB
  DEVICE["LUMI实体设备<br/>表情、动作与语音交互参照"]
  PHONE["手机上的Lumi App<br/>绑定、配置及教程中的聊天协作"]
  SERVICE["外部模型服务<br/>政策声明，具体链路待核"]
  CAR["原车音响，可选输出<br/>教程描述手机蓝牙连接车机"]
  DEVICE -.->|"蓝牙绑定，拾音路由待核"| PHONE
  PHONE -.->|"按所需服务与网络条件"| SERVICE
  PHONE -.->|"媒体蓝牙，非CarPlay证明"| CAR
```

<details class="cp-terms"><summary>教程说明了什么，哪些还不能下结论？</summary>
<p>公开安装教程的AI转写描述App绑定机器人、另连媒体蓝牙、AI对话触发App页面，以及手机熄屏/后台后继续；原车音响教程描述手机再连接车机蓝牙。它们支持“实体设备、手机协作和原车音频分开处理”的解释，不等于已亲看完整视频或实车测试。</p>
<p>教程提到关闭App蓝牙后可触发“跳舞”，须限定到该动作及其前置设置；这不等于手机关机、所有连接或互联网断开，更不能证明完整离线聊天或本地大模型。教程日期不稳定，上市日期待核。</p>
<p>原视频：<a href="https://www.douyin.com/video/7629608396925350134">安装使用教程</a>、<a href="https://www.douyin.com/video/7643012811606182563">原车音响教程</a>；读取依据为其<a href="https://www.douyin.com/shipin/7630288336766191616">聚合页作者内容转写</a>。iOS同名“Lumi – AI Car Companion”由ZIGZAG TECHNOLOGY LIMITED发行，与该整机及Android主体的关系未确认，不能合并规格与服务。整机当前价格和供给、芯片与本地模型、CarPlay原生支持及蓝牙/CarPlay并用仍待核。</p>
</details>

**可借鉴的是实体交互与软件服务的组合。** 项目若采用类似路径，需要落实配套软件的供应、开发和维护，再单独评估CarPlay或导航集成。

<!-- lumi-reference:end -->

## （二）首期直接竞品与历史经验
价格及销售状态核对日为2026年11月5日，LUMI证据另核于11月6日。下表为对应地区的商品页线索或历史公告；尚未下单确认交付，波兰含税、运费与售后报价需另询。

| **产品与阶段** | **能力和依赖** | **价格及状态** | **对产品判断的价值** |
|---|---|---|---|
| Avantree CK11，小型免提音箱 | 遮阳板夹装、自带扬声器、手机蓝牙和手机助手 | 2026-11-05，titanium US$44.99，标In Stock | 是免拆首款的直接参照。官方指南明确语音命令使用手机麦克风，不能据设备有麦克风宣传已改善助手拾音。[CK11 商品页](https://avantree.com/products/ck11-hands-free-bluetooth-for-car)、[CK11 指南](https://avantree.com/pages/ck11-interactive-user-guide) |
| Avantree Roadtrip，小音箱与 FM | 自带扬声器，支持将手机音频送入收音机，长按旋钮两秒调用手机助手 | 2026-11-05，US$64.99，标In Stock | 通过安装、音频和操作入口形成价值。助手说明仍要求手机助手启用、蓝牙和网络条件。[Roadtrip 商品页](https://avantree.com/products/roadtrip-handsfree-bluetooth-speaker-for-cars)、[助手激活说明](https://support.avantree.com/hc/en-us/articles/38121800304793-Roadtrip-How-to-activate-the-voice-assistant-with-the-car-kit-Siri-Google-Assistant) |
| Echo Auto 第 2 代，历史语音入口 | 专用拾音和固定配件，经手机 Alexa App 接入服务与车内音响 | 2022年美国发布价 US$54.99。2026-11-05美国购买框显示暂不可购，现价未取得 | 展示手机加专用外设的路径。历史价格、支持页保留和当日服务可用是三件事。[Amazon 发布公告](https://press.aboutamazon.com/2022/9/amazon-introduces-four-new-echo-devices-plus-upgrades-to-echo-studio-audio)、[美国商品页](https://www.amazon.com/dp/B09X27YPS1) |
| Garmin Speak Plus，历史组合产品 | 手机数据连接 Alexa，同时加入行车记录和风险提示 | 2018年公告建议零售价 US$229.99，当前供货未核 | 可观察语音与摄像任务的组合，其功能不证明可转向、制动或已经形成成功业务。[Garmin 发布公告](https://www.garmin.com/en-US/newsroom/press-release/automotive/2018-the-new-garmin-speak-plus-with-amazon-alexa-brings-amazon-alexa-to-a-vehicle-and-adds-a-built-in-dash-cam/) |

这些产品展示了手机助手外设、独立交互终端及配套服务等不同路径，未证明新进入者有足够需求。比较时应把手机直接使用、普通免提设备、独立交互终端和成熟投射平台一并纳入，考察从上车到完成任务的全过程。Roav VIVA、JBL Smartbase 等历史型号可用于补充形态和服务依赖，不能以历史发布信息代替当前采购证据。

## （三）面板、驾驶辅助与模型参照
第二阶段可比较 Carpuride W903 这类独立投射屏、ATOTO S8 Gen4 这类替换车机，以及 Ottocast、Carlinkit 原车屏升级盒。W903默认SKU于2026-11-05官网标US$219.99，主要说明固定屏与记录任务的组合。升级盒通常先要求相容有线手机互联接口，完全无屏的旧车无法直接套用这一入口。[W903 商品页](https://carpuride.com/products/carpuride-w903-portable-smart-multimedia-dashboard-console-with-front-camera)、[Carlinkit UHD 产品条件](https://www.carlinkit.com/uhd6225)

ATOTO 官方手册明确 DriveChat 处理命令和回答需要联网，不能因其运行 Android 就写成完整离线语音。由此可见，第二阶段的关键问题仍是任务和系统整合，不必先建设本地大模型。[ATOTO S8 Gen4 手册](https://www.atotodirect.com/en-gb/pages/manual-460-en)

第三阶段的参考应拆为 Garmin Dash Cam 等记录预警设备、Mobileye 历史后装预警系统，以及 comma 的车型适配运动辅助。Cerence 等企业语音或模型方案属于后续集成参考，开发板、PC 演示和预告产品另列，不能与现售小音箱混成同一采购价格榜。

# 四、首款小型语音助手功能与工程
## （一）先限制任务，再补全使用过程
候选任务可包含设备交互、语音服务、媒体，以及按支持接口转交导航或通话；先选少量高频任务。导航、通话与媒体是一组参照，不预设首款必须覆盖。Google官方分别提供Android Auto中的导航、通话和媒体路径，构成现成能力基线。若选择借用Apple Siri、Google Gemini或厂商助手，再分别核对其支持条件，不能由语音按钮推定取得同样权限。[Google 导航](https://support.google.com/androidauto/answer/6348322?hl=en)、[电话](https://support.google.com/androidauto/answer/6348066?hl=en)、[媒体](https://support.google.com/androidauto/answer/6348327?hl=en)

以“去公司”为例，首次停车配置时选择地图应用并保存地点，完成一次实际导航。日常上车后，设备恢复供电和连接，用户按键得到短提示，说出指令，系统确认必要参数并交给导航。若无法取得最终状态，只能提示请求已转交，不能把识别成功或应用打开称为导航完成。拨号则核对联系人与号码、音频和挂断后的恢复，媒体任务核对目标应用及实际播放状态。

以下为拟议任务闭环，提示和状态反馈以所选设备、应用、服务及接口实际可取得的能力为限。

```mermaid
%% title: 从上车到任务结果的完整闭环
flowchart TD
  A[上车 设备供电与重连] --> B{连接与必要配置可用}
  B -->|否| X[说明不可用 保留基础操作]
  X --> Y[停车后按提示修复配置]
  Y --> B
  B -->|是| C[按键触发与短反馈]
  C --> D[所选语音组件处理]
  D --> E{参数明确且已授权}
  E -->|否| F[确认参数 或说明缺少权限]
  F -->|确认或补充后重验| E
  F -->|缺少权限| X
  F -->|取消或超时| Z[退出并恢复音频]
  E -->|是| G[设备功能或支持的应用与服务执行]
  G --> H{能否确认实际结果}
  H -->|能| I[反馈完成或明确失败]
  H -->|不能| J[说明已转交与状态边界]
  I --> Z
  J --> Z
```

首期可采用按键、明确唤醒方式和有限任务，识别与执行按所选方案分工；本机、手机或在线处理均需核对语言、权限、音频和失败回退。新增配套软件需开发、采购授权方案或合作，不视为项目已具备。长对话、长期记忆、多乘员识别和通用车控应按增量价值另行评估。

## （二）把工程职责分到实际可控的环节
| **环节** | **需要负责的结果** | **不能默认取得的条件** |
|---|---|---|
| 外设与固件 | 固定、供电、按钮、音量、静音、连接和可理解反馈 | 外设麦克风会被手机助手使用，系统助手支持任意按钮映射 |
| 任务与服务集成 | 权限配置、账号、应用转交、后台和锁屏恢复、状态观测 | 第三方应用具有系统助手全部能力，所有手机保持同一行为 |
| 语音或云组件 | 实际支持的语言、接口可用性、超时和费用、版本维护 | 服务一直在线，断网仍完成同一任务，供应商替产品承担任务结果 |
| 供应与支持 | 型号批次、固件、说明、故障复现、换修和升级 | 同名称商品的充电口、配件和行为始终相同 |

## （三）按失败原因验证完整任务
以下是建议的验证方法，尚未执行。先限定手机、系统、外设、固件、应用和原车音源组合，以手机直接使用为基线。随后按停车准备、日常上车、触发执行和中断恢复重复同一任务，记录噪声、位置、网络及是否需要看手机。

```mermaid
%% title: 任务验证与改进闭环
flowchart TB
  A[固定组合与任务] --> B[比较手机直接使用]
  B --> C[记录完整成功与失败]
  C --> D[定位连接 拾音 权限或执行原因]
  D --> E[修正方案或缩小支持范围]
  E --> F[在原条件复测并检查恢复]
  F --> A
```

重点加入来电抢占、断网、未登录、重名联系人、重复按键和超时场景，检查会否误执行以及怎样取消。网络恢复后也要避免重复发起过期任务。对既有助手无法观测或改变的环节，记录边界并调整产品承诺。

可分别统计完整任务完成、连接可用、人工重试、错误执行和恢复结果。完整任务完成率以预先约定的全部尝试为分母，包含连接失败，另列可用状态下的执行结果，避免只展示识别成功率。样本和验收阈值由实际产品目标确定，现阶段没有识别率、续航或工期的项目实测结论。

# 五、商业、渠道与经营可行性
## （一）市场量级与销售边界
<!-- market-summary:start -->
以下为截至2026年11月5日可核实的统计基数。使用同口径EU27乘用车做量级演算，不以汽车存量直接推导需求、年度销量或收入。

| **指标** | **数量** | **统计口径** |
|---|---:|---|
| 欧盟乘用车 | 2.56亿辆 | 2024，EU27 |
| 汽油＋柴油 | 87.6%，约2.24亿辆 | 混动另列，占比推算 |
| 平均车龄 | 12.7年 | ACEA口径，车龄表保加利亚缺报 |

依据：[ACEA 2026报告](https://www.acea.auto/files/ACEA_Report-%E2%80%93-Vehicles_on_European_roads_2026.pdf)，2026年1月发布，实际统计2024年，第5、11、15页。乘用车精确量255,999,373辆；汽油49.2%＋柴油38.4%，推算约2.24亿辆，因占比四舍五入，结果用约数。不能以非纯电比例、车龄或新车联网装配率替代无便捷入口的既有车队占比。

市场量级按条件缩小：缺口量＝汽柴油基数×目标任务缺口比例；技术可服务量＝缺口量×手机与任务适配率；年度购买量＝可服务量×年度购买率。这三个比例均未知，后两者是前一筛选人群中的条件比例，不需要假定独立。网页默认10%/50%/1%是演示输入，得到约1,121万车辆可服务、11.2万台/年购买情景，不是调查结论、基准预测或本项目销量。实际适配需涵盖手机、语言、音频与任务；购买还需价格与试售验证。

波兰仅为渠道案例：2025年CEP更新记录口径乘用车21,161,500辆，排除archived，平均车龄15.3年；不等于每辆都在日常上路，也不是2,116万台可售市场。[PZPM 2025存量表](https://www1.pzpm.org.pl/pl/layout/set/print/content/download/2590/10563/file/Park_2025.pdf)、[PZPM 2026/27年鉴第25页](https://www1.pzpm.org.pl/pl/content/download/11094/68148/file/Raport_2026_caly_lekki.pdf#page=25) 波兰已包含于EU，不与EU相加。

渠道年销量＝有效门店数×每店每月独立合格客户数×成交率×12。需取得去重、实际可销售和已适配的合格客户数；门店、展示、转化数据尚未取得。20店×30合格客户/月×5%×12＝360台/年只是演示，不是对合作伙伴能力的估计。实际净销量、退货、供货及现金需求再核。

中国作为范围背景：2025年末民用轿车19773万辆。该分类与EU乘用车不同，且未取得同口径燃油或互联缺口细分，不合并为全球可售市场。[国家统计局2025公报](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html)，2026-02-28发布；实际读取汽车保有量段落。全部参数与来源保存在 [评分与市场数据](<车载智能化 评分与市场.json>)。
<!-- market-summary:end -->


## （二）先明确卖什么，以及谁承担承诺
可比较硬件套餐、软件或集成授权、可选持续服务三种方式。硬件套餐交付设备和已验证任务，软件授权交付受约定接口与版本支持的能力，持续服务则需说明服务内容和期限。首期依赖手机已有助手可以减少建设范围，但外设本身无法保证手机账号、第三方内容和网络长期不变。Roadtrip 的官方助手说明就把手机配置、蓝牙和网络作为前提。[Roadtrip 助手说明](https://support.avantree.com/hc/en-us/articles/38121800304793-Roadtrip-How-to-activate-the-voice-assistant-with-the-car-kit-Siri-Google-Assistant)

以下是拟议的责任划分，具体承担方及费用需供应、授权和渠道合同确认，未取得已成交的分成条件。

| **参与者** | **交付或取得的价值** | **需要落实的成本与责任** |
|---|---|---|
| 设备制造或 ODM 方 | 硬件、固件、配件和供货 | 批次一致性、质量、固件升级、备件及换修，软件接口是否开放 |
| 产品或软件方 | 任务体验、适配、品牌和版本支持 | 手机测试、账号与数据安排、服务监测、问题定位、停服或变更处置 |
| 电商或汽配渠道 | 获客、展示、选型和销售 | 宣传准确性、佣金或进销差价、退换入口、客服及结算，避免超出支持范围销售 |
| 安装或配置服务方 | 固定、配对、音频选择和现场演示 | 服务收费、配置失败、重复上门、原车功能问题和记录留存 |
| 外部服务提供方 | 地图、媒体、识别或云能力 | 商用许可、按量或周期费用、账号和地区条件、更新及退出机制 |

收入分配要和工作对应。门店仅交货，或同时承担配置、演示与一线售后，所需资源不同。软件授权也要明确按设备、用户、项目还是期间收费。未取得条款前，不预设渠道比例、持续订阅或交易佣金成立。

## （三）把用户配置和支持连成可交付流程
售前先识别手机、原车音频和用户任务。首次配置尽量在停车状态完成：固定供电、配对、选择音源、启用所需权限，再演示一次真实任务和取消。交付记录保留准确型号、固件、手机和服务版本，便于后续定位。CK11 官方指南列出配对、安装、重连和助手设置，这些步骤会形成支持工作，不能因产品免拆而省略。[CK11 交互指南](https://avantree.com/pages/ck11-interactive-user-guide)

```mermaid
%% title: 配置、交付与支持责任链
flowchart TD
  A[售前核对手机 原车接口与任务] --> B[渠道或用户按指南配置]
  B --> C[完成一次真实任务与取消演示]
  C --> D[交付兼容条件与支持入口]
  D --> E{日常是否遇到问题}
  E -->|否| F[记录复用与实际价值]
  E -->|是| G[一线支持按设备与版本复现]
  G --> H{定位责任环节}
  H -->|硬件或固件| I[供应方换修或修复]
  H -->|配置或平台软件| J[渠道或软件方处理]
  H -->|外部服务| K[核实账号 接口或服务变化]
  I --> L[复测并反馈给用户]
  J --> L
  K --> L
  L --> F
```

售后应区分损坏、接口不兼容、手机设置、网络和第三方服务问题，明确用户先找谁、如何升级处理。故障频繁的组合可缩小销售范围或暂缓推荐，不能仅靠增加客服解释维持过宽的兼容承诺。

## （四）统一口径计算贡献和阶段投入
硬件套餐可用下式整理单机贡献，所有变量采用同币种、同税务与服务期间。该式是经营分析框架，不含虚构报价。

$$C=P_{\mathrm{net}}-C_{\mathrm{device}}-C_{\mathrm{delivery}}-C_{\mathrm{support}}-C_{\mathrm{service}}$$

$P_{\mathrm{net}}$ 为扣税、渠道扣点和促销后实际到账净收入，预测也沿用这一口径。各成本为设备、交付、退换支持及对应期间的服务费用，渠道扣点不重复扣除。退款若已冲减收入，也避免再次作为损失扣减。云费用和预期支持成本使用相同服务期，不能用一次硬件收入覆盖未经估算的无限期承诺。

固定研发、模具、认证、人员和验证投入另算，库存、账期、备货及回款再决定现金需求。轻量外设先核供货和手机适配，面板增加显示、安装及固件维护，记录预警增加摄像与感知评测，运动辅助增加车型接口及安全体系。前期正贡献只能支持当前经营判断，不能自动覆盖后续投入。

区域渠道应取得真实客群、接口分布、交付和售后能力、采购与结算资料。波兰仅为待核案例，语言、当地服务和含税交付另行确认。硬件售出、激活、复用、付费和退货分别记录，再判断应扩大渠道、改善产品还是停止某种组合。

# 六、辅助驾驶和后续大模型演进
## （一）记录预警先形成自己的产品目标
记录、事件回看和风险提示可以成为独立业务。Garmin Dash Cam X110 手册列出记录、保存及驾驶提醒，也明确提示受安装、视野和工作条件影响，驾驶员仍负责驾驶。Mobileye 8 Connect 则提供专用摄像与预警参照，其说明同样不能用来宣称替代驾驶员控制。[Garmin X110 手册](https://www8.garmin.com/manuals/webhelp/GUID-93747543-12A8-453C-9896-32070F5B0710/EN-US/Dash_Cam_X110_OM_EN-US.pdf)、[Mobileye 8 Connect 手册](https://static.mobileye.com/manual/me8/Mobileye%208%20connect%20%E2%80%93%20User%20manual.pdf)

这一阶段新增摄像头位置与标定、视频存储、感知、提醒策略和误报漏报评测。自有面板可以复用部分显示与电源，但新摄像头仍需重新验证。夜间、逆光、遮挡和天气变化应进入计划，记录的连续性与提示的准确性分别评估。停车看护、远程查看和云存储按供电、网络及服务条件另列，不能把基础录像能力扩大为全部功能离线可用。

商业需求也要重算。Mobileye 于2024年宣布收缩后装解决方案业务，解释原厂 ADAS 普及压缩后装机会，且该业务近年未对盈利作正贡献，同时保留商用车原厂相关业务。这一反例要求按具体客群评估替代和付费，并不证明所有后装提示产品都没有机会。[Mobileye 后装业务公告](https://ir.mobileye.com/news-releases/news-release-details/mobileye-wind-down-aftermarket-solutions-unit)

## （二）运动辅助需要单独的系统与合作条件
涉及转向、加减速或制动时，产品进入不同工程范围。comma 官方支持表按车型、年份、配置和线束限定，安全文档要求驾驶员关注、可接管，并说明限幅与测试。这些约束说明，车辆运动辅助需要具体接口和功能边界，无法从“传统燃油车”或“新能源车”这一动力标签判断支持。[comma 车辆支持](https://docs.comma.ai/CARS/)、[comma 安全说明](https://docs.comma.ai/concepts/safety/)

下图为能力分工分析，三类系统各自处理不同任务。语音结果通过授权工具执行座舱任务，不能直接等同车辆运动决策。

```mermaid
%% title: 座舱、预警与运动辅助的能力边界
flowchart TD
  A[已有任务 用户与渠道经验] --> B[记录与预警产品]
  B --> B1[摄像 标定 存储与感知评测]
  B --> B2[音画提示与使用边界]
  A -.-> C[运动辅助独立立项]
  C --> C1[车型接口 感知 实时控制]
  C --> C2[驾驶员接管 安全验证与持续支持]
  A --> D[按任务评估模型升级]
  D --> D1[知识问答 自然表达或任务组合]
  D1 --> E[参数检查与授权工具]
  E --> F[允许的座舱任务]
```

自有团队可负责需求、用户界面、设备管理和支持，传感、控制、车型接入或验证可与专业伙伴分工。合作前需确认适配权利、修改与升级边界、故障处置、验证证据和持续支持。座舱用户及对话可帮助发现需求，经授权的同步道路数据、控制专业团队和安全资源仍需另行取得。

## （三）后续模型按具体增量选择部署位置
适合比较的增量包括更自然的表达、许可车主资料问答、受限任务组合和多模态理解。先与规则或现成助手完成同一任务比较，再考虑云 API、手机模型、车内模型或混合。若选择车内推理，才继续核算算力、内存、热管理、启动、语音链路、许可和更新。辅助驾驶本身可能已有感知模型，和引入通用 LLM 是两个问题。

Cerence CaLLM Edge 的原始公告可作为企业嵌入式模型集成参考，其模型与部署能力不等于可直接采购的后装整机。具体硬件、软件授权、移植、工具接口和支持条件都应另核。[Cerence 嵌入式模型公告](https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive)

模型引入后，确认、取消、超时和权限规则仍然有效。知识回答允许说明不确定，实际动作需验证参数与权限。模型演示、开发板可运行和客户计划装车分别标注成熟度，不能据此承诺量产、全离线或车辆控制。第四阶段作为后续选择保留，但无需等待完成运动辅助后才研究其有用任务。

# 七、参考资料

以下资料按主题归类，同一来源合并列示。除另注外，访问日为2026年11月5日；11月6日核查的资料在表内标明。未标发布日期的滚动页面不以访问日代替发布日期。阅读深度为针对性阅读，具体范围见各条记录；未进行采购、账号激活、SDK运行或实车验证。商品页用于确认厂商声明与当日销售线索，不构成独立性能或业务效果验证。

逐项产品记录见 [车载智能化 产品样本](<车载智能化 产品样本.json>)，评分原始分与市场参数见 [评分与市场数据](<车载智能化 评分与市场.json>)，各来源的阅读范围与限制列于下表。

## （一）平台与接入

| **责任方与资料** | **版本、日期** | **实际阅读范围与边界** |
|---|---|---|
| Apple：[CarPlay产品介绍](https://www.apple.com/ios/carplay/)、[开发入口](https://developer.apple.com/carplay/)、[使用说明](https://support.apple.com/en-us/108415) | 滚动页；产品介绍访问2026-11-06 | 产品分工、应用类别与entitlement入口、设置及Siri触发方式。既有CarPlay能力不证明新增蓝牙配件可并用 |
| Apple：[CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf) | 2026-10-13；2026-11-06复核 | 已保存官方PDF及提取文本，针对性阅读类别、授权、模板、分发与导航章节，重点包括印刷第8、13–15、27、30、67页。非全文研读；应用授权与接收硬件资格分别核对 |
| Apple：[Rev up your CarPlay app / WWDC26讲稿](https://developer.apple.com/videos/play/wwdc2026/212/) | WWDC26、iOS27；2026-11-06复核 | 约6:22–8:17的Voice Control、URL任务及音频会话，并查看导航面板相关讲稿；未观看完整视频。模板扩展不等于任意后台或车辆权限 |
| Apple：[Displaying Content in CarPlay](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay) | 滚动文档；访问2026-11-06 | 文档索引内容与官方指南相互参照，确认地图窗口和模板分工；未运行SDK，不将索引阅读记作DocC全文阅读 |
| Apple：[MFi FAQ](https://mfi.apple.com/en/faqs) | 滚动页 | MFi技术范围、标准蓝牙例外、开发/ODM/品牌/销售角色。未取得保密规格、项目资格或完整商业费用 |
| Apple：[CarPlay Ultra发布公告](https://www.apple.com/newsroom/2025/05/carplay-ultra-the-next-generation-of-carplay-begins-rolling-out-today/) | 2025-05-15 | 原厂深度集成、首发及系统条件；不以历史扩展计划推定2026年各市场已交付，也不把Ultra车控能力赋给普通CarPlay |
| Apple：[车内Siri指南](https://support.apple.com/en-ie/guide/iphone/iph0aa8c80e6/27/ios/27)、[功能可用性](https://www.apple.com/ios/feature-availability/) | iOS27指南及iOS/iPadOS27功能页 | 车内入口、CarPlay地区、Siri语言、离线请求和系统语言分别核验；界面语言不证明语音任务可用 |
| Apple：[会员详情](https://developer.apple.com/programs/whats-included/)、[商标清单](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) | 滚动页 | US$99/会员年的公开费用及Siri、CarPlay与Apple Inc.关系；会员费不等于接收端许可费，公司归属不替代地区服务合同 |
| Google：[Android Auto开发概览](https://developer.android.com/training/cars/platforms/android-auto)、[Android车载类别](https://developer.android.com/training/cars)、[用户入门](https://support.google.com/androidauto/answer/6348019?hl=en) | 开发概览及类别页更新2026-10-22；帮助页滚动 | 手机执行、支持类别、声明、质量、可信分发及有线/无线条件。未列通用对话类别不等于禁止全部语音输入；官方页面最低系统表述有差异，未合并为统一门槛 |
| Google：[Android Auto导航](https://support.google.com/androidauto/answer/6348322?hl=en)、[电话](https://support.google.com/androidauto/answer/6348066?hl=en)、[媒体](https://support.google.com/androidauto/answer/6348327?hl=en) | 滚动帮助页 | 现成任务、操作与依赖；不证明新增外设取得相同入口或权限 |
| Google/AOSP：[平台定义](https://source.android.com/docs/automotive/start/what_automotive)、[AAOS应用概览](https://developer.android.com/training/cars/platforms/automotive-os)、[AOSP项目说明](https://source.android.com/docs/setup/about)、[GAS说明](https://developers.google.com/cars) | 平台定义更新2026-09-30；应用概览更新2026-10-22；其余滚动 | Android Auto、AAOS、GAS/Google built-in的关系，Google主导开源项目与设备商集成的分工；AAOS不默认包含GAS，也不是统一零售车机 |
| Google/AOSP：[AAOS助手集成](https://source.android.com/docs/automotive/voice/voice_interaction_guide/integration_flows)、[VHAL定义](https://source.android.com/docs/automotive/vhal) | 均更新2026-09-24 | 触发、系统特权、预装更新，以及车厂车辆属性的读写/订阅抽象；具体权限仍取决于系统与车辆实现 |
| Google：[Car Hardware API](https://developer.android.com/training/cars/apps/library/car-hardware-api) | 更新2026-09-08 | CarInfo权限、数据可用性与车型依赖；部分信息读取不等于通用车辆控制 |
| Google：[导航应用开发](https://developer.android.com/training/cars/apps/navigation)、[地图绘制](https://developer.android.com/training/cars/apps/library/draw-maps) | 导航页更新2026-09-08；地图页更新2026-03-05；访问2026-11-06 | 导航类别与模板、Surface绘制、可见区域及行程信息。应用提供地图内容，主机管理界面和交互，不据此推定外部设备能控制地图 |
| Google：[built-in离线说明](https://support.google.com/built-in/answer/11013995?hl=en)、[车内通话](https://support.google.com/built-in/answer/9927598?hl=en) | 滚动帮助页 | Assistant部分任务、预下载地图与联网条件，以及通话所需手机蓝牙配对；不外推为全部Gemini会话离线可用 |
| Google：[Gemini移动助手入门](https://support.google.com/gemini/answer/14554984?hl=en)、[手机任务与限制](https://support.google.com/gemini/answer/14579631?hl=en) | 滚动帮助页 | 移动助手定位、设置、锁屏、语言及旧助手差异；不保证任意手机或应用具有相同功能 |
| Google：[Gemini相容耳机](https://support.google.com/gemini/answer/15456140?hl=en)、[Gemini车内帮助](https://support.google.com/gemini/answer/16735982?hl=en) | 滚动帮助页 | 相容设备、触发及Android Auto条件；相容耳机或方向盘入口不能证明通用车载蓝牙按钮兼容 |
| Google：[Gemini发行页](https://play.google.com/store/apps/details?id=com.google.android.apps.bard&hl=en)、[Android Auto发行页](https://play.google.com/store/apps/details?id=com.google.android.projection.gearhead&hl=en)、[Play开发者注册](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en) | 滚动商店/帮助页 | 产品身份与Google LLC发行者、US$25一次性发布账号注册费；商店旧描述不用于确定当前最低系统，注册费不替代GAS或硬件许可 |

## （二）音频与移动接口

| **责任方与资料** | **版本、日期** | **实际阅读范围与边界** |
|---|---|---|
| Bluetooth SIG：[HFP简介](https://www.bluetooth.com/specifications/specs/hands-free-profile-1-10/)，Google：[Android蓝牙配置](https://developer.android.com/develop/connectivity/bluetooth/profiles) | HFP 1.10，Adopted；Android页更新2026-10-23 | 阅读HFP规范简介及Headset/HFP、A2DP职责；未研读完整协议或验证产品合规。音频连通不保证助手采用外设麦克风 |
| Google：[车载麦克风](https://developer.android.com/training/cars/apps/library/car-microphone) | 更新2026-09-08 | 录音许可、音频焦点与失焦停止条件；录音API不是任意外部麦克风的路由选择接口 |
| Apple：[App Intents](https://developer.apple.com/documentation/appintents) | 滚动框架文档 | 官方Markdown的Overview与系统集成说明；系统可发现应用动作，不等于任意跨App或车辆控制权 |
| Google：[运行时权限](https://developer.android.com/training/permissions/requesting)、[后台限制](https://developer.android.com/develop/background-work/background-tasks/bg-work-restrictions)、[跨App任务接口](https://developer.android.com/guide/components/intents-common) | 权限与Intent文档滚动；后台页更新2026-10-21 | 沙箱、授权与拒绝后回退，系统/用户后台限制及隐式Intent；未运行示例。发出请求不证明目标任务完成，第三方应用也不保证常驻 |

## （三）具体产品与LUMI参照

| **责任方与资料** | **版本、日期** | **实际阅读范围与边界** |
|---|---|---|
| Avantree：[CK11商品页](https://avantree.com/products/ck11-hands-free-bluetooth-for-car)、[交互指南](https://avantree.com/pages/ck11-interactive-user-guide)、[语音拨号说明](https://support.avantree.com/hc/en-us/articles/50767188774937-How-to-Make-a-Call-by-Voice-Command) | 商品页滚动；指南更新2026-10-30；拨号说明更新2026-10-05 | 具体SKU、价格与库存、安装重连、助手设置和手机麦克风排查；不能由设备有通话麦克风推断助手拾音来源 |
| Avantree：[Roadtrip商品页](https://avantree.com/products/roadtrip-handsfree-bluetooth-speaker-for-cars)、[助手激活](https://support.avantree.com/hc/en-us/articles/38121800304793-Roadtrip-How-to-activate-the-voice-assistant-with-the-car-kit-Siri-Google-Assistant) | 商品页滚动；支持页更新2026-09-03 | 当前价与库存、音箱/FM、旋钮及手机前提；续航描述存在差异，不采用统一续航承诺；Google Assistant说明不自动证明Gemini兼容 |
| Amazon：[Echo Auto第2代发布](https://press.aboutamazon.com/2022/9/amazon-introduces-four-new-echo-devices-plus-upgrades-to-echo-studio-audio)、[美国购买页](https://www.amazon.com/dp/B09X27YPS1) | 公告2022-09-28；购买页滚动 | 历史形态、手机依赖、发布价与当日购买框；未验证账号激活或当日全部服务 |
| Garmin：[Speak Plus发布](https://www.garmin.com/en-US/newsroom/press-release/automotive/2018-the-new-garmin-speak-plus-with-amazon-alexa-brings-amazon-alexa-to-a-vehicle-and-adds-a-built-in-dash-cam/) | 2018-01-08 | 语音、摄像和预警组合及历史价格；当前供货与业务成效未知，不据此推断运动控制能力 |
| Carpuride：[W903商品页](https://carpuride.com/products/carpuride-w903-portable-smart-multimedia-dashboard-console-with-front-camera) | 滚动商品页 | 默认SKU、价格、供电、音频、手机投射、相机与后摄布线；未证实可安装任意第三方助手 |
| ATOTO：[S84G209P商品页](https://www.atotodirect.com/de-us/products/atoto-s84g209p-9inch-double-din-car-stereo-eu)、[S8 Gen4手册](https://www.atotodirect.com/en-gb/pages/manual-460-en)、[公司说明](https://www.atotodirect.com/en-gb/pages/about-atoto)、[联系主体](https://www.atotodirect.com/en-gb/pages/contact) | 滚动页面；手册对应S84G209P | 双DIN安装、常电/ACC、休眠、方向盘适配、DriveChat联网与厂商软件；核查Aotule品牌归属和HK Auto Smart运营销售关系，未确认具体型号铭牌制造商，不混用地区配置 |
| Carlinkit：[Tbox UHD产品条件](https://www.carlinkit.com/uhd6225)、[商城条件](https://carlinkitmall.com/collections/wireless-carplay-adapter/products/carlinkit-tbox-uhd-android-13-carplay-ai-box-with-hdmi-output) | 滚动页面 | 原厂有线协议、USB与车型排除项；仅适用于对应盒子，普通USB口不构成兼容条件 |
| Carlinkit：[CPC200-2air](https://www.carlinkit.com/2air) | 滚动产品页 | 有线转无线、原有控制和使用前提；连接适配能力不证明新增语音理解或助手服务 |
| Ottocast：[OttoSafe Knob](https://www.ottocast.com/products/ottosafe-knob) | 滚动产品页 | 旋钮操作、指定适配器及固件；页面清单存在差异，未证语音拾音或确认法律公司主体 |
| 深圳云衍相关软件：[Lumi Android应用条目](https://app.mi.com/details?id=com.example.lumi_client)、[隐私政策](https://yyzc.yylumi.com/privacy.html) | 政策2025-05-27；应用条目滚动；访问2026-11-06 | 直接读取商店开发主体、包名、简介与隐私链接；政策读取官方URL的索引正文，直开返回502。蓝牙绑定、模型及输入共享是政策声明，不等于特定整机当前实现 |
| LUMI教程：[安装使用原视频](https://www.douyin.com/video/7629608396925350134)、[原车音响原视频](https://www.douyin.com/video/7643012811606182563)、[实际读取的聚合页转写](https://www.douyin.com/shipin/7630288336766191616) | 教程日期不稳定；访问2026-11-06 | 实际阅读AI转写，未亲看原视频；涉及App绑定、后台聊天、媒体蓝牙与原车音响。个别动作脱离App蓝牙不证明完整离线对话、本地模型或CarPlay兼容 |
| ZIGZAG：[iOS同名Lumi应用](https://apps.apple.com/us/app/lumi-ai-car-companion/id6754324797) | 滚动商店页；访问2026-11-06 | 直接读取ZIGZAG TECHNOLOGY LIMITED发行信息；与所指机器人及Android主体的关系未确认，不合并规格或服务 |

LUMI的整机制造主体、确切SKU、当前报价与供给、本地模型和CarPlay支持仍未知；深圳云衍仅按已核实的Android软件开发/运营角色列示。同名软件、同根域其他业务与整机产品不得直接合并。

## （四）市场统计

| **责任方与资料** | **版本、日期** | **实际阅读范围与边界** |
|---|---|---|
| ACEA：[Vehicles on European roads 2026](https://www.acea.auto/files/ACEA_Report-%E2%80%93-Vehicles_on_European_roads_2026.pdf) | 发布2026-01-15；统计2024年 | PDF第5、11、15页：EU27乘用车、车龄、动力与脚注；不含互联入口缺口或改装购买率调查 |
| PZPM：[2025存量表](https://www1.pzpm.org.pl/pl/layout/set/print/content/download/2590/10563/file/Park_2025.pdf)、[2026/27年鉴](https://www1.pzpm.org.pl/pl/content/download/11094/68148/file/Raport_2026_caly_lekki.pdf) | 分别发布2026-05-13、2026-09-17；统计2025年 | 存量表第1页及年鉴第23–28页：更新记录、乘用车与平均车龄；不是实时在用车辆普查，也不是可售设备数量 |
| 国家统计局：[2025年国民经济和社会发展统计公报](https://www.stats.gov.cn/sj/zxfb/202602/t20260228_1962662.html) | 发布2026-02-28；统计2025年 | 原始HTML汽车保有量段落；民用轿车分类不同于EU乘用车，不合并为全球可售市场 |

评分是基于平台文档的研究判断；市场筛选比例、渠道成交率及网页默认输入是情景假设，均不是上述统计来源的调查结果。

## （五）辅助驾驶与模型

| **责任方与资料** | **版本、日期** | **实际阅读范围与边界** |
|---|---|---|
| Garmin：[Dash Cam X110用户手册](https://www8.garmin.com/manuals/webhelp/GUID-93747543-12A8-453C-9896-32070F5B0710/EN-US/Dash_Cam_X110_OM_EN-US.pdf) | ©2024 | 安装、记录、驾驶提醒与条件限制；未取得当前可核官网价或实车效果，不等同车辆控制 |
| Mobileye：[8 Connect手册](https://static.mobileye.com/manual/me8/Mobileye%208%20connect%20%E2%80%93%20User%20manual.pdf)、[后装业务公告](https://ir.mobileye.com/news-releases/news-release-details/mobileye-wind-down-aftermarket-solutions-unit) | 手册未明示日期；公告2024-03-18 | 预警功能、驾驶员责任及业务收缩原因；历史支持资料不代表当前重新开放后装销售 |
| comma：[车辆支持](https://docs.comma.ai/CARS/)、[安全说明](https://docs.comma.ai/concepts/safety/) | 滚动文档 | 车型、年份、配置及线束条件，驾驶员关注、接管与安全约束；未安装、刷写或进行道路验证 |
| Cerence：[CaLLM Edge嵌入式模型公告](https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive) | 2024-11-13 | 模型规格、嵌入式/混合部署与目标客户；企业集成方案不等于可直接采购的后装整机，也不是独立性能或车型交付验证 |

本地模型专项的扩展技术与产品来源见 [专题正文](https://dreamsoul-ai.github.io/in-vehicle-ai-research/advanced.html) 和 [专项样本的sources字段](https://dreamsoul-ai.github.io/in-vehicle-ai-research/data/advanced-products.json)，按2026年11月5日的阅读范围保留。
