'''
author:     R
encoding:   utf-8
title:      测试插件
version:    1.0
introduce:  各种奇奇怪怪的功能都会塞这里面
time:       2022年11月16日21:28:58
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

import time

excludeList = [
    "time"
]



# 测试
@mapping(value = ["helloWorld"])
def test(*args, **kwargs):
    # request: conn, url, headers, data
    # response: ...
    # metaMap: ...
    # applicationContext: 插件, 库, 基本信息
    # messageBean: 包装过后的数据
    print(f"""
    原始数据: {request}\n
    返回数据: {response}\n
    元数据: {metaMap}\n
    上下文: {applicationContext}\n
    消息类: {messageBean}\n
    """.strip())
    response.text.append("hello World!")
    return True

@mapping("测试视频")
def testVideo(*args, **kwargs):
    time.sleep(5)
    response.text.append("(假装是加载了5s的网络视频)")
    return True

@mapping("测试图片")
def testImage(*args, **kwargs):
    time.sleep(5)
    response.text.append("(假装是加载了5s的网络图片)")
    return True

