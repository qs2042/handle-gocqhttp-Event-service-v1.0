'''
author:     R
encoding:   utf-8
title:      GPT插件
version:    1.0
introduce:  https://gpt.chatapi.art/
functions:  AI [message]
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

import requests, datetime, json
from cq.API import API as RQAPI
rqAPI = RQAPI()

excludeList = [
    "requests", "datetime", "json",
    "rqAPI", "RQAPI"
]

def _GPT(InPut):
    api = "https://gpt.chatapi.art/backend-api/conversation"
    headers = {
        "authority": "gpt.chatapi.art",
        "method": "POST",
        "path": "/backend-api/conversation",
        "scheme": "https",
        "accept": "text/event-stream", # */*
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorization": "Bearer",
        "content-length": "236", # 298
        "content-type": "application/json",
        "origin": "https://gpt.chatapi.art",
        "referer": "https://gpt.chatapi.art/",
        "sec-ch-ua": """Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108""",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
        "If-Modified-Since": f"Tue, 28 Jan 2020 12:{datetime.datetime.now().minute}:{datetime.datetime.now().second} GMT",
        "cookie": "cf_chl_2=83f525eb2272168; cf_clearance=O.03dK3l.TYRtnldkQodlj5GJDUadY4EoFrDxxBMBvM-1670811551-0-150"
    }

    Json = {
        "action": "next",
        "messages": [{
            "id": "a2e292a1-59cc-4fca-81ed-5a8f8458f1be",
            "role": "user",
            "content": {"content_type": "text", "parts": [InPut]}
        }],
        "parent_message_id": "be81a331-eacf-45fd-bc47-6a6375ab2335",
        "model": "text-davinci-002-render"
    }

    RES = ""

    r = requests.post(api, json=Json, headers=headers)
    data = r.text.replace("data: ", "")
    
    lis0 = data.split("\n")

    for i in lis0[::-1]:
        if i and i != '[DONE]':
            RES = i
            break

    try:
        return json.loads(RES)['message']['content']['parts'][0]
    except:
        print(r.status_code)
        print(r.text)
        return False

@mapping("AI")
def ai(*args, **kwargs):
    # 获取截取指令后的参数
    text = kwargs.get('message')

    # 数据校验
    if len(text) <= 1: return response.text.append("参数不可小于等于1")

    # 使用API主动发送消息
    rqAPI.sendMessage(messageBean.raw_data.get("message_type"), messageBean.user_id, messageBean.group_id, "该功能需要等待1~2分钟")

    # 功能
    r = _GPT(text)

    # 将消息交给框架统一进行发送
    if r == False: response.text.append("出现网络错误, 请过会重新尝试")
    if r != False: response.text.append(r)

    # None=未触发前缀(当前请求继续执行其他插件方法)
    # True=执行成功(当前请求不再执行其他插件方法)
    # False=执行失败(当前请求继续执行其他插件方法)
    return True
