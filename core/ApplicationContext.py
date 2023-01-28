
class ApplicationContext: 
    def __init__(self) -> None:
        # 插件
        self.loadPlugins()

        # 路径
        self.basePath = None
        
        # 配置文件
        self.bootstrap = {}

        # 缓存
        self.cache = {}

        # 错误
        self.error = {}
    
    def getCache(self): pass
    def setCache(self): pass
    
    def getBootstrap(self, *args): 
        node = None
        data: dict = self.bootstrap
        for i in args:
            node = data.get(i)
            if node == None: return node
            data = node
        return node
    

    def __setBootstrap(self, l) -> dict:
        if len(l) == 1: return l[0]
        d = { l[0]: self.__setBootstrap(l[1:]) }
        return d
    def setBootstrap(self, *args): 
        if type(args) == tuple:
            print("当前功能暂未写完")
            return False

        if len(args) == 1: return False

        data = self.__setBootstrap(list(args))

        self.bootstrap.update(data)
        
        return True
        
    def loadPlugins(self):
        self.plugins = {
            "cq": [],
            "h5": [],
            "shieldingWords": [
                # 注解
                "mapping",
                # 排除列表
                "excludeList", 
                # global variable List
                "gvl",
                # bean
                "request", "Request", 
                "response", "Response",
                "messageBean", "MessageBean", 
                # context
                "requestContext", "RequestContext",
                "sessionContext", "SessionContext",
                "applicationContext", "ApplicationContext", 
            ]
        }

    def __str__(self) -> str:
        return str(self.__dict__)