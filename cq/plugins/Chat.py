'''
author:     R
encoding:   utf-8
title:      聊天插件
version:    1.0
introduce:  机器人主动聊天 + 被动聊天
functions:  [本地词库, 图灵123, 青云客]
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


import requests, json
excludeList = [
    "requests", "json",
    "chatThesaurus", "chatTuLing123", "chatQingYunKe"
]


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

    answer = data["content"]

    return answer



# 聊天
@mapping(value = ["#", "聊天"])
def chat(*args, **kwargs):
    message = kwargs.get("message")
    if len(message) == 0: return None
    isTrigger = False

    if isTrigger==False: isTrigger = chatThesaurus(message)
    if isTrigger==False: isTrigger = chatTuLing123(message)
    if isTrigger==False: isTrigger = chatQingYunKe(message)
    if isTrigger==False: return None

    response.text.append(isTrigger)
    return True
