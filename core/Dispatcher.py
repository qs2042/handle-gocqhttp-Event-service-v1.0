# 核心代码
from core.Response import Response
from core.Request import Request
from core.MetaMap import MetaMap
from core.ApplicationContext import ApplicationContext

from library.Log import Log
import threading, asyncio

from cq.Event import Event as CQEvent
from h5.Event import Event as H5Event

from tools.SocketUtil import SocketUtil

def picture2base(path):
    import base64
    img = open(path, "rb")

    # 使用base64进行编码
    b64encode = base64.b64encode(img.read())
    result = f"data:image/jpeg;base64,{b64encode.decode()}"
    img.close()

    # 返回base64编码字符串
    return result.encode()

class Dispatcher():
    def __init__(self, request: Request, metaMap: MetaMap, applicationContext: ApplicationContext) -> Response:
        self.request = request
        self.metaMap = metaMap
        self.applicationContext = applicationContext
        self.response = Response()

    def cq(self):
        # 判断是否为CQ请求
        if not "CQHttp" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.metaMap.isTriggerModule = "CQ"
        
        # 开启子线程
        run = CQEvent(self.request, self.response, self.metaMap, self.applicationContext).main
        threading.Thread(target=run).start()

        # 返回数据
        SocketUtil.sendAll(self.request, self.response)

    def cqTest(self):
        # 判断是否为CQ请求
        if not "Test" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.metaMap.isTriggerModule = "CQTest"

        # 开启子线程
        CQEvent(self.request, self.response, self.metaMap, self.applicationContext).main()

        # 返回数据
        SocketUtil.sendAll(self.request, self.response)

    def h5(self):
        # 判断是否为H5请求
        if not "AppleWebKit" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.metaMap.isTriggerModule = "H5"

        # 判断是否为网站头像请求
        if (self.request.url == "/favicon.ico"):
            # 不打印日志
            self.metaMap.isLog = False

            # 设置为图片模式
            self.response.modeImage("favicon.ico")

            # 加载图片
            #with open(r"static/round.jpeg", 'rb') as fp:
            #    self.response.text.append(fp.read())
            self.response.text.append(picture2base("static/round.jpeg"))

            return None

        # TODO: 开启子线程
        H5Event(self.request, self.response, self.metaMap).main()

        # 返回数据
        SocketUtil.sendAll(self.request, self.response)



    def main(self):
        if self.metaMap.isTriggerModule == False: self.cq()
        if self.metaMap.isTriggerModule == False: self.cqTest()
        if self.metaMap.isTriggerModule == False: self.h5()

        return self.response