"""
author:     R
encoding:   utf-8
title:      群管插件
version:    1.0
introduce:  无可奉告
functions:  禁我 [number]
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
from cq.API import API as RQAPI

@Event.messageGroup()
@Mapping.prefix("禁我")
def banMe(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    groupId = messageBean.group_id
    userId = messageBean.user_id

    if groupId == None:
        response.text.append("该功能仅限于群聊使用")
        return True
    
    time = None
    if len(params) == 0:
        time = random.randint(30, 240)
    if len(params) >= 1:
        tmp: str = params[0]
        isPositiveInt = tmp.isdigit()
        if isPositiveInt: 
            time = int(tmp)
            if time <= 30: time = 400
        else: 
            time = random.randint(30, 240)

    response.text.append(f"已禁言{time}秒")

    rqAPI = RQAPI()
    rqAPI.setGroupBan(groupId, userId, time)
    return True
