"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import asset as router_asset
from app.routers import scanjob as router_scanjob
from app.routers import vuln as router_vuln
from app.routers import verify as router_verify
from app.routers import patch as router_patch
from app.routers import exemption as router_exemption
from app.routers import component as router_component
from app.routers import artifact as router_artifact
from app.routers import leaked as router_leaked
from app.routers import pentest as router_pentest
from app.routers import waf as router_waf
from app.routers import incident as router_incident
from app.routers import forensics as router_forensics
from app.routers import intel as router_intel
from app.routers import baseline as router_baseline
from app.routers import phishing as router_phishing
from app.routers import bounty as router_bounty
from app.routers import review as router_review

ROUTERS = [router_asset, router_scanjob, router_vuln, router_verify, router_patch, router_exemption, router_component, router_artifact, router_leaked, router_pentest, router_waf, router_incident, router_forensics, router_intel, router_baseline, router_phishing, router_bounty, router_review]
