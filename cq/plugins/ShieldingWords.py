'''
author:     R
encoding:   utf-8
title:      屏蔽词插件
version:    1.0
introduce:  用于双向屏蔽不雅词汇
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

excludeList = []


def main(*args, **kwargs):
    message = request.data.get('message')
    # TODO: 后续设置一个等级评定, 比如警告, 禁言, 踢出群, 撤回等
    l = [
        "下单方法", "长按复制这条信息", "打开手机淘宝", "傻逼", "弱智"
    ]

    if True in [i in message for i in l]:
        response.text.append(f"@{messageBean.user_nick} 检测到屏蔽词汇")
        return True
    
    return None
