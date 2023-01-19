"""
author:     R
encoding:   utf-8
title:      时间插件
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
import time

@Event.messageGroup()
@Mapping.all(["当前时间", ".time"])
def cruuentTime(*args, **kwargs):
    r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    response.text.append(r)
    return True

@Event.messageGroup()
@Mapping.all("当前时间戳")
def currentTimeStamp(*args, **kwargs):
    r = str(time.time())
    response.text.append(r)
    return True

