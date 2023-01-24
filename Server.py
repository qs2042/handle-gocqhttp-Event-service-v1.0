####################################################
# library
####################################################
# base
import importlib
import json
import os

# context
from core.RequestContext import RequestContext
from core.SessionContext import SessionContext
from core.ApplicationContext import ApplicationContext
# 
from core.Dispatcher import Dispatcher
# utils
from library.Log import Log
from library.Counter import Counter
from library.SocketUtil import SocketUtil
from library.PythonUtil import PythonUtil
from library.StringUtil import StringUtil


####################################################
# Variable
####################################################
IP = "127.0.0.1"
PORT = 5701
BUFSIZE = 4096


def printInfo():
    print(f"""
{'='*30}
欢迎使用RQ框架
{'='*30}
author: R
version: v1.0
encoding: utf-8
introduce: 此项目基于gocqhttp(https://github.com/Mrs4s/go-cqhttp)
createTime: 2022-10-8 15:41:59
{'='*30}
    """.strip())


####################################################
# Main
####################################################
class Server:
    def __init__(self) -> None:
        # 初始化socket对象
        self.listenSocket = SocketUtil.getSocket(IP, PORT)

        # ...
        self.log = Log("server")
        self.counter = Counter()

    def __loadContainer(self) -> None:
        '''
        request         当前请求后销毁
        session         指定某时间销毁
        application     程序关闭后销毁
        '''
        # 容器(request, session, application)
        self.requestContext = RequestContext()
        self.sessionContext = SessionContext()
        self.applicationContext = ApplicationContext()

    def __loadPluings(self) -> None:
        cq: list = os.listdir(self.applicationContext.basePath + r"/cq/plugins")
        h5: list = os.listdir(self.applicationContext.basePath + r"/h5/plugins")

        for i in cq:
            # 如果后缀不是py, 那就直接跳过
            if not StringUtil.equals(i, "py", 2): continue

            # 获取插件名称
            pluginName = StringUtil.splitToString(i)

            # 动态导入插件
            # plugin = importlib.import_module(".", f"cq.plugins.{pluginName}")
            plugin = importlib.import_module(f"cq.plugins.{pluginName}")

            # 解析插件信息
            pluginInfo = PythonUtil.analysisDoc(plugin.__doc__)
            print(f"正在加载CQ插件: {pluginInfo.get('title')}v{pluginInfo.get('version')} ({pluginInfo.get('author')})")

            # 加载插件
            self.applicationContext.plugins["cq"].append(plugin)

        for i in h5:
            if not StringUtil.equals(i, "py", 2): continue
            # 获取插件名称
            pluginName = StringUtil.splitToString(i)

            # 动态导入插件
            # plugin = importlib.import_module(".", f"h5.plugins.{pluginName}")
            plugin = importlib.import_module(f"h5.plugins.{pluginName}")

            # 解析插件信息
            pluginInfo = PythonUtil.analysisDoc(plugin.__doc__)
            print(f"正在加载H5插件: {pluginInfo.get('title')}v{pluginInfo.get('version')} ({pluginInfo.get('author')})")

            # 加载插件
            self.applicationContext.plugins["h5"].append(plugin)
        
        print("CQ插件数量: %d个" % len(self.applicationContext.plugins["cq"]))
        print("H5插件数量: %d个" % len(self.applicationContext.plugins["h5"]))
        print()
        return None

    def __loadBootstrap(self) -> None:
        path = self.applicationContext.basePath + r"/data/bootstrap.json"
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("{}")

        with open(path, "r") as f:
            self.applicationContext.bootstrap = json.loads(f.read())
        return None

    def init(self):
        # 加载容器
        self.__loadContainer()

        # 路径
        self.applicationContext.basePath = os.getcwd()

        # 加载插件/配置文件
        self.__loadPluings()
        self.__loadBootstrap()

    def _run(self):
        # 初始化元信息
        self.requestContext.reset()

        # 获取conn数据并封装为Request
        request = SocketUtil.getConn(self.listenSocket, BUFSIZE)

        # 不知道从哪里蹦出来的无效请求
        if (request.source == None):
            self.log.error(f"出现了一条无效请求: {request.__dict__}")
            return None

        # 将Request和map交给Dispatcher进行派发
        response = Dispatcher(request, self.requestContext, self.sessionContext, self.applicationContext).main()

        # 返回数据
        # SocketUtil.sendAll(request, response)

        # 关闭连接
        # SocketUtil.close(self.listenSocket)

        # 打印日志
        if (self.requestContext.isLog and self.requestContext.isTriggerModule != "False"):
            self.log.info(f"[{self.counter.next()}]")
            self.log.info(f"{self.requestContext.isTriggerModule}模块 {request.version} {request.method} {request.url}")
            # self.log.info(list(request.headers))
            # self.log.info(list(request.data))
            self.log.info(request.data)
            for n, i in enumerate(response.text):
                self.log.info(f"({n + 1}/{len(response.text)}) {i}")
            print("\n\n")

    def main(self):
        while True: self._run()


####################################################
# Run
####################################################
if __name__ == "__main__":
    printInfo()

    s = Server()

    s.init()

    s.main()
