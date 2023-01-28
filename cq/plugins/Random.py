"""
author:     R
encoding:   utf-8
title:      随机插件
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

import random, requests
from bs4 import BeautifulSoup

# 选择困难症
@Event.messageGroup()
@Mapping.prefix([".helpMeChoose", "帮我选择"])
def helpMeChoose(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    paramsLen = len(params)
    if paramsLen == 0:
        response.text.append("缺少参数")
        return None
    if paramsLen == 1:
        response.text.append("总共1个选择, 就不帮您选啦")
        return None

    result = f"总共{paramsLen}个选择, 已为您选择: {params[random.randint(0, paramsLen-1)]}"
    response.text.append(result)
    return True

# 投掷骰子
@Event.messageGroup()
@Mapping.prefix([".roll", "投掷骰子"])
def roll(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    number = None

    # 如果没有携带参数
    if len(params) == 0: number = 10

    # 如果携带的参数不是正数
    tmp: str = params[0]
    if not tmp.isdigit(): number = 10
    else: number = int(tmp)
    
    # 如果携带的参数过小
    if number <= 0: number = 10

    response.text.append(f"投掷结果为: {random.randint(0, number)}")
    return True


# 随机美食
@Event.messageGroup()
@Mapping.all("随机食物")
def food(*args, **kwargs):
    l = {
        "肠粉":"暂无介绍",
        "瘦肉粥":"暂无介绍",
        "青椒炒肉":"暂无介绍",
        "云吞面":"",
        "煲仔饭":"",
        "蚝皇凤爪":"",
        "花雕鸡":"",
        "白切鸡": "",
        "叉烧包": "",
        "虾饺": "",
        "烧卖": "",
        "烧鹅": "",
        "双皮奶": "",
        "奶黄包": "",
        "流沙包": "",
        "莲蓉包": "",
        "马蹄糕": "",
        "榴莲酥": "",
        "咸水角": "",
        "香芋酥": "",
        "黑椒猪大肠": "",
        "黑椒牛仔骨": "",
        "糯米鸡": "",
        "香芋牛肉球": "",
        "鸳鸯菜": "",
        "艇仔粥": "",
        "皮蛋瘦肉粥": "",
        "梅菜扣肉": "",
    }
    key = list(l)[random.randint(0, len(l)-1)]
    response.text.append(f"[{key}]\n菜品介绍: {l.get(key)}\n星级评价: ...\n简易难度: ...")
    return True

# 随机超能力
@Event.messageGroup()
@Mapping.all("随机超能力")
def superPowers(*args, **kwargs):
    powers = [
        "隐身",
        "瞬间移动",
        "预知未来",
        "成为布鲁斯韦恩",
        "所有副作用无效化",
        "瞬间看透任何事物本质",
        "获得蓝色药丸, 隔着屏幕给插件制作人一巴掌",
        "可以把你的朋友变成双马尾美少女",
        "你可以以观察者的身份，在任意时间空间观察世间万物",
        "你可以模仿一切声音",
        "玩抽卡游戏, 十发以内必中",
        "你可以控制核聚变",
        "你可以不需要睡觉",
        "可以任意切换自己的性别",
    ]

    punishment = [
        "变成未知生物",
        "每五秒窜一次稀",
        "产生多种不同人格",
        "你的智商水平降为6岁水平",
        "你会不受控制地追着狗咬",
        # "你会成为别人的性奴",
        "你必须跑到人多的地方，把超能力名字念出来才会生效",
        "你会变成抖m",
        "你每天起来都会忘记昨天发生的事情",
        "每天必须使用该超能力1000次, 否则能力失效",
        # "牛子缩短50%",
    ]

    v1 = powers[random.randint(0, len(powers)-1)]
    v2 = punishment[random.randint(0, len(punishment)-1)]

    response.text.append(f"您的超能力为: {v1}.\n能力副作用为: {v2}")
    # response.text.append(f"Tips: 提交超能力 一夜之间暴富 但是交税是其他人的100倍")
    return True

@Event.messageGroup()
@Mapping.all("随机诗词")
def poetry(*args, **kwargs):
    url = "https://so.gushiwen.cn/shiwens/default.aspx?"
    params = { "page": "1", "tstr":"", "astr":"", "cstr":"", "xstr":"" }
    res = requests.get(url, params=params)

    soup = BeautifulSoup(res.text, 'html.parser')
    leftZhankai = soup.find_all(id="leftZhankai")
    sons = leftZhankai[0].find_all(class_="sons")

    # TODO: 未成年的缓存方法
    try:
        poetry = applicationContext.poetry
    except:
        poetry = None
    if poetry != None:
        l = list(applicationContext.poetry)
        n = random.randint(0, len(l) - 1)
        title = l[n]
        author = poetry[l[n]]["author"]
        contson = poetry[l[n]]["contson"]
        response.text.append(f"{title}\n{author}\n{contson}\nTips: 已缓存")
        return None

    d = {}
    for i in sons:
        # 标题, 作者/朝代, 诗词
        title = i("b")
        source = i(class_="source")
        contson = i(class_="contson")
        d[title[0].text] = {"author": source[0].text, "contson": contson[0].text.replace("\r\n                    ", "").strip()}
    applicationContext.poetry = d
    l = list(d)
    n = random.randint(0, len(l) - 1)
    title = l[n]
    author = d[l[n]]["author"]
    contson = d[l[n]]["contson"]
    response.text.append(f"{title}\n{author}\n{contson}")

    return True

@Event.messageGroup()
@Mapping.all("随机老婆")
def rollWifeRaw(*args, **kwargs):
    data = [
        "凌波丽", "春日野穹","神尾观铃", "阿尔托利亚·潘德拉贡", "优克莉伍德·海尔赛兹", "立华奏",
        "夏娜", "C.C", "五河琴里", "楪祈", "神崎·H·亚里亚", "椎名真白", "五更琉璃", "桔梗",
        "结城明日奈", "伊卡洛斯", "本间萌衣子", "雨宫优子", "梦梦·贝莉雅·戴比路克", "小樱公主", "木之本樱",
        "赤夜萌香", "时崎狂三", "我妻由乃", "椎名真冬", "古手梨花", "两仪式", "菲莉丝·艾利斯",
        "小鸟游六花", "小日向速水", "凉宫春日", "筒隐月子", "春野樱", "日向雏田", "娜美", "东条希",
    ]
    response.text.append("您上辈子的老婆为: %s" % data[random.randint(0,len(data)-1)])
    return True

@Event.messageGroup()
@Mapping.all("随机老公")
def rollHusbandRaw(*args, **kwargs):
    data = [
        "橘真琴", "罗伊·马斯坦古", "坂田银时", "利威尔·阿克曼", "赤司征十郎", "御幸一也", "风早翔太",
        "维克托·尼基福罗夫", "巴卫", "塞巴斯蒂安", "工藤新一", "宇智波佐助", "索隆", "夏目贵志", "利威尔",
        "碓冰拓海", "五条悟", "塞巴斯蒂安", "杀生丸", "月咏几斗", "孙悟饭", "草壁达郎", "波风水门",
        "藤原滋", "木之本藤隆", "工藤优作", "野原广志", "黑桐干也", "白纯里绪", "影山飞雄"
    ]
    response.text.append("您上辈子的老公为: %s" % data[random.randint(0,len(data)-1)])
    return True

# 概率
def __probability(self, number=10, percentage=2):
    data = {"True" : 0, "False" : 0}
    for i in range(0, number):
        lucky = random.randint(0, 100 * 10) # 概率公式

        if lucky <= percentage * 10:
            data["True"] += 1
        else:
            data["False"] += 1
    return data

# 随机老公/老婆(取自群友)
# 随机老婆/老公(动漫角色)
# 随机事件
# 随机笑话