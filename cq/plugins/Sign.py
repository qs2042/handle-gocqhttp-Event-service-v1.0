'''
author:     R
encoding:   utf-8
title:      签到插件
version:    1.0
introduce:  顾名思义
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

excludeList = [
    "QQ"
]



@mapping([".sign", "签到"])
def main(*args, **kwargs):
    # 获取QQ号
    print(messageBean.user_id)

    # 获取QQ群
    print(messageBean.group_id)

    # 获取消息
    print(messageBean.message)
    
    # 获取消息
    print(kwargs.get("message"))
    

    # 获取QQ名称 和 QQ群名片
    r = f"@{messageBean.user_nick}({messageBean.user_card}) 恭喜您签到成功"

    # 返回信息
    response.text.append(r)
    return True
