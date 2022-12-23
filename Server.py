####################################################
# library
####################################################
import os, importlib, pickle, json

from core.Dispatcher import Dispatcher
from core.Request import Request
from core.Response import Response
from core.MetaMap import MetaMap
from core.ApplicationContext import ApplicationContext

from tools.SocketUtil import SocketUtil
from tools import StringUtil
from tools import PythonUtil

from library.Log import Log



'''
TODO
1.CQ模块            事件, 特殊消息解析
2.CQ模块            自定义事件
3.CQ模块            新版API
4.@mapping          增加全匹配模式
5.@order            咕咕咕
6.@chat_group       咕咕咕
7.@chat_private     咕咕咕
8.@jurisdiction     咕咕咕
9.bootstrap.json    咕咕咕

'''


####################################################
# 路线图
####################################################
'''
QQ -> gocqhttp -> RQ(server) -> RQ(conn -> request)
↓
dispatcher
↓
-> event(h5) -> plugins -> function(api)
-> event(cq) -> plugins -> function(api)
↓
response(result)
'''

####################################################
# Variable
####################################################
IP = "127.0.0.1"
PORT = 5701
BUFSIZE = 4096

def printInfo() -> None:
    print("="*30)
    print("欢迎使用RQ框架")
    print("="*30)
    print("""
    author: R
    version: v1.0
    encoding: utf-8
    introduce: 此项目基于gocqhttp(https://github.com/Mrs4s/go-cqhttp)
    createTime: 2022-10-8 15:41:59
    """.strip().replace("    ", ""))
    print("="*30)


####################################################
# Main
####################################################
class Server:
    def __init__(self) -> None:
        # 初始化socket对象
        self.listenSocket = SocketUtil.getSocket(IP, PORT)

        self.base= os.getcwd()

        # 日志        
        self.log = Log("server")

        # 容器(request, session, application)
        self.metaMap = MetaMap()
        self.sessionContext = None
        self.applicationContext = ApplicationContext()

        self.loadPluings()
        self.loadBootstrap()

    # 加载插件
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
    
    # 加载配置文件
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
                self.log.info(f"({n+1}/{len(response.text)}) {i}")
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