"""
author:     R
encoding:   utf-8
title:      R的垃圾桶
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

import requests, time, json, random
from cq.CQCode import CQCode


@Event.messageGroup()
@Mapping.all("服务器状态")
def serverStatus(*args, **kwargs):
    response.text.append("该功能暂时下架")
    return True

# 公告列表/查看
@Event.messageGroup()
@Mapping.all([".noticeList", "公告列表"])
def noticeList(*args, **kwargs): 
    return False

@Event.messageGroup()
@Mapping.all("查看公告")
def noticeSee(*args, **kwargs): 
    return False


def chooseSongBase(musicName):
    url = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    params = {
        '_': str(time.time()),
        'cv': '4747474',
        'ct': '24',
        'format': 'json',
        'inCharset': 'utf-8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '1',
        'uin': '0',
        'g_tk_new_20200303': '5381',
        'g_tk': '5381',
        'hostUin': '0',
        'is_xml': '0',
        'key': musicName,
    }
    
    res = requests.get(url, params=params, headers={"Referer": "http://y.qq.com"})

    data = json.loads(res.text)

    musics = data["data"]["song"]["itemlist"]
    if len(musics) < 1:
        return "False"
    if len(musics) == 1:
        music = musics[0]
    if len(musics) > 1:
        music = musics[0]
    musicDocid = music["docid"]  # musicId = music["id"]
    musicMid = music["mid"] # musicName = music["name"] musicSinger = music["singer"]

    # url = "https://y.qq.com/n/ryqq/albumDetail/%s" % musicMid    url = "https://y.qq.com/n/ryqq/songDetail/%s" % musicMid
    url = "https://i.y.qq.com/v8/playsong.html?ADTAG=ryqq.songDetail&songmid=%s&songid=%s&songtype=0#webchat_redirect"\
            % (musicMid, musicDocid)

    musicsImage = data["data"]["album"]["itemlist"]
    if len(musics) < 1:
        return "False"
    musicPic = musicsImage[0]["pic"]

    result = {
        "musicDocid":music["docid"],
        "musicMid": music["mid"],
        "musicName": music["name"],
        "musicSinger": music["singer"],
        "musicUrl":url,
        "musicPic":musicPic,
    }
    return result
def chooseSongDownload(musicMid):
    # audio = "http://dl.stream.qqmusic.qq.com/%s.m4a?guid=%s&vkey=%s&uin=&fromtag=66" %\
    #        ("C400"+musicMid, "guid", "vKey")

    # https://dl.stream.qqmusic.qq.com/C400002kFRrU0q6QXD.m4a
    # guid=585592520
    # vkey=1D1D8807B15C4FD832379BBB066A7539B925EAE4871702DBAD76F07390A45533C76069822B874A55A843E0E9C88AFFD27CDD21CB37FC6B4B
    # uin=
    # fromtag=66

    url = "https://u.y.qq.com/cgi-bin/musicu.fcg"
    params = {
        '_': time.time() * 1000,
        'sign': 'zzakgej75pk8w36d82032784bdb9204d99bf6351acb7d',
        "data": '{"req":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7469768631","songmid":["' + musicMid + '"],"songtype":[0],"uin":"1164153961","loginflag":1,"platform":"20"}}}'
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    dataPro = data["req"]["data"]["midurlinfo"][0]

    songmid = dataPro["songmid"]
    filename = dataPro["filename"]
    vkey = dataPro["vkey"]
    purl = dataPro["purl"]
    audio = "http://dl.stream.qqmusic.qq.com/" + dataPro["purl"]

    result = {
        "dlSongMid":songmid,
        "dlFilename": filename,
        "dlVKey": vkey,
        "dlPurl": purl,
        "dlAudio": audio,
    }
    return result

@Event.messageGroup()
@Mapping.prefix("点歌")
def chooseSong(*args, **kwargs):
    try:
        musicName = kwargs["kv"]["message"]
    except:
        response.text.append("缺少音乐名")
        return None

    music = chooseSongBase(musicName)
    if music == "False": 
        response.text.append("获取音乐信息失败")
        return False
    musicDocid = music["musicDocid"] # musicId = music["id"]
    musicMid = music["musicMid"]
    musicName = music["musicName"]
    musicSinger = music["musicSinger"]
    musicUrl = music["musicUrl"]
    musicPic = music["musicPic"]

    musicDownload = chooseSongDownload(musicMid)
    if musicDownload == "False": 
        response.text.append("获取音乐下载链接失败")
        return False
    musicAudio = musicDownload["dlAudio"]

    #print(musicDownload)

    # data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; [title]" sourceMsgId="0" url="[url]" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="[pic]" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>[title]</title><summary>[singer]</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'''
    data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; [title]" sourceMsgId="0" url="[url]" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="[pic]" src="[audio]" /><title>[title]</title><summary>[singer]</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'''
    data = data.replace("[singer]", musicSinger)
    data = data.replace("[url]", musicUrl)
    data = data.replace("[audio]", musicAudio)
    data = data.replace("[title]", musicName)
    data = data.replace("[pic]", musicPic)
    data = data.replace(",", "&#44;").replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    print(musicAudio)

    result = "[CQ:xml,data=%s]" % data
    response.text.append(result)
    return True

@Event.messageGroup()
@Mapping.prefix(["跟我说", "发语音"])
def tellMe(*args, **kwargs):
    try:
        result = kwargs["kv"]["message"]
        if result == "":
            response.text.append("缺少关键词")
            return None
    except:
        response.text.append("未知错误")
        return None

    data = request.data
    switch = False
    #if data["message_type"] == "private":
    #    response.text.append("此功能暂时未开发私聊")
    #    return True
    l = []
    l.append(applicationContext.bootstrap.get("admin"))
    l.append("2042136767")
    if not str(data["user_id"]) in l:
        response.text.append("该功能处于测试阶段, 您没有权限操作")
        return True
    
    '''
    l = [
        "690293425",
        "871232998",
        "560325915",
    ]
    for i in l:
        if str(data["group_id"]) == i:
            switch = True
    '''

    # 调用方法
    res = CQCode.tts(result)
    if res == False:return None
    
    response.text.append(res)
    return True

@Event.messageGroup()
@Mapping.prefix(["随机表情", "给我一个脸色"])
def face(*args, **kwargs):
    try:
        result = kwargs["kv"]["message"]
    except:
        response.text.append("未知错误")
        return None

    # 调用方法
    res = CQCode.face(result)
    if res == False:return res
    
    response.text.append(res)
    return True

@Event.messageGroup()
@Mapping.prefix(["戳一戳"])
def poke(*args, **kwargs):
    try:
        result = kwargs["kv"]["message"]
        # TODO: 如果未指定, 那么就随机抽取群友戳一戳
        if result == "":
            response.text.append("未指定一位好友")
            return None
    except:
        response.text.append("未知错误")
        return None

    # 调用方法
    res = CQCode.poke(result)
    if res == False:return res
    
    response.text.append(res)
    return True

@Event.messageGroup()
@Mapping.prefix("给我点钱")
def giveMeSomeMoney(*args, **kwargs):
    # 来自阿白想要的功能
    n = random.randint(1, 20)
    response.text.append(CQCode.face("158") * n)
    return True


@Event.messageGroup()
@Mapping.prefix(".ra")
def ra(*args, **kwargs):
    try:
        result = kwargs["kv"]["message"]
    except:
        response.text.append("未知错误")
        return None
    
    # 调用方法
    res = "[name]进行[event]检定:\nD[number]=[random]/[number] [result]"

    arrayList = result.split(" ")
    if len(arrayList) < 2:
        response.text.append("格式不正确, 请按照这个模板进行使用: .ra 写作业 100")
        return False

    event = arrayList[0]
    number = arrayList[1]
    if number.isalnum()==True:
        number = int(number)
    else:
        response.text.append("参数2不是一个整数或不是一个正数")
        return False
        
    
    ranNumber = random.randint(0, number)
    
    success = ["事件成功", "可能成功", "困难成功", "极难成功"]
    if number < len(success):
        response.text.append("参数2需大于%d" % len(success))
        return False
    
    switch = False
    sp = int(number / len(success))
    if (switch==False and ranNumber<sp):
        successResult = success[3]
        switch = True
    if (switch==False and ranNumber<sp*2):
        successResult = success[2]
        switch = True
    if (switch==False and ranNumber<sp*3):
        successResult = success[1]
        switch = True
    if (switch==False and ranNumber<sp*4):
        successResult = success[0]
    
    res = res.replace("[name]", str(request.data.get("sender").get("nickname")))
    res = res.replace("[event]", event)
    res = res.replace("[number]", str(number))
    res = res.replace("[random]", str(ranNumber))
    res = res.replace("[result]", str(successResult))
    

    response.text.append(res)
    return True
