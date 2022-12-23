import requests, re, json



class ApplicationContext: 
    def __init__(self) -> None:
        # 插件
        self.loadPlugins()

        # 包
        self.loadPlugins()

        self.loadBootstrap()
        
    def loadPlugins(self):
        self.plugins = {
            "cq": [],
            "h5": []
        }

    def loadLibrary(self):
        self.library = {
            "requests": requests,
            "re": re,
            "json": json
        }

    def loadEvent(self):
        self.eventList = {}
    
    def loadBootstrap(self):
        self.bootstrap = {}

    def __str__(self) -> str:
        return str(self.__dict__)