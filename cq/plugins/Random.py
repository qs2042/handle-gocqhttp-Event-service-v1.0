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

import random

# 选择困难症
@Event.messageGroup()
@Mapping.prefix([".helpMeChoose", "帮我选择"])
def helpMeChoose(*args, **kwargs):
    kwargs: dict = kwargs.get("kv")
    if type(kwargs) != dict: 
        response.text.append("出现未知错误")
        return None
    
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
@Event.messageGroup()
@Mapping.prefix([".roll", "投掷骰子"])
def roll(*args, **kwargs):
    kwargs: dict = kwargs.get("kv")
    if type(kwargs) != dict: 
        response.text.append("出现未知错误")
        return None

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
@Event.messageGroup()
@Mapping.all("随机食物")
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