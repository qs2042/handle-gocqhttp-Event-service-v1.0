'''
author:     R
encoding:   utf-8
title:      随机插件
version:    1.0
introduce:  解决你的选择困难症
functions:  帮我选择 [args...], 投掷骰子 [number], 随机美食
time:       2022年11月15日15时34分27秒
'''
from library.Decorator import mapping
from core.Request import Request
from core.Response import Response
from core.MetaMap import MetaMap
from core.ApplicationContext import ApplicationContext
from cq.core.MessageBean import MessageBean

request: Request = None
response: Response = None
metaMap: MetaMap = None
applicationContext: ApplicationContext = None
messageBean: MessageBean = None


import random
excludeList = [
    "random"
]



# 选择困难症
@mapping([".helpMeChoose", "帮我选择"])
def helpMeChoose(*args, **kwargs):
    message:str = kwargs.get("message")
    if (len(message) == 0):
        response.text.append("指令缺少参数, 正确格式请参照文档: null")
        return None

    l = message.split(" ")
    if (len(l) == 1):
        response.text.append("总共1个选择, 就不帮您选啦") 
        return None

    r = "总共%d个选择, 已为您选择: %s" % (len(l), l[random.randint(0, len(l)-1)])
    response.text.append(r)
    return True

# 投掷骰子
@mapping([".roll", "投掷骰子"])
def roll(*args, **kwargs):
    message:str = kwargs.get("message")
    print(message)
    print(len(message))
    print(message.isspace())

    if len(message) == 0 or not message.isdigit():
        response.text.append(f"投掷结果为: {random.randint(0, 10)}")
        return True

    number = int(message)
    if number<=0: 
        response.text.append(f"投掷结果为: {random.randint(0, 10)}")
        return True

    response.text.append(f"投掷结果为: {random.randint(0, number)}")
    return True


# 随机美食
@mapping(value="随机食物")
def food(*args, **kwargs):
    l = {
        "肠粉":"暂无介绍",
        "瘦肉粥":"暂无介绍",
        "青椒炒肉":"暂无介绍",
    }
    key = list(l)[random.randint(0, len(l)-1)]
    response.text.append([key, l[key]])
    return True

# 随机老公/老婆(取自群友)
# 随机老婆/老公(动漫角色)
# 随机超能力
# 随机事件
# 随机笑话