"""
author:     R
encoding:   utf-8
title:      屏蔽词插件
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
@Mapping.approved()
def aaa(*args, **kwargs):
    '''
    检测关键词
    TODO: 后续设置一个等级评定, 比如警告, 禁言, 踢出群, 撤回等
    '''
    message = messageBean.message
    l = [
        "下单方法", "长按复制这条信息", "打开手机淘宝", "傻逼", "弱智"
    ]

    re0 = [
            "[0-9]{11}", "[0-9]{10}", "jj",
            "\{face:[0-9]\}|\{face:[0-9]{2}\}|\{face:[0-9]{3}\}",
            "狂撸", "狂射", "9000次", "求草"
            "你就不能搞点新创意出来嘛", "face57","我不是大便，我的粉丝也不是苍蝇",
            "别发这么无聊的信息行不",
        ]

    # '傻逼', '煞笔', '神经病', '母猪', "tianyu" -> 小可爱
    # '菲菲', '浩哥', '小燕', '吴珂', '王雨昕', '茉姐', "杨秀花" -> 小晴
    # "帮群主爽" -> 在写代码
    # "发的什么呀你，乱打的吧", "咱是中国人，请讲中文，谢谢！" -> None

    if True in [i in message for i in l]:
        response.text.append(f"@{messageBean.user_nick}({messageBean.user_id}) 检测到屏蔽词汇")
        return True
    
    return None
