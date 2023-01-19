"""
author:     R
encoding:   utf-8
title:      框架
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

from library.PythonUtil import PythonUtil


@Event.messageGroup()
@Mapping.all([".help", "功能列表"])
def functionList(*args, **kwargs):
    plugins = applicationContext.plugins.get("cq")
    s = ""
    for i,plugin in enumerate(plugins):
        data:dict = PythonUtil.analysisDoc(plugin.__doc__)
        s += f"{i+1}.{data.get('title')}v{data.get('version')} ({data.get('author')}) \n"
    response.text.append(s[:-1])
    return True

@Event.messageGroup()
@Mapping.prefix("查看功能")
def functionSee(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))

    title = kwargs.get("message")

    plugins = applicationContext.plugins.get("cq")
    for plugin in plugins:
        data:dict = PythonUtil.analysisDoc(plugin.__doc__)
        if title == data.get("title"):
            response.text.append(f"已为您获取{title}功能的介绍")
            response.text.append(f"[{title}]\n作者:{data.get('author')}\n介绍:{data.get('introduce')}\n功能列表:{data.get('functions')}")
    
    if len(response.text) == 0:
        response.text.append(f"{title}功能不存在, 请重新输入")

