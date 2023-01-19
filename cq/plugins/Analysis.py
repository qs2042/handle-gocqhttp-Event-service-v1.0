"""
author:     R
encoding:   utf-8
title:      解析插件
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
import re, requests, json



# 解析哔哩哔哩: 几年前写的, 已经不能用了. 有时间再修复
def _analysisBiliBiliJSON(BV, AV):
    url = "https://api.bilibili.com/x/v2/reply/main"
    params = {
        "callback":"jQuery17204877570012846435_1646906954364",
        "jsonp":"jsonp",
        "next":"0",
        "type":"1",
        "oid":AV,
        "mode":"3",
        "plat":"1",
        "_":"1646907161286",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "referer":f"https://www.bilibili.com/video/{BV}?p=1&share_medium=android&share_plat=android&share_source=COPY&share_tag=s_i&timestamp=1646905753&unique_k=6LzhAFb"
    }
    res = requests.get(url, params=params)
    if (res.status_code != 200): raise Exception("请求报错")
    text = res.text
    data = json.loads(text[text.index("{"):-1])

    replies = data["data"]["replies"]
    number = 0
    result = ""
    for i in replies:
        if number >= 3:
            break
        result += "%s(%s): %s\n" % (i["member"]["uname"], i["member"]["mid"], i["content"]["message"])
        number += 1
    return result[:-1]
def _analysisBiliBiliRe(pattern, text):
    result = re.findall(pattern, text)
    if len(result) == 0:
        return "False"
    if len(result) > 1:
        return result[0]
    return result[0]

def analysisBiliBili(*args, **kwargs):
    '''
    # url = re.findall("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", text)
    # url = re.findall("https://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", text)
    '''
    # 获取文本
    text = request.data.get("message")

    # 从文本中查看是否有哔哩哔哩的链接
    urls = re.findall("https://b23[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", text)
    if len(urls) == 0: return False
    
    # 从链接中获取BV和AV
    res = requests.get(urls[0])
    text = res.text
    BV = _analysisBiliBiliRe('content="https://www.bilibili.com/video/(.*?)/"', text)
    AV = _analysisBiliBiliRe('"aid":(.*?),', text)
    
    keywords = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="keywords" name="keywords" content="(.*?)">', text)
    description = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="description" name="description" content="(.*?)"', text)
    if description == "False":
        description = _analysisBiliBiliRe('<span class="desc-info-text">(.*?)</span>', text)

    author = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="author" name="author" content="(.*?)">', text)
    mid = _analysisBiliBiliRe('"mid":(.*?),', text)
    
    
    title = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="name" name="title" content="(.*?)">', text)
    if title != False:
        title = title.replace("_哔哩哔哩_bilibili", "")

    url = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="url" content="(.*?)">', text)
    image = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="image" content="(.*?)">', text)
    thumbnailUrl = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="thumbnailUrl" content="(.*?)">', text)
    
    uploadDate = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="uploadDate" content="(.*?)">', text)
    datePublished = _analysisBiliBiliRe('<meta data-vue-meta="true" itemprop="datePublished" content="(.*?)">', text)

    #download = self.analysisBiliBiliRe('"base_url":"(.*?)"', text)

    ''
    result = "[%s]\n" % urls[0]
    #if image != False:result += "%s\n" % CQCode.image(image)
    result += "BV: %s\n" % BV
    result += "AV: %s\n" % AV
    result += "UP: %s(%s)\n" % (author, mid)
    result += "[Image]\n%s\n" % image
    result += "[Title]\n%s\n" % title
    result += "[Description]\n%s\n" % description
    result += "[Upload]\n%s\n" % uploadDate
    result += "[Published]\n%s\n" % datePublished
    # TODO: 这里出BUG了, 懒得修复
    # result += "[replies]\n%s" % _analysisBiliBiliJSON(BV, AV)
    result = f'''
    [BV/AV] {BV}/{AV}
    [作者] {author}({mid})
    [封面] {image}
    [标题] {title}
    [介绍] {description}
    [上传时间] {uploadDate}
    [发布时间] {datePublished}

    '''.replace("        ", "")

    response.text.append(result)
    return True
    