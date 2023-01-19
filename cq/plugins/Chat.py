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
    result = data.get(tmp)
    return False if result == None else result

def chatTuLing123(tmp:str):
    url = "http://openapi.tuling123.com/openapi/api/v2"

    apikey = applicationContext.bootstrap.get("tu_ling_apikey")
    if apikey == None or apikey == '': 
        print("您还未填写图灵123的apikey, 无法使用该功能\n")
        return False
    
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

    data = json.loads(res.text)
    
    answer = data["results"][0]["values"]["text"]

    return False if answer == "请求次数超限制!" else answer

def chatQingYunKe(tmp:str):
    url = "http://api.qingyunke.com/api.php"
    params = {
        "key": "free",
        "appid": "0",
        "msg": tmp,
    }
    res = requests.get(url, params=params)
    if res.status_code != 200: return False

    data = json.loads(res.text)

    answer: str = data["content"]

    if type(answer) == str:
        answer.replace("夏夏的宠物", "你的小晴")
        answer.replace("菲菲", "小晴")

    return answer


@Event.messageGroup()
@Mapping.prefix(["#", "聊天"])
def chat(*args, **kwargs):
    kwargs.update(kwargs.get("kv"))

    message = kwargs.get("message")
    if len(message) == 0: return False

    isTrigger = False
    if isTrigger==False: isTrigger = chatThesaurus(message)
    if isTrigger==False: isTrigger = chatTuLing123(message)
    if isTrigger==False: isTrigger = chatQingYunKe(message)
    if isTrigger==False: return None

    response.text.append(isTrigger)
    return True
