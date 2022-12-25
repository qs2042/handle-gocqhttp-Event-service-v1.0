####################################################
# library
####################################################
import importlib
import json
import os

from core.ApplicationContext import ApplicationContext
from core.Dispatcher import Dispatcher
from core.MetaMap import MetaMap

from library.Log import Log
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

        # 路径, 日志
        self.base = os.getcwd()
        self.log = Log("server")

        # 容器(request, session, application)
        self.metaMap = MetaMap()
        self.sessionContext = None
        self.applicationContext = ApplicationContext()

        # 加载插件, 配置文件
        self.loadPluings()
        self.loadBootstrap()

    def loadPluings(self) -> None:
        # isExist = os.path.exists(base + r"/data/plugins.pkl")
        # if isExist:
        #     with open("data.pkl", "rb") as f:
        #         self.applicationContext.plugins = pickle.load(f)
        #     return None

        cq: list = os.listdir(self.base + r"/cq/plugins")
        h5: list = os.listdir(self.base + r"/h5/plugins")

        for i in cq:
            # 如果后缀不是py, 那就直接跳过
            if not StringUtil.equals(i, "py", 2): continue

            # 获取插件名称
            pluginName = StringUtil.splitToString(i)

            # 动态导入插件
            plugin = importlib.import_module(".", f"cq.plugins.{pluginName}")

            # 解析插件信息
            pluginInfo = PythonUtil.analysisDoc(plugin.__doc__)
            print(f"正在加载CQ插件: {pluginInfo.get('title')}v{pluginInfo.get('version')} ({pluginInfo.get('author')})")

            # 加载插件
            self.applicationContext.plugins["cq"].append(plugin)
        print("总共:%d个\n" % len(self.applicationContext.plugins["cq"]))

        for i in h5:
            if not StringUtil.equals(i, "py", 2): continue
            # 获取插件名称
            pluginName = StringUtil.splitToString(i)

            # 动态导入插件
            plugin = importlib.import_module(".", f"h5.plugins.{pluginName}")

            # 解析插件信息
            pluginInfo = PythonUtil.analysisDoc(plugin.__doc__)
            print(f"正在加载H5插件: {pluginInfo.get('title')}v{pluginInfo.get('version')} ({pluginInfo.get('author')})")

            # 加载插件
            self.applicationContext.plugins["h5"].append(plugin)
        print("总共:%d个...\n" % len(self.applicationContext.plugins["h5"]))

        # with open("data.pkl", "wb") as f:
        #     pickle.dump(self.applicationContext.plugins, f)
        return None

    def loadBootstrap(self) -> None:
        path = self.base + r"/data/bootstrap.json"
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("{}")

        with open(path, "r") as f:
            self.applicationContext.bootstrap = json.loads(f.read())
        return None

    def _run(self):
        # 初始化元信息
        self.metaMap.reset()

        # 获取conn数据并封装为Request
        request = SocketUtil.getConn(self.listenSocket, BUFSIZE)

        # 不知道从哪里蹦出来的无效请求
        if (request.source == None):
            self.log.error(f"出现了一条无效请求: {request.__dict__}")
            return None

        # 将Request和map交给Dispatcher进行派发
        response = Dispatcher(request, self.metaMap, self.applicationContext).main()

        # 返回数据
        # SocketUtil.sendAll(request, response)

        # 关闭连接
        # SocketUtil.close(self.listenSocket)

        # 打印日志
        if (self.metaMap.isLog and self.metaMap.isTriggerModule != "False"):
            self.log.info(f"{self.metaMap.isTriggerModule}模块 {request.version} {request.method} {request.url}")
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

    s.main()
