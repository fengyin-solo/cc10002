<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">漏洞检测与治理运营平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向暴露面资产纳管、扫描作业编排、漏洞复现验证、补丁灰度上线与豁免审批的一体化漏洞治理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "暴露面资产", path: "/asset" }, { label: "扫描作业", path: "/scanjob" }, { label: "漏洞条目", path: "/vuln" }, { label: "复现验证", path: "/verify" }, { label: "补丁修复", path: "/patch" }, { label: "风险豁免", path: "/exemption" }, { label: "开源组件", path: "/component" }, { label: "制品清单", path: "/artifact" }, { label: "凭据泄露", path: "/leaked" }, { label: "渗透测试", path: "/pentest" }, { label: "防护策略", path: "/waf" }, { label: "安全事件", path: "/incident" }, { label: "取证分析", path: "/forensics" }, { label: "威胁情报", path: "/intel" }, { label: "安全基线", path: "/baseline" }, { label: "钓鱼演练", path: "/phishing" }, { label: "外部提交", path: "/bounty" }, { label: "治理复盘", path: "/review" }]
</script>
