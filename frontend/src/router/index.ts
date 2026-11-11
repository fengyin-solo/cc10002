import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Asset = () => import('@/views/asset/index.vue')
const Scanjob = () => import('@/views/scanjob/index.vue')
const Vuln = () => import('@/views/vuln/index.vue')
const Verify = () => import('@/views/verify/index.vue')
const Patch = () => import('@/views/patch/index.vue')
const Exemption = () => import('@/views/exemption/index.vue')
const Component = () => import('@/views/component/index.vue')
const Artifact = () => import('@/views/artifact/index.vue')
const Leaked = () => import('@/views/leaked/index.vue')
const Pentest = () => import('@/views/pentest/index.vue')
const Waf = () => import('@/views/waf/index.vue')
const Incident = () => import('@/views/incident/index.vue')
const Forensics = () => import('@/views/forensics/index.vue')
const Intel = () => import('@/views/intel/index.vue')
const Baseline = () => import('@/views/baseline/index.vue')
const Phishing = () => import('@/views/phishing/index.vue')
const Bounty = () => import('@/views/bounty/index.vue')
const Review = () => import('@/views/review/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/asset', name: 'asset', component: Asset },
    { path: '/scanjob', name: 'scanjob', component: Scanjob },
    { path: '/vuln', name: 'vuln', component: Vuln },
    { path: '/verify', name: 'verify', component: Verify },
    { path: '/patch', name: 'patch', component: Patch },
    { path: '/exemption', name: 'exemption', component: Exemption },
    { path: '/component', name: 'component', component: Component },
    { path: '/artifact', name: 'artifact', component: Artifact },
    { path: '/leaked', name: 'leaked', component: Leaked },
    { path: '/pentest', name: 'pentest', component: Pentest },
    { path: '/waf', name: 'waf', component: Waf },
    { path: '/incident', name: 'incident', component: Incident },
    { path: '/forensics', name: 'forensics', component: Forensics },
    { path: '/intel', name: 'intel', component: Intel },
    { path: '/baseline', name: 'baseline', component: Baseline },
    { path: '/phishing', name: 'phishing', component: Phishing },
    { path: '/bounty', name: 'bounty', component: Bounty },
    { path: '/review', name: 'review', component: Review },
  ],
})

export default router
