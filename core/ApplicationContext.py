
class ApplicationContext: 
    def __init__(self) -> None:
        # 插件
        self.loadPlugins()

        # 路径
        self.basePath = None
        
        # 配置文件
        self.bootstrap = {}

        
        
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