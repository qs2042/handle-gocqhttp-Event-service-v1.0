"""
author:     R
encoding:   utf-8
title:      签到插件
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


@Event.messageGroup()
@Mapping.all([".sign", "签到"])
def main(*args, **kwargs):
    print(messageBean)
    print(request)
    # 获取QQ号
    print(messageBean.user_id)

    # 获取QQ群
    print(messageBean.group_id)

    # 获取消息
    print(messageBean.message)

    # 获取QQ名称 和 QQ群名片
    r = f"@{messageBean.user_nick}({messageBean.user_id}) 恭喜您签到成功"

    # 返回信息
    response.text.append(r)
    return True
