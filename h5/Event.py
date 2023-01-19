from urllib import response
from core.Response import Response
from core.Request import Request

# context
from core.RequestContext import RequestContext
from core.SessionContext import SessionContext
from core.ApplicationContext import ApplicationContext

from library.Log import Log
from library.SocketUtil import SocketUtil


class Event:
    def __init__(self, request: Request, response: Response, requestContext: RequestContext) -> None:
        self.request = request
        self.response = response
        self.requestContext = requestContext

        self.log = Log("CQ-Event")


    def main(self):
        # self.log.info(self.request)
        # self.log.info(self.response)
        # self.log.info(self.requestContext)
        
        # 返回数据
        SocketUtil.sendAll(self.request, self.response)