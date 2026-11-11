# 漏洞检测与治理运营平台

面向暴露面资产纳管、扫描作业编排、漏洞复现验证、补丁灰度上线与豁免审批的一体化漏洞治理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 暴露面资产 | `asset` | 纳管资产 | 资产编号、主机名称、归属业务 |
| 扫描作业 | `scanjob` | 扫描作业 | 作业编号、扫描策略、目标网段 |
| 漏洞条目 | `vuln` | 漏洞条目 | 漏洞编号、漏洞名称、CVE 编号 |
| 复现验证 | `verify` | 验证记录 | 验证编号、关联漏洞、复现环境 |
| 补丁修复 | `patch` | 修复单 | 修复单号、关联漏洞、补丁版本 |
| 风险豁免 | `exemption` | 豁免申请 | 豁免编号、豁免事由、关联漏洞 |
| 开源组件 | `component` | 依赖组件 | 组件名称、所属语言、当前版本 |
| 制品清单 | `artifact` | 制品清单 | 清单编号、制品名称、构建版本 |
| 凭据泄露 | `leaked` | 泄露线索 | 泄露编号、泄露类型、命中位置 |
| 渗透测试 | `pentest` | 测试委托 | 测试编号、测试类型、授权范围 |
| 防护策略 | `waf` | 拦截策略 | 策略编号、规则名称、生效域名 |
| 安全事件 | `incident` | 安全事件 | 事件编号、事件类型、影响范围 |
| 取证分析 | `forensics` | 取证样本 | 取证编号、样本类型、文件哈希 |
| 威胁情报 | `intel` | 情报指标 | 情报编号、指标类型、指标值 |
| 安全基线 | `baseline` | 基线检查项 | 基线编号、检查项、适用系统 |
| 钓鱼演练 | `phishing` | 演练批次 | 演练编号、演练主题、投递人数 |
| 外部提交 | `bounty` | 外部提交 | 提交编号、提交人、所属机构 |
| 治理复盘 | `review` | 复盘记录 | 复盘编号、复盘周期、遗漏漏洞数 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
