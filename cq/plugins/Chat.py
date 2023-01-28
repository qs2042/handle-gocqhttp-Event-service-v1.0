"""
author:     R
encoding:   utf-8
title:      聊天插件
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

import requests, json


# 聊天(本地词库, 图灵123, 青云客)
def chatThesaurus(tmp:str):
    data = {
        "早":"早啊,祝你今天愉快!",
        "中午好": "中午好,吃午饭没呀",
        "晚上好": "晚上好,我去睡觉觉啦",
    }
    return data.get(tmp)

def chatTuLing123(tmp:str):
    url = "http://openapi.tuling123.com/openapi/api/v2"

    apikey = applicationContext.getBootstrap("chat", "tu_ling_api_key")
    if apikey == None or apikey == '': 
        print("您还未填写图灵123的apikey, 无法使用该功能\n")
        return None
    
    params = {
        "reqType": "0",
        "perception": {
            "inputText": {
                "text": tmp,
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": "5",
        },
    }
    
    res = requests.post(url, data=json.dumps(params))
    if res.status_code != 200: return None

    data = json.loads(res.text)
    
    answer = data["results"][0]["values"]["text"]

    return None if answer == "请求次数超限制!" else answer

def chatQingYunKe(tmp:str):
    url = "http://api.qingyunke.com/api.php"
    params = {
        "key": "free",
        "appid": "0",
        "msg": tmp,
    }
    res = requests.get(url, params=params)
    if res.status_code != 200: return None

    data = json.loads(res.text)

    answer: str = data["content"]

    # TODO: 这里聊天词替换
    if type(answer) == str:
        answer = answer.replace("夏夏的宠物", "你的小晴")
        answer = answer.replace("菲菲", "小晴")
        answer = answer.replace("吴珂", "小晴")

    return answer


@Event.messageGroup()
@Mapping.prefix(["#", "聊天"])
def chat(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))
    message: str = kwargs.get("message")
    params: list = kwargs.get("params")

    if len(params) == 0: 
        response.text.append("缺少参数")
        return False
    
    msg = params[0]
    result = None

    if result==None: result = chatThesaurus(msg)
    if result==None: result = chatTuLing123(msg)
    if result==None: result = chatQingYunKe(msg)
    if result==None: return None

    response.text.append(result)
    return True
