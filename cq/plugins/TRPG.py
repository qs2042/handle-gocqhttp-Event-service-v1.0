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



