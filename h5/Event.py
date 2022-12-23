from urllib import response
from cv2 import log
from requests import request
from core.Response import Response
from core.Request import Request
from core.MetaMap import MetaMap

from library.Log import Log


class Event:
    def __init__(self, request: Request, response: Response, metaMap: MetaMap) -> None:
        self.request = request
        self.response = response
        self.metaMap = metaMap

        self.log = Log("CQ-Event")


    def main(self):
        # self.log.info(self.request)
        # self.log.info(self.response)
        # self.log.info(self.metaMap)
        pass