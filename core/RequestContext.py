class RequestContext:
    def __init__(self) -> None:
        # 是否触发模块, 事件, 功能
        self.isTriggerModule = False
        self.isTriggerEvent = False
        self.isTriggerFunction = False

        # 是否发送日志
        self.isLog = True
    
    def reset(self):
        self.isTriggerModule = False
        self.isTriggerEvent = False
        self.isTriggerFunction = False
        self.isLog = True
    
    def __str__(self) -> str:
        return str(self.__dict__)