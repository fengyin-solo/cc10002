"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class AssetEntry(BaseModel):
    """纳管资产明细结构。"""

    field_0: str | None = None  # 资产编号
    field_1: str | None = None  # 主机名称
    field_2: str | None = None  # 归属业务
    field_3: str | None = None  # 公网地址
    field_4: str | None = None  # 开放端口
    field_5: str | None = None  # 服务指纹
    field_6: str | None = None  # 责任团队
    field_7: str | None = None  # 纳管状态

class ScanjobEntry(BaseModel):
    """扫描作业明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 扫描策略
    field_2: str | None = None  # 目标网段
    field_3: str | None = None  # 扫描引擎
    field_4: str | None = None  # 并发线程
    field_5: str | None = None  # 发起人
    field_6: str | None = None  # 开始时刻
    field_7: str | None = None  # 作业状态

class VulnEntry(BaseModel):
    """漏洞条目明细结构。"""

    field_0: str | None = None  # 漏洞编号
    field_1: str | None = None  # 漏洞名称
    field_2: str | None = None  # CVE 编号
    field_3: str | None = None  # 影响组件
    field_4: str | None = None  # 危害评分
    field_5: str | None = None  # 利用难度
    field_6: str | None = None  # 发现来源
    field_7: str | None = None  # 漏洞等级

class VerifyEntry(BaseModel):
    """验证记录明细结构。"""

    field_0: str | None = None  # 验证编号
    field_1: str | None = None  # 关联漏洞
    field_2: str | None = None  # 复现环境
    field_3: str | None = None  # 复现步骤
    field_4: str | None = None  # 验证人
    field_5: str | None = None  # 验证日期
    field_6: str | None = None  # 验证结论
    field_7: str | None = None  # 验证状态

class PatchEntry(BaseModel):
    """修复单明细结构。"""

    field_0: str | None = None  # 修复单号
    field_1: str | None = None  # 关联漏洞
    field_2: str | None = None  # 补丁版本
    field_3: str | None = None  # 影响组件
    field_4: str | None = None  # 灰度批次
    field_5: str | None = None  # 上线窗口
    field_6: str | None = None  # 复核人
    field_7: str | None = None  # 修复状态

class ExemptionEntry(BaseModel):
    """豁免申请明细结构。"""

    field_0: str | None = None  # 豁免编号
    field_1: str | None = None  # 豁免事由
    field_2: str | None = None  # 关联漏洞
    field_3: str | None = None  # 补偿措施
    field_4: str | None = None  # 豁免范围
    field_5: str | None = None  # 到期日期
    field_6: str | None = None  # 审批人
    field_7: str | None = None  # 豁免状态

class ComponentEntry(BaseModel):
    """依赖组件明细结构。"""

    field_0: str | None = None  # 组件名称
    field_1: str | None = None  # 所属语言
    field_2: str | None = None  # 当前版本
    field_3: str | None = None  # 已知缺陷数
    field_4: str | None = None  # 许可证类型
    field_5: str | None = None  # 维护团队
    field_6: str | None = None  # 引入工程
    field_7: str | None = None  # 组件状态

class ArtifactEntry(BaseModel):
    """制品清单明细结构。"""

    field_0: str | None = None  # 清单编号
    field_1: str | None = None  # 制品名称
    field_2: str | None = None  # 构建版本
    field_3: str | None = None  # 依赖层级
    field_4: str | None = None  # 生成时间
    field_5: str | None = None  # 签名状态
    field_6: str | None = None  # 存放仓库
    field_7: str | None = None  # 清单状态

class LeakedEntry(BaseModel):
    """泄露线索明细结构。"""

    field_0: str | None = None  # 泄露编号
    field_1: str | None = None  # 泄露类型
    field_2: str | None = None  # 命中位置
    field_3: str | None = None  # 提交作者
    field_4: str | None = None  # 发现时刻
    field_5: str | None = None  # 内容摘要
    field_6: str | None = None  # 轮换进度
    field_7: str | None = None  # 线索状态

class PentestEntry(BaseModel):
    """测试委托明细结构。"""

    field_0: str | None = None  # 测试编号
    field_1: str | None = None  # 测试类型
    field_2: str | None = None  # 授权范围
    field_3: str | None = None  # 测试人员
    field_4: str | None = None  # 测试窗口
    field_5: str | None = None  # 报告版本
    field_6: str | None = None  # 高危发现数
    field_7: str | None = None  # 测试状态

class WafEntry(BaseModel):
    """拦截策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 规则名称
    field_2: str | None = None  # 生效域名
    field_3: str | None = None  # 匹配条件
    field_4: str | None = None  # 处置动作
    field_5: str | None = None  # 策略优先级
    field_6: str | None = None  # 生效时间
    field_7: str | None = None  # 策略状态

class IncidentEntry(BaseModel):
    """安全事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 事件类型
    field_2: str | None = None  # 影响范围
    field_3: str | None = None  # 初判等级
    field_4: str | None = None  # 响应负责人
    field_5: str | None = None  # 处置时限
    field_6: str | None = None  # 上报渠道
    field_7: str | None = None  # 事件状态

class ForensicsEntry(BaseModel):
    """取证样本明细结构。"""

    field_0: str | None = None  # 取证编号
    field_1: str | None = None  # 样本类型
    field_2: str | None = None  # 文件哈希
    field_3: str | None = None  # 分析工具
    field_4: str | None = None  # 分析结论
    field_5: str | None = None  # 封存位置
    field_6: str | None = None  # 分析人
    field_7: str | None = None  # 取证状态

class IntelEntry(BaseModel):
    """情报指标明细结构。"""

    field_0: str | None = None  # 情报编号
    field_1: str | None = None  # 指标类型
    field_2: str | None = None  # 指标值
    field_3: str | None = None  # 情报来源
    field_4: str | None = None  # 置信度
    field_5: str | None = None  # 命中次数
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 情报状态

class BaselineEntry(BaseModel):
    """基线检查项明细结构。"""

    field_0: str | None = None  # 基线编号
    field_1: str | None = None  # 检查项
    field_2: str | None = None  # 适用系统
    field_3: str | None = None  # 期望值
    field_4: str | None = None  # 实测值
    field_5: str | None = None  # 检查频率
    field_6: str | None = None  # 整改负责人
    field_7: str | None = None  # 合规判定

class PhishingEntry(BaseModel):
    """演练批次明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 演练主题
    field_2: str | None = None  # 投递人数
    field_3: str | None = None  # 打开人数
    field_4: str | None = None  # 上报人数
    field_5: str | None = None  # 演练轮次
    field_6: str | None = None  # 承办部门
    field_7: str | None = None  # 演练状态

class BountyEntry(BaseModel):
    """外部提交明细结构。"""

    field_0: str | None = None  # 提交编号
    field_1: str | None = None  # 提交人
    field_2: str | None = None  # 所属机构
    field_3: str | None = None  # 漏洞等级
    field_4: str | None = None  # 赏金金额
    field_5: str | None = None  # 复核结论
    field_6: str | None = None  # 提交日期
    field_7: str | None = None  # 发放状态

class ReviewEntry(BaseModel):
    """复盘记录明细结构。"""

    field_0: str | None = None  # 复盘编号
    field_1: str | None = None  # 复盘周期
    field_2: str | None = None  # 遗漏漏洞数
    field_3: str | None = None  # 平均修复时长
    field_4: str | None = None  # 复盘结论
    field_5: str | None = None  # 主持人
    field_6: str | None = None  # 改进事项
    field_7: str | None = None  # 复盘状态
