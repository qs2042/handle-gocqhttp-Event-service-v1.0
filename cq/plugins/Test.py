"""
author:     R
encoding:   utf-8
title:      测试插件
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

# 自动注入(不会使用的话, 可以使用print函数, 将下面的变量打印出来)
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

import time



# 测试
@Event.messageGroup()
@Mapping.all(".test")
def test(*args, **kwargs):
    print(f"request: {request}\n")
    print(f"response: {response}\n")
    print(f"messageBean: {messageBean}\n")
    print(f"requestContext: {requestContext}\n")
    print(f"sessionContext: {sessionContext}\n")
    print(f"applicationContext: {applicationContext}\n")
    response.text.append(".test: 测试成功")
    return True

# 测试@Mapping.all
@Meta.order(0)
@Meta.jurisdiction(0)
@Event.messageGroup()
@Mapping.all(".testA")
def testAll(*args, **kwargs):
    response.text.append(".testA: 测试成功")
    return True

# 测试@Mapping.prefix
@Meta.order(0)
@Meta.jurisdiction(0)
@Event.messageGroup()
@Mapping.prefix(".testP")
def testPrefix(*args, **kwargs):
    response.text.append(".testPrefix: 测试成功")
    return True


# 测试多线程(加载视频)
@Event.messageGroup()
@Mapping.all(".testV")
def testVideo(*args, **kwargs):
    print("start: 加载视频中")
    time.sleep(5)

    response.text.append("(假装是加载了5s的网络视频)")

    print("end: 加载完视频")
    return True

# 测试多线程(加载图片)
@Event.messageGroup()
@Mapping.all(".testI")
def testImage(*args, **kwargs):
    print("start: 加载视频中")
    time.sleep(5)

    response.text.append("(假装是加载了5s的网络图片)")

    print("end: 加载完视频")
    return True




'''
@Meta.order(0)
@Meta.jurisdiction(0)
@Event.messageGroup()
@Mapping.approved()
def t1(*args, **kwargs):
    response.text.append(".t1: 测试成功")
    return None

@Meta.order(0)
@Meta.jurisdiction(0)
@Event.messageGroup()
@Mapping.approved()
def t2(*args, **kwargs):
    response.text.append(".t2: 测试成功")
    return True
'''
