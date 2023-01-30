"""
author:     R
encoding:   utf-8
title:      模板插件
version:    1.0
introduce:  无可奉告
qq:         2042136767
phone:      ...
time:       2023年1月16日12:28:23
"""
# 注解
from library.Decorator import Meta, Event, Mapping

# Bean
from core.Request import Request
from core.Response import Response
from cq.core.MessageBean import MessageBean

# context
from core.RequestContext import RequestContext
from core.SessionContext import SessionContext
from core.ApplicationContext import ApplicationContext

# 自动注入数据
request: Request = None
response: Response = None
messageBean: MessageBean = None

requestContext: RequestContext = None
applicationContext: ApplicationContext = None
sessionContext: SessionContext = None

# 排除项
excludeList = []

# 全局变量(Global Variable List)
gvl = {
    "qq": "2042136767"
}

import random
from library.PythonEnhanceUtil import PythonEnhanceUtil


@Event.messageGroup()
@Mapping.prefix([".probability", "概率计算"])
def probability(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: number, percentage")
        return False

    if len(params) == 1:
        response.text.append("缺少参数: percentage")
        return False
    
    number: int = PythonEnhanceUtil.getByList(params, 0, int, 10)
    percentage: int = PythonEnhanceUtil.getByList(params, 1, int, 2)

    data = {"True" : 0, "False" : 0}
    for i in range(0, number):
        lucky = random.randint(0, 100 * 10) # 概率公式

        if lucky <= percentage * 10:
            data["True"] += 1
        else:
            data["False"] += 1
        
    response.text.append(f"正在为您抽{number}次(概率{percentage}%)\n抽中次数为: {data['True']}\n没抽中次数为: {data['False']}")
    return True

# TODO: ...
@Event.messageGroup()
@Mapping.prefix("年龄计算")
def age(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")
    
    response.text.append("该功能已下架")
    return False

# TODO: ...
@Event.messageGroup()
@Mapping.prefix("保质期计算")
def qualityGuaranteePeriod(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    return False

@Event.messageGroup()
@Mapping.prefix(["饮水量推荐", "饮水量计算"])
def waterStandard(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    kg = PythonEnhanceUtil.getByList(params, 0, int)
    if kg == None:
        response.text.append("缺少参数: kg(int)")
        return True

    All = kg * 33
    AM1 = int(All / 6.8)
    AM2 = int(All / 7.36)
    AM3 = int(All / 6.85)

    PM1 = int(All / 6.8)
    PM2 = int(All / 6.79)
    PM3 = int(All / 6.82)
    PM4 = int(All / 7.17)

    string = f"""
    [结果]
    每日饮水量共{All}(毫升)\n

    [喝水时间表]
    AM(06:30)
    经过一整夜的睡眠,身体开始缺水
    起床之际先喝杯{AM1}CC的水,可帮助肾脏及肝脏解毒.
    别马上吃早餐,等待半小时让水融入每个细胞
    进行新陈代谢后,再进食!\n

    AM(08:30)
    清晨从起床到办公室的过程
    时间总是特别紧凑,情绪也较紧张
    身体无形中会出现脱水现象
    所以到了办公室后,先别急着泡咖啡
    给自己一杯至少{AM2}CC的水!\n

    AM(11:00)
    在办公室里工作一段时间后
    一定得趁起身动动的时候
    再给自己一天里的第三杯水{AM3}CC
    补充流失的水分,有助于放松紧张的工作情绪!\n

    PM(12:50)
    用完午餐半小时后,喝一些水{PM1}CC
    取代让你发胖的人工饮料,可以加强身体的消化功能
    不仅对健康有益,也能助你维持身材.\n

    PM(03:00)
    以一杯健康矿泉水代替午茶与咖啡等提神饮料吧!
    喝上一大杯{PM2}CC的水
    除了补充在办公室里流失的水份之外
    还能帮助头脑清醒.\n

    PM(05:30)
    下班离开办公室前,再喝一杯水{PM3}CC.
    想要运用喝水减重的可以多喝几杯
    增加饱足感,待会吃晚餐时
    自然不会暴饮暴食.\n

    PM(10:00)
    睡前一至半小时再喝上一杯水{PM4}CC
    目标达成!\n

    [参照物] 
    一个可乐罐大概能装 335CC的水\n
    """
    string = string.replace("\n\n", "\n").replace("    ", "")
    response.text.append(string)
    return True

@Event.messageGroup()
@Mapping.prefix(["BMI", "bmi"])
def bmi(*args, **kwargs):
    """
    【BMI计算】【Body Mass Index】
    BMI  = 体重(kg) / 身高^2(m)
    2.86 = 70kg    / (1.75x1.75)
    """
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    height = PythonEnhanceUtil.getByList(params, 0, int)
    kg = PythonEnhanceUtil.getByList(params, 1, int)
    if height == None:
        response.text.append("缺少参数: height(int), kg(int)")
        return True
    if kg == None:
        response.text.append("缺少参数: kg")
        return True

    height = str(height)
    height = "%s.%s" % (height[0], height[1:])
    height = float(height)

    bmi = kg / (height * height)
    bmiList = str(bmi).split(".")
    bmiInt = "%s.%s" % (bmiList[0], bmiList[1][0])
    string = f"""
    您的BMI值为 : [{bmiInt}]({bmi})
    体重过轻 BMI < 18.5
    正常范围 BMI > 18.5 And BMI < 24
    体重过重 BMI > 24
    轻度肥胖 BMI > 27
    中度肥胖 BMI > 30
    重度肥胖 BMI > 35
    """
    string = string.replace("    ", "")
    response.text.append(string)
    return True

def humanQualityRaw(name:str) -> int:
    number = 0
    for i in name:
        number += ord(i)
    number = number / 100
    numberFloat = int(str(number).split(".")[-1])
    return numberFloat
@Event.messageGroup()
@Mapping.prefix("人品计算")
def humanQuality(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")
    # ASCII码

    username = PythonEnhanceUtil.getByList(params, 0)
    if username == None:
        response.text.append("缺少参数: username")
        return True

    number = humanQualityRaw(username)
    response.text.append(f"[{message}]\n您的人品值为: {number} \nTips:仅供娱乐参考,该数值由ASCII码转换得来")
    return True



@Event.messageGroup()
@Mapping.prefix("算数")
def calculation(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    tmp = "" + message
    l = [ "+", "-", "*", "/" ]
    for i in l: tmp = tmp.replace(i, "")
    for i in range(0,10): tmp = tmp.replace(str(i), "")
    tmp = tmp.strip()
    if len(tmp) != 0:
        response.text.append(f"非法参数: {tmp}")
        return None

    if len(message.split("**")) >= 2:
        response.text.append("非法参数: 目前暂不支持**运算符, 后续会加入")
        return None

    response.text.append(f"计算结果为: {eval(message)}")
    return True


