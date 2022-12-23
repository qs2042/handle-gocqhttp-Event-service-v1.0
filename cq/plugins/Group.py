'''
author:     R
encoding:   utf-8
title:      group插件
version:    1.0
introduce:  暂无介绍
functions:  禁我 [number], ...
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
from cq.API import API as RQAPI

rqAPI = RQAPI()

excludeList = [
    "random", "RQAPI", "rqAPI"
]

@mapping("禁我")
def banMe(*args, **kwargs):
    message = kwargs.get("message")
    groupId = messageBean.group_id
    userId = messageBean.user_id

    if groupId == None:
        response.text.append("该功能仅限于群聊使用")
        return True

    time = 0
    try:
        time = int(message)
        if time <= 30: time = 400
    except:
        time = random.randint(30, 240)

    response.text.append(f"已禁言{time}秒")

    rqAPI.setGroupBan(groupId, userId, time)
    return True
