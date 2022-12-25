import requests, re, json



class ApplicationContext: 
    def __init__(self) -> None:
        # 插件, 事件, 官方库
        self.loadPlugins()
        self.loadEvent()
        self.loadLibrary()

        # 配置文件
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
        self.event = {
            # 视频, 语音, 图片
            "video": [], "record": [], "image": [],

            # 抖一抖, 
            "tremble": []
            
            # 分享(app), 被@, 被回复, QQ表情
        }
    
    def loadBootstrap(self):
        self.bootstrap = {}

    def __str__(self) -> str:
        return str(self.__dict__)