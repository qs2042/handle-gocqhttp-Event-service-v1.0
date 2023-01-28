"""
author:     R
encoding:   utf-8
title:      R的垃圾桶
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

import requests, time, json, random, re
from demjson import decode  # pip install demjson
from cq.CQCode import CQCode



# 实时热点
# 微博/B站/知乎热搜
# Github高星项目
# 快递查询
# 百度/搜狗/必应搜索
# 创造冒险
# 创造角色(Default, 动漫, 古代, 小说, 影视剧)
# 创造梦境
# 人生模拟器
# 比特币模拟器
# 黑白名单
# 好感度
# 整点报时
# 定时消息
# 表情包制作
# 世界频道
# 消息转发
# 摸一摸(戳头像)
# 禁我/抽奖
# 随机老婆/老公/外星人(取群友)




@Event.messageGroup()
@Mapping.approved()
def reverseRaw(*args, **kwargs):
    message:str = messageBean.message

    assassinationList = [
        "鱼鱼", "阿白", "阿蚕",
        "云云", "蛙蛙", "冬日",
        "花花", "雨凡", "换装", 
        "糕糕", "阿黑", "言儿", "等..."
    ]
    if not "R" in message.upper(): return None
    if not "YYDS" in message.upper(): return None

    result = ", ".join(assassinationList)
    response.text.append(f"{result} YYDS!TQL!WSL!NB!666!")
    return True

# TODO: ...
@Event.messageGroup()
@Mapping.prefix("抽签算卦")
def divination(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    # (Year + Month + Day + Name)
    response.text.append("该功能已下架")
    return False

# TODO: ...
@Event.messageGroup()
@Mapping.prefix("今日运势")
def fortune(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    # (Year + Month + Day + Name)
    response.text.append("该功能已下架")
    return False

# TODO: ...
@Event.messageGroup()
@Mapping.prefix("星座运势")
def fortuneConstellation(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    # (Year + Month + Day + Name)
    response.text.append("该功能已下架")
    return False

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

    if len(params) == 0:
        response.text.append("缺少参数: kg")
        return True

    kg = None
    tmp: str = params[0]
    if tmp.isdigit(): 
        kg = int(tmp)
    else:
        response.text.append("参数错误: 不是正数")
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

    if len(params) == 0:
        response.text.append("缺少参数: height, kg")
        return True
    if len(params) == 1:
        response.text.append("缺少参数: kg")
        return True
    if len(params) >= 3:
        response.text.append("参数过多")
        return True
    
    height: int = None
    kg: int = None

    tmpHeight: str = params[0]
    tmpKg: str = params[1]
    if tmpHeight.isdigit(): height = int(tmpHeight)
    else: 
        response.text.append("参数错误: height不是正数")
        return True
    
    if tmpKg.isdigit(): kg = int(tmpKg)
    else:
        response.text.append("参数错误: kg不是正数")
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

    if len(params) == 0:
        response.text.append("缺少参数: name")
        return True

    number = humanQualityRaw(message)
    response.text.append(f"[{message}]\n您的人品值为: {number} \nTips:仅供娱乐参考,该数值由ASCII码转换得来")
    return True

def smallScreenwriterTemplateRaw(name, describe):
    string = """
    说到[Name]大家肯定都不陌生.
    那么[Name][Describe]是怎么一回事呢？
    [Name]相信大家都很熟悉.
    但是[Name]为什么[Describe]是怎么回事呢.
    这是我们都关心的问题.
    下面就让小编来带大家一起了解一下.
    [Name]为什么[Describe].
    [Name][Describe]其实就是因为[Describe].
    大家可能会很惊讶.
    [Name]怎么会[Describe]呢？
    但事实就是这样.
    看完这段网友表示难以置信.
    小编也感到非常惊讶.
    以上就是关于[Name]为什么[Describe]的全部内容了.
    大家对此有什么想法呢?
    欢迎在评论区告诉小编一起讨论哦!
    """.replace("\n\n", "\n").replace("    ", "")
    result = string.replace("[Name]", name).replace("[Describe]", describe)
    return result
@Event.messageGroup()
@Mapping.prefix("小编模板")
def smallScreenwriterTemplate(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: name, describe")
        return True
    if len(params) == 1:
        response.text.append("缺少参数: describe")
        return True
    
    response.text.append(smallScreenwriterTemplateRaw(params[0], params[1]))
    return True

def dianaMissTemplateRaw(self, name="嘉然小姐", desireDog="狗", desireCat="猫猫", real="老鼠"):
    string = """
    我好想做[Name]的[Desire_Dog]啊.
    可是[Name]说她喜欢的是[Desire_Cat]
    我哭了.
    我知道既不是[Desire_Dog]
    也不是[Desire_Cat]的我为什么要哭的
    因为我其实是一只[Real].
    我从没奢望[Name]能喜欢自己.
    我明白的
    所有人都喜欢理解余裕上手天才打钱的萌萌的[Desire_Dog]
    或者[Desire_Cat]
    没有人会喜欢阴湿带病的[Real].
    但我还是问了[Name]
    "我能不能做你的[Desire_Dog]?"
    我知道我是注定做不了[Desire_Dog]的
    但如果她喜欢[Desire_Dog]
    我就可以一直在身边看着她了
    哪怕她怀里抱着的永远都是[Desire_Dog].
    可是她说喜欢的是[Desire_Cat].
    她现在还在看着我,还在逗我开心
    是因为[Desire_Cat]还没有出现
    只有我这[Real]每天蹑手蹑脚地从洞里爬出来,远远地和她对视.
    等她喜欢的[Desire_Cat]来了的时候
    我就该重新滚回我的洞了吧.
    但我还是好喜欢她
    她能在我还在她身边的时候多看我几眼吗？
    [Name]说接下来的每个圣诞夜都要和大家一起过.
    我不知道大家指哪些人.
    好希望这个集合能够对我做一次胞吞.

    [Desire_Cat]还在害怕[Name]
    我会去把她爱的[Desire_Cat]引来的
    我知道稍有不慎,我就会葬身[Desire_Cat]口.
    那时候[Name]大概会把我的身体好好地装起来扔到门外吧.
    那我就成了一包[Real]味鼠条
    嘻嘻.
    我希望她能把我扔得近一点
    因为我还是好喜欢她,会一直喜欢下去的.

    我的灵魂透过窗户向里面看去
    挂着的铃铛在轻轻鸣响
    [Name]慵懒地靠在沙发上
    表演得非常温顺的[Desire_Cat]坐在她的肩膀
    壁炉的火光照在她的脸庞
    我冻僵的心脏在风里微微发烫.
    """.replace("[Name]", name)
    result = string.replace("[Desire_Dog]", desireDog)
    result = result.replace("[Desire_Cat]", desireCat)
    result = result.replace("[Real]", real)
    return result.replace("\n\n", "\n").replace("    ", "")
@Event.messageGroup()
@Mapping.prefix("嘉然模板")
def dianaMissTemplate(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: name, desire1=dog, desire=cat, real=rats")
        return True
    
    name = params[0]
    response.text.append(dianaMissTemplateRaw(name))
    return True

# 疫情地区状况
def virusAllRaw():
    url = "https://lab.isaaclin.cn/nCoV/api/overall"
    res = requests.get(url)
    data = json.loads(res.text)
    if str(data["success"]) != "True":
        return "False"
    data = data["results"][0]

    string = ""

    string += "现存确诊人数: %s(%s)\n" % (data["currentConfirmedCount"],data["currentConfirmedIncr"])
    string += "累计确诊人数: %s(%s)\n" % (data["confirmedCount"],data["confirmedIncr"])
    string += "似疑感染人数: %s(%s)\n" % (data["suspectedCount"],data["suspectedIncr"])
    string += "自愈人数: %s(%s)\n" % (data["curedCount"],data["curedIncr"])
    string += "死亡人数: %s(%s)\n" % (data["deadCount"],data["deadIncr"])
    string += "重症病例人数: %s(%s)\n" % (data["seriousCount"],data["seriousIncr"])
    #string += "globalStatistics: %s\n" % data["globalStatistics"]
    timeStamp = str(data["updateTime"])[:-3]
    timeArray = time.localtime(int(timeStamp))
    string += "数据采集时间: %s\n" % time.strftime("%Y年%m月%d日 %H:%M:%S", timeArray)
    string += "数据来源: 丁香园(portal.dxy.cn)\n"
    string += "鸣谢项目: Github(BlankerL/DXY-COVID-19-Crawler)"
    return string
@Event.messageGroup()
@Mapping.all("疫情新闻")
def virusAll(*args, **kwargs):
    response.text.append(virusAllRaw())
    return True

def virusProvinceNameListRaw(pageSee, pageShow=7):
    url = "https://lab.isaaclin.cn/nCoV/api/provinceName"
    res = requests.get(url)
    data = json.loads(res.text)
    if str(data["success"]) != "True":
        return "False"
    data = data["results"]

    return data
@Event.messageGroup()
@Mapping.prefix("疫情地区")
def virusProvinceNameList(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    page: int = None
    if len(params) == 0: page = 1
    else:
        tmpPage: str = params[0]
        if tmpPage.isdigit(): page = int(tmpPage)
        else: page = 1

    response.text.append(virusProvinceNameListRaw(page))
    return True

def virusAreaRaw(province, cite=None):
    url = "https://lab.isaaclin.cn/nCoV/api/area?province=%s" % province
    res = requests.get(url)
    data = json.loads(res.text)
    if str(data["success"]) != "True":
        return "False"
    # print(data)
    # print("*"*50)
    data = data["results"][0]

    string = ""
    #string += "城市编号: %s\n" % data["locationId"]
    #string += "大洲名称: %s(%s)\n" % (data["continentName"],data["continentEnglishName"])
    #string += "国家名称: %s(%s)\n" % (data["countryName"],data["countryEnglishName"])
    #string += "countryFullName: %s\n" % data["countryFullName"]
    #string += "省份,地区或直辖市全称: %s(%s)\n" % (data["provinceName"],data["provinceEnglishName"])
    #string += "省份,地区或直辖市简称: %s\n" % data["provinceShortName"]
    string += "城市: %s(%s)\n" % (data["provinceName"],data["provinceEnglishName"])
    string += "现存确诊人数: %s\n" % data["currentConfirmedCount"]
    string += "累计确诊人数: %s\n" % data["confirmedCount"]
    string += "疑似感染人数: %s\n" % data["suspectedCount"]
    string += "治愈人数: %s\n" % data["curedCount"]
    string += "死亡人数: %s\n" % data["deadCount"]
    # string += "其他信息: %s\n" % data["comment"]
    if cite != None:
        '''
        citiesString = "下属城市的情况: 可能是城市名输错了,无法准确显示信息\n"
        for i in data["cities"]:
            if i["cityName"] == cite:
                citiesString = "下属城市的情况: %s\n" % i
                break
        string += citiesString
        '''
        isBoolean = False
        for i in data["cities"]:
            if i["cityName"] == cite:
                isBoolean = i
                break

        if isBoolean != False:
            string = ""
            string += "名称: %s(%s)\n" % (isBoolean["cityName"], isBoolean["cityEnglishName"])
            string += "现存确诊人数: %s\n" % isBoolean["currentConfirmedCount"]
            string += "累计确诊人数: %s\n" % isBoolean["confirmedCount"]
            string += "疑似感染人数: %s\n" % isBoolean["suspectedCount"]
            string += "治愈人数: %s\n" % isBoolean["curedCount"]
            string += "死亡人数: %s" % isBoolean["deadCount"]
            #string += "highDangerCount: %s\n" % isBoolean["highDangerCount"]
            #string += "midDangerCount: %s\n" % isBoolean["midDangerCount"]
            #string += "locationId: %s\n" % isBoolean["locationId"]
            #string += "currentConfirmedCountStr: %s\n" % isBoolean["currentConfirmedCountStr"]
            return string
    if cite == None:
        string += "下属城市的情况: [请输入城市名]\n"

    timeStamp = str(data["updateTime"])[:-3]
    timeArray = time.localtime(int(timeStamp))
    string += "数据采集时间: %s\n" % time.strftime("%Y年%m月%d日 %H:%M:%S", timeArray)
    string += "数据来源: 丁香园(portal.dxy.cn)\n"
    string += "鸣谢项目: Github(BlankerL/DXY-COVID-19-Crawler)"
    return string
def virusAreaRawPro(province, cite=None):
    url = "https://lab.isaaclin.cn/nCoV/api/area?province=%s" % province
    res = requests.get(url)
    data = json.loads(res.text)
    if str(data["success"]) != "True":
        return "False"
    data = data["results"][0]

    string = ""
    string += "城市: %s(%s)\n" % (data["provinceName"],data["provinceEnglishName"])
    string += "现存确诊人数: %s\n" % data["currentConfirmedCount"]
    string += "累计确诊人数: %s\n" % data["confirmedCount"]
    string += "疑似感染人数: %s\n" % data["suspectedCount"]
    string += "治愈人数: %s\n" % data["curedCount"]
    string += "死亡人数: %s\n" % data["deadCount"]
    if cite != None:
        isBoolean = False
        for i in data["cities"]:
            if i["cityName"] == cite:
                isBoolean = i
                break

        if isBoolean != False:
            string = ""
            string += "名称: %s(%s)\n" % (isBoolean["cityName"], isBoolean["cityEnglishName"])
            string += "现存确诊人数: %s\n" % isBoolean["currentConfirmedCount"]
            string += "累计确诊人数: %s\n" % isBoolean["confirmedCount"]
            string += "疑似感染人数: %s\n" % isBoolean["suspectedCount"]
            string += "治愈人数: %s\n" % isBoolean["curedCount"]
            string += "死亡人数: %s" % isBoolean["deadCount"]
            return string
    if cite == None:
        string += "下属城市的情况: [请输入城市名]\n"

    timeStamp = str(data["updateTime"])[:-3]
    timeArray = time.localtime(int(timeStamp))
    string += "数据采集时间: %s\n" % time.strftime("%Y年%m月%d日 %H:%M:%S", timeArray)
    string += "数据来源: 丁香园(portal.dxy.cn)\n"
    string += "鸣谢项目: Github(BlankerL/DXY-COVID-19-Crawler)"
    return string
@Event.messageGroup()
@Mapping.prefix("疫情状况")
def virusAreaPro(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: province, cite")
        return True
    if len(params) == 1:
        response.text.append("缺少参数: cite")
        return True
    
    province = "广东省"
    cite = "东莞"
    # asyncio方式
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(virusAreaRaw(province, cite))
    # loop.run_until_complete(get_future)  # 事件循环
    # result = get_future.result()
    response.text.append(virusAreaRawPro(province, cite))
    return True

# TODO: 手机归属
def phoneNumberAttributionRaw(self, phoneNumber):
    web = phoneNumber[0:3]
    region = phoneNumber[3:7]
    region = phoneNumber[7:11]

    yd = [134,135,136,137,138,139,150,151,152,157,158,159,178,182,183,184,187,188,198]
    lt = [130,131,132,155,156,166,175,176,185,186]
    dx = [133,153,173,177,180,181,189,191,199]

    for i in yd:
        if i == web:
            return "移动"
    for i in lt:
        if i == web:
            return "联通"
    for i in dx:
        if i == web:
            return "电信"

# TODO: QQ头像查询(False)
def partyTitleImageRaw(self, targetQQ):
    url = "http://q1.qlogo.cn/g"
    params = {
        "b": "qq",
        "nk": targetQQ,
        "s": "640",
    }
    return self.session.get(url, params=params)
def partyTitleImage(self, message:str, triggerInstructionList:list):
    isReply = self.prifix(message, triggerInstructionList)
    if isReply == "False":
        return isReply
    if isReply == "Default":
        pass
    if isReply != "Default":
        pass


    return None

# TODO: 垃圾分类查询
def refuseClassificationRaw(self, keyWord):
    url = "https://lajifenleiapp.com/sk/%s" % keyWord
    res = self.session.get(url)

    p_Identification = r'<span style="#2e2a2b">(.*?)</span></h1></div>'
    Identification = re.findall(p_Identification, res.text)[0]

    p_Info = r'<div class="col-md-12 col-xs-12">(.*?)</div>'
    Info_Raw = re.findall(p_Info, res.text)
    Info = ""
    for i in Info_Raw:
        Info += "%s \n" % i

    string = """
    昵称: [keyWord]
    标识: [Identification]
    [Info]
    """.replace("[keyWord]", keyWord)
    string = string.replace("[Identification]", Identification)
    string = string.replace("[Info]", Info)

    string = string.replace("\n\n", "\n").replace("        ", "")
    return string[1:-1]
def refuseClassification(self, message:str, triggerInstructionList:list):
    isReply = self.prifix(message, triggerInstructionList)
    if isReply == "False":
        return isReply
    if isReply == "Default":
        text = self.refuseClassificationRaw("衣服")
    if isReply != "Default":
        text = self.refuseClassificationRaw(isReply)

    list = re.findall(r'<.*?>', text)
    for i in list:
        text = text.replace(i, "")

    return text

# TODO: 联想词查询(百度)
def associateWordBaiDuRaw(self, keyWord):
    Url = "https://www.baidu.com/sugrec"
    Params = {
        "cb": "jQuery1111042881393840028337_1617071732854",
        "ie": "utf-8",
        "wd": keyWord,
        "prod": "open_image",
        "t": "0.5594884698388642",
        "_": "1617071732857",
    }
    Params = {
        "pre": "1",
        "p": "3",
        "ie": "utf-8",
        "json": "1",
        "prod": "pc",
        "from": "pc_web",
        "sugsid": "35106,31253,35049,34584,34517,34532,35234,34579,34812,34814,26350,35112",
        "wd": keyWord,
        "req": "2",
        "csor": "2",
        "pwd": "qs",
        "cb": "jQuery110203756743872956667_1637218512062",
        "_": "1637218512065",
    }
    res = self.session.get(Url, params=Params)
    return res
def associateWordBaiDu(self, message:str, triggerInstructionList:list):
    isReply = self.prifix(message, triggerInstructionList)
    if isReply == "False":
        return isReply
    if isReply == "Default":
        res = self.associateWordBaiDuRaw("小晴")
    if isReply != "Default":
        res = self.associateWordBaiDuRaw(isReply)

    text = res.text[42:-1]
    data = json.loads(text)
    string = ""
    for i in range(0, len(data["g"])):
        string += "%s \n" % data["g"][i]["q"]

    return string

# TODO: 联想词查询(搜狗)
def associateWordSoGouRaw(self, keyWord: str):
    url = "https://baikeapi.sogou.com/suggsearch/sugg/ajaj_json.jsp"
    params = {
        "type": "baike",
        "key": keyWord,
        "pr": "baike.web",
        "callback": "jQuery111103725644847587286_1639366256691",
        "_": "1639366256695",
        "_traceId": "4c8316ef7eba46e590c1a4e5461eac23:9",
    }
    res = self.session.get(url, params=params)
    res.encoding = "GBK"
    return res
def associateWordSoGou(self, message:str, triggerInstructionList:list):
    isReply = self.prifix(message, triggerInstructionList)
    if isReply == "False":
        return isReply
    if isReply == "Default":
        res = self.associateWordSoGouRaw("小晴")
    if isReply != "Default":
        res = self.associateWordSoGouRaw(isReply)

    text = res.text[17:-7]
    list = eval(text)
    string = ""
    for i in list[1]:
        string += "%s \n" % i
    return string[:-1]

# TODO: 搜狗百科
def encyclopediasSoGouRealUrl(keyWord):
    url = "https://baike.sogou.com/bapi/searchBarEnter"
    params = {
        "searchText": keyWord,
        "_": "1639367189402",
        "_traceId": "c05fe90f3b6f4ae4aa8418eecd4ca102:6",
    }
    res = requests.get(url, params=params) # res.encoding = "GBK"

    return "https://baike.sogou.com" + res.text
def encyclopediasSoGouRaw(keyWord):
    url = encyclopediasSoGouRealUrl(keyWord)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
    }
    res = requests.get(url, headers=headers) # res.encoding = "GBK"

    text = res.text
    title = re.findall(r'<h1 id="title" data-full-title="(.*?)".*?</h1>', text)
    info = re.findall(r'<[^>]+>', text)

    data = {
        "Title": title,
        "Info": info
    }
    return res, data
@Event.messageGroup()
@Mapping.prefix("搜狗百科")
def encyclopediasSoGou(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")
    
    msg: str = None
    if len(params) == 0: msg = "小晴"
    else: msg = params[0]

    response.text.append(encyclopediasSoGouRaw(msg))
    return True

# TODO: 图片查询
def searchImage(self, keyWord):
    pass

def encyclopediasBaiDuRaw(keyWord):
    result = {
        "status": True, "title": None, "info": None, "msg": None
    }
    url = f"https://baike.baidu.com/item/{keyWord}"
    res = requests.get(url)
    res.encoding = "utf-8"
    resText = res.text

    error = [
        "访问异常，请进行验证", "验证失败，请重新验证"
    ]
    for i in error:
        if i in resText:
            result["status"] = False
            result["msg"] = i
            return result
    
    P_Title = r'<title>(.*?)</title>'
    P_Info = r'\<meta name="description" content="(.*?)"\>'

    result["title"] = re.findall(P_Title, res.text)[0].replace("_百度百科", "")
    result["info"] = re.findall(P_Info, res.text)[0]

    return result
@Event.messageGroup()
@Mapping.prefix("百度百科")
def encyclopediasBaiDu(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    msg: str = None
    if len(params) == 0: msg = "小晴"
    else: msg = params[0]

    data = encyclopediasBaiDuRaw(msg)
    if data["status"] == False:
        response.text.append(data["msg"])
        return True
    
    response.text.append(f"{data['title']} \n{data['info']}")
    return True

def scenicSpotRaw(townName):
    Url = "https://m.ctrip.com/restapi/h5api/globalsearch/search"
    Params = {
        "action": "online",
        "source": "globalonline",
        "keyword": townName,
        "t": time.time(),
    }
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

    res = session.get(Url, params=Params)
    Data = json.loads(res.text)
    Data = Data["data"]

    return res
@Event.messageGroup()
@Mapping.prefix(["查询景点", "景点查询"])
def scenicSpot(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    msg: str = None
    if len(params) == 0: msg = "东莞"
    else: msg = params[0]

    res = scenicSpotRaw(msg)

    Data = json.loads(res.text)["data"]
    string = ""
    for i in Data:
        string += f"{i['word']}: {i['url']} \n"
        # string += "%s \n" % i["districtName"]
        # string += "%s \n" % i["content"]
        # string += "%s \n" % i["price"]
        # string += "%s \n" % i["locationName"]
        # string += "%s \n" % i["starRating"]
        # string += "%s \n" % i["tagNames"]
        # string += "%s \n" % i["address"]
        # string += "%s \n" % i["zoneName"]
        # string += "%s \n" % i["tagNames"]
        # string += "%s \n" % i["brandName"]

    response.text.append(string)
    return True

def weatherTownID(townName:str, timeStamp:str):
    url = "http://toy1.weather.com.cn/search"
    params = {
        "cityname": townName,
        "callback": "success_jsonpCallback",
        "_": timeStamp,
    }
    res = requests.get(url, params=params)

    p = r'^\w+\((.*)\)$'
    JSON = re.findall(p, res.text)[0]
    JSON = json.loads(JSON)
    if len(JSON) > 1:
        Town_ID = JSON[0]["ref"]
        Town_ID = Town_ID.split("~")[0]
    return Town_ID
def weatherRaw(townName:str):
    # 获取时间戳
    timeStamp = f"{int(time.mktime(time.localtime())) + int(random.randint(100, 999))}"

    # 获取城市ID
    townID = weatherTownID(townName, timeStamp)

    # 获取城市天气
    url = "http://d1.weather.com.cn/sk_2d/%s.html" % townID
    url = "http://d1.weather.com.cn/dingzhi/%s.html" % townID
    params = {"_": timeStamp}

    headers = {
        "Referer": "http://www.weather.com.cn/",
        "Host": "d1.weather.com.cn"
    }
    res = requests.get(url, headers=headers, params=params)
    res.encoding = "utf-8"

    text = res.text
    qslb = text.split(";")

    qslb_1 = json.loads(qslb[0].split("=")[-1])
    qslb_2 = json.loads(qslb[1].split("=")[-1])
    return qslb_1,qslb_2
@Event.messageGroup()
@Mapping.prefix(["查询天气", "天气查询"])
def weather(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    msg: str = None
    if len(params) == 0: msg = "东莞"
    else: msg = params[0]

    if msg == "火星":
        response.text.append("""
        没想到你个小呆子还真的想看火星天气!
        火星大气中含有95%的二氧化碳,气压低,加之极度的干燥,就阻止了水的形成积聚。这意味着火星几乎没有云,冰层覆盖了火星的两极,它们的融化和冻结受到火星与太阳远近距离的影响,它产生了强大的尘埃云,阻挡了太阳光,使冰层的融化慢下来。
        所以说火星天气太恶劣了,去过一次就不想再去第二次了
        """.replace("            ",""))
        return True

    try:
        data1, data2 = weatherRaw(msg)
    except:
        response.text.append("格式错误")
        return True
    
    data1 = data1["weatherinfo"]
    string = ""
    string += "[%s天气] \n" % data1["cityname"]
    string += "当前时间: %s \n" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    string += "云层状况: %s \n" % data1["weather"]
    string += "最低气温: %s \n" % data1["tempn"]
    string += "最高气温: %s \n" % data1["temp"]
    string += "风向状况: %s(%s) \n" % (data1["wd"], data1["ws"])
    string += "数据来源: 中央气象台"
    response.text.append(string)
    return True

@Event.messageGroup()
@Mapping.prefix("翻译")
def translate(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    table = {
        "en": "英文",
        "zh": "中文",
        "ice": "冰岛语",
        "ru": "俄语",
    }

    # 这里就不用msg = params[0]了, 比如他们传 hello world 到时候只会翻译hello
    if len(params) == 0:
        response.text.append("缺少参数: language")
        return None
    

    # 获取要翻译文本的语言类型
    langRes = requests.post("https://fanyi.baidu.com/langdetect", json={"query": message})
    langJson: dict = langRes.json()
    lang = langJson.get("lan")
    if table.get(lang) == None:
        response.text.append("该语言暂不支持翻译")
        return None
    
    # 翻译
    response.text.append(f"正在翻译中: {table.get(lang)} -> 中文")
    res = requests.post("https://fanyi.baidu.com/transapi", json={"from":lang, "to":"zh", "source": "txt", "query": message})
    resJson: dict = res.json()

    try:
        result = resJson["result"]
    except:
        response.text.append("获取结果失败")
        return None
    resultJson = decode(result)

    try:
        src = resultJson["src"]
        cont = resultJson["content"]
        cont: dict = cont[0]["mean"][0]["cont"]
        cont = ", ".join(cont.keys())
    except:
        response.text.append("处理JSON时发生了错误")
        return None
    
    response.text.append(f"{src} -> {cont}")
    
    return True

@Event.messageGroup()
@Mapping.prefix("计算")
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

@Event.messageGroup()
@Mapping.all("服务器状态")
def serverStatus(*args, **kwargs):
    response.text.append("该功能暂时下架")
    return True

@Event.messageGroup()
@Mapping.all([".noticeList", "公告列表"])
def noticeList(*args, **kwargs): 
    return False

@Event.messageGroup()
@Mapping.all("查看公告")
def noticeSee(*args, **kwargs): 
    return False

def chooseSongBase(musicName):
    url = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    params = {
        '_': str(time.time()),
        'cv': '4747474',
        'ct': '24',
        'format': 'json',
        'inCharset': 'utf-8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '1',
        'uin': '0',
        'g_tk_new_20200303': '5381',
        'g_tk': '5381',
        'hostUin': '0',
        'is_xml': '0',
        'key': musicName,
    }
    
    res = requests.get(url, params=params, headers={"Referer": "http://y.qq.com"})

    data = json.loads(res.text)

    musics = data["data"]["song"]["itemlist"]
    if len(musics) < 1:
        return "False"
    if len(musics) == 1:
        music = musics[0]
    if len(musics) > 1:
        music = musics[0]
    musicDocid = music["docid"]  # musicId = music["id"]
    musicMid = music["mid"] # musicName = music["name"] musicSinger = music["singer"]

    # url = "https://y.qq.com/n/ryqq/albumDetail/%s" % musicMid    url = "https://y.qq.com/n/ryqq/songDetail/%s" % musicMid
    url = "https://i.y.qq.com/v8/playsong.html?ADTAG=ryqq.songDetail&songmid=%s&songid=%s&songtype=0#webchat_redirect"\
            % (musicMid, musicDocid)

    musicsImage = data["data"]["album"]["itemlist"]
    if len(musics) < 1:
        return "False"
    musicPic = musicsImage[0]["pic"]

    result = {
        "musicDocid":music["docid"],
        "musicMid": music["mid"],
        "musicName": music["name"],
        "musicSinger": music["singer"],
        "musicUrl":url,
        "musicPic":musicPic,
    }
    return result
def chooseSongDownload(musicMid):
    # audio = "http://dl.stream.qqmusic.qq.com/%s.m4a?guid=%s&vkey=%s&uin=&fromtag=66" %\
    #        ("C400"+musicMid, "guid", "vKey")

    # https://dl.stream.qqmusic.qq.com/C400002kFRrU0q6QXD.m4a
    # guid=585592520
    # vkey=1D1D8807B15C4FD832379BBB066A7539B925EAE4871702DBAD76F07390A45533C76069822B874A55A843E0E9C88AFFD27CDD21CB37FC6B4B
    # uin=
    # fromtag=66

    url = "https://u.y.qq.com/cgi-bin/musicu.fcg"
    params = {
        '_': time.time() * 1000,
        'sign': 'zzakgej75pk8w36d82032784bdb9204d99bf6351acb7d',
        "data": '{"req":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7469768631","songmid":["' + musicMid + '"],"songtype":[0],"uin":"1164153961","loginflag":1,"platform":"20"}}}'
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    dataPro = data["req"]["data"]["midurlinfo"][0]

    songmid = dataPro["songmid"]
    filename = dataPro["filename"]
    vkey = dataPro["vkey"]
    purl = dataPro["purl"]
    audio = "http://dl.stream.qqmusic.qq.com/" + dataPro["purl"]

    result = {
        "dlSongMid":songmid,
        "dlFilename": filename,
        "dlVKey": vkey,
        "dlPurl": purl,
        "dlAudio": audio,
    }
    return result
@Event.messageGroup()
@Mapping.prefix("点歌")
def chooseSong(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: musicName")
        return True
    
    musicName = params[0]

    music = chooseSongBase(musicName)
    if music == "False": 
        response.text.append("获取音乐信息失败")
        return False
    musicDocid = music["musicDocid"] # musicId = music["id"]
    musicMid = music["musicMid"]
    musicName = music["musicName"]
    musicSinger = music["musicSinger"]
    musicUrl = music["musicUrl"]
    musicPic = music["musicPic"]

    # TODO: 获取失败还有另外一种方式, 会返回http://dl.stream.qqmusic.qq.com/ 这种情况也是获取失败
    musicDownload = chooseSongDownload(musicMid)
    if musicDownload == "False": 
        response.text.append("获取音乐下载链接失败")
        return False
    musicAudio = musicDownload["dlAudio"]

    #print(musicDownload)

    # data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; [title]" sourceMsgId="0" url="[url]" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="[pic]" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>[title]</title><summary>[singer]</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'''
    data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; [title]" sourceMsgId="0" url="[url]" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="[pic]" src="[audio]" /><title>[title]</title><summary>[singer]</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'''
    data = data.replace("[singer]", musicSinger)
    data = data.replace("[url]", musicUrl)
    data = data.replace("[audio]", musicAudio)
    data = data.replace("[title]", musicName)
    data = data.replace("[pic]", musicPic)
    data = data.replace(",", "&#44;").replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    print(musicAudio)

    result = "[CQ:xml,data=%s]" % data
    response.text.append(result)
    response.text.append(musicAudio)
    return True

@Event.messageGroup()
@Mapping.prefix(["跟我说", "发语音"])
def tellMe(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: word")
        return True
    msg = params[0]

    data = request.data
    switch = False
    #if data["message_type"] == "private":
    #    response.text.append("此功能暂时未开发私聊")
    #    return True
    l = []
    l.append(str(applicationContext.getBootstrap("robot", "admin")))
    if not messageBean.user_id in l:
        response.text.append(f"该功能处于测试阶段, 您({messageBean.user_id})没有权限操作")
        response.text.append(f"白名单: {l}")
        return True
    
    '''
    l = [
        "690293425",
        "871232998",
        "560325915",
    ]
    for i in l:
        if str(data["group_id"]) == i:
            switch = True
    '''

    # 调用方法
    res = CQCode.tts(msg)
    if res == False:return None
    
    response.text.append(res)
    return True

@Event.messageGroup()
@Mapping.prefix(["随机表情", "给我一个脸色"])
def face(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    msg = None
    if len(params) == 0: pass
    else: msg = params[0]

    response.text.append(CQCode.face(msg))
    return True

@Event.messageGroup()
@Mapping.prefix(["戳一戳"])
def poke(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    msg = None

    # TODO: 如果未指定, 那么就随机抽取群友戳一戳
    if len(params) == 0: msg = messageBean.user_id
    else: msg = params[0]

    response.text.append(CQCode.poke(msg))
    return True

@Event.messageGroup()
@Mapping.all("给我点钱")
def giveMeSomeMoney(*args, **kwargs):
    # 来自阿白想要的功能
    n = random.randint(1, 20)
    response.text.append(CQCode.face("158") * n)
    return True

@Event.messageGroup()
@Mapping.prefix(".ra")
def ra(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0:
        response.text.append("缺少参数: event, number")
        return None
    
    res = "[name]进行[event]检定:\nD[number]=[random]/[number] [result]"

    arrayList = message.split(" ")
    if len(arrayList) < 2:
        response.text.append("格式不正确, 请按照这个模板进行使用: .ra 写作业 100")
        return False

    event = arrayList[0]
    number = arrayList[1]
    if number.isalnum()==True:
        number = int(number)
    else:
        response.text.append("参数2不是一个整数或不是一个正数")
        return False
        
    
    ranNumber = random.randint(0, number)
    
    success = ["事件成功", "可能成功", "困难成功", "极难成功"]
    if number < len(success):
        response.text.append("参数2需大于%d" % len(success))
        return False
    
    switch = False
    sp = int(number / len(success))
    if (switch==False and ranNumber<sp):
        successResult = success[3]
        switch = True
    if (switch==False and ranNumber<sp*2):
        successResult = success[2]
        switch = True
    if (switch==False and ranNumber<sp*3):
        successResult = success[1]
        switch = True
    if (switch==False and ranNumber<sp*4):
        successResult = success[0]
    
    res = res.replace("[name]", str(request.data.get("sender").get("nickname")))
    res = res.replace("[event]", event)
    res = res.replace("[number]", str(number))
    res = res.replace("[random]", str(ranNumber))
    res = res.replace("[result]", str(successResult))
    

    response.text.append(res)
    return True
