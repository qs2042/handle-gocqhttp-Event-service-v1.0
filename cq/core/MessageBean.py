

class Type: 
    META_EVENT = 0
    NOTICE = 1
    REQUEST = 2
    MESSAGE = 3

class MessageBean:
    def __init__(self, raw_data) -> None:
        # 类型, 副类型, 源数据
        self.type:int = None
        self.sub_type:int = None
        self.raw_data:dict = raw_data
        
        # 群, 消息, 消息ID
        self.group_id:int = None
        self.message:str = None
        self.message_id:int = None

        # 用户ID, 用户群名片, 用户网名
        self.user_id:int = None
        self.user_card:str = None
        self.user_nick:str = None

        self.a()
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def a(self):
        # 消息类型
        post_type = self.raw_data.get("post_type")

        # 元事件
        if post_type == "meta_event": 
            self.type = Type.META_EVENT

        # 事件
        if post_type == "notice": 
            self.type = Type.NOTICE

        # 请求
        if post_type == "request": 
            self.type = Type.REQUEST
        
        if post_type == "message": 
            self.type = Type.MESSAGE
            messageType = self.raw_data.get("message_type")
            anonymous = self.raw_data.get("anonymous")

            # 群聊匿名, 群聊, 私聊
            if (anonymous != None): self.sub_type = 0
            if (messageType == "group"): self.sub_type = 1
            if (messageType == "private"): self.sub_type = 2

            self.message = self.raw_data.get("message")
            self.message_id = self.raw_data.get("message_id")
            self.group_id = self.raw_data.get("group_id")
            
            self.user_id = self.raw_data.get("sender").get("user_id")
            self.user_card = self.raw_data.get("sender").get("card")
            self.user_nick = self.raw_data.get("sender").get("nickname")
    
    def __str__(self) -> str:
        return str(self.__dict__)
