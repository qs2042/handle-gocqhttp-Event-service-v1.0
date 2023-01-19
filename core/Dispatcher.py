# 核心代码
from core.Response import Response
from core.Request import Request

# context
from core.RequestContext import RequestContext
from core.SessionContext import SessionContext
from core.ApplicationContext import ApplicationContext

import threading

from cq.Event import Event as CQEvent
from h5.Event import Event as H5Event

from library.SocketUtil import SocketUtil
import base64

from library.Decorator import Utils

def picture2base(path):
    # 开启流
    img = open(path, "rb")

    # 使用base64进行编码
    b64encode = base64.b64encode(img.read())
    result = f"data:image/jpeg;base64,{b64encode.decode()}"

    # 关闭流
    img.close()

    # 返回base64编码字符串
    return result.encode()

class Dispatcher():
    def __init__(self, request: Request, requestContext: RequestContext, sessionContext: SessionContext, applicationContext: ApplicationContext) -> Response:
        self.request = request
        self.requestContext = requestContext
        self.sessionContext = sessionContext
        self.applicationContext = applicationContext
        self.response = Response()

    def cq(self):
        # 判断是否为CQ请求
        if not "CQHttp" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.requestContext.isTriggerModule = "CQ"
        
        # 开启子线程
        run = CQEvent(self.request, self.response, self.requestContext, self.sessionContext, self.applicationContext).main
        threading.Thread(target=run).start()

    def cqTest(self):
        # 判断是否为CQ请求
        if not "Test" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.requestContext.isTriggerModule = "CQTest"

        # 开启子线程
        CQEvent(self.request, self.response, self.requestContext, self.sessionContext, self.applicationContext).main()

    def h5(self):
        # 判断是否为H5请求
        if not "AppleWebKit" in self.request.headers["User-Agent"]: return None
        
        # 成功触发功能
        self.requestContext.isTriggerModule = "H5"

        # 判断是否为网站头像请求
        if (self.request.url == "/favicon.ico"):
            # 不打印日志
            self.requestContext.isLog = False

            # 设置为图片模式
            self.response.modeImage("favicon.ico")

            # 加载图片
            #with open(r"static/round.jpeg", "rb") as f:
            #    img = f.read()

            img = picture2base(r"static/round.jpeg")

            # 返回数据
            self.response.text.append(img)
            print(img)
            print(f"{img}"[1:-1])
            print(self.response.result())
            print("\n\n\n")

            SocketUtil.sendAll(self.request, self.response)
            # SocketUtil.close(self.request)
            return None

        # TODO: 开启子线程
        H5Event(self.request, self.response, self.requestContext).main()

    def main(self):
        if self.requestContext.isTriggerModule == False: self.cq()
        if self.requestContext.isTriggerModule == False: self.cqTest()
        if self.requestContext.isTriggerModule == False: self.h5()

        return self.response