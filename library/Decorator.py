'''
id      ...
type    0=Meta, 1=Event, 2=Mapping, 3=...
func    ...
args    ...
kwargs  ...
note    ...
'''
import types, time

class Data:
    def __init__(self, id: int, type: int, func: types.FunctionType, args: tuple, kwargs: dict, note: str) -> None:
        self.id = id
        # 0=元信息, 1=消息事件, 2=
        self.type = type
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.note = note
    
    def __repr__(self) -> str:
        d = self.__dict__
        #d["func"] = None
        return str(d)
    
    def __getData(self):
        # result = { type: { id: func... }, func: Function }
        result = {}
        _func = self

        while True:
            # 判断func是否为Meta
            if type(_func) != Data: 
                result["func"] = _func
                break
            
            # 二级数据初始化
            if not str(_func.type) in result:
                result[str(_func.type)] = {}

            result[str(_func.type)][str(_func.id)] = _func
            #print(f"{_func.type}: {_func.note}({_func.id})\n{_func}\n\n")
            _func = _func.func

            
        return result

    def getFunc(self):
        return self.__getData().get("func")
    def get(self, type: int = None, id: int = None):
        # 一级菜单
        one = self.__getData()
        if one == None: return None
        if type == None: return one
        
        # 二级菜单
        two: dict = one.get(str(type))
        if two == None: return None
        if id == None: return two

        # 最终数据
        return two.get(str(id))

class Meta:
    @staticmethod
    def order(value, *args, **kwargs):
        def wrapper(func):
            kwargs["value"] = value
            return Data(100, 0, func, args, kwargs, "排序")
        return wrapper

    @staticmethod
    def jurisdiction(value, *args, **kwargs):
        def wrapper(func):
            kwargs["value"] = value
            return Data(101, 0, func, args, kwargs, "权限")
        return wrapper

class Event:
    @staticmethod
    def messagePrivate(*args, **kwargs):
        def wrapper(func):
            return Data(100, 1, func, args, kwargs, "事件: 私聊")
        return wrapper

    @staticmethod
    def messageGroup(*args, **kwargs):
        def wrapper(func):
            return Data(101, 1, func, args, kwargs, "事件: 群聊")
        return wrapper

    @staticmethod
    def messageRecall(*args, **kwargs):
        def wrapper(func):
            return Data(102, 1, func, args, kwargs, "事件: 消息撤回")
        return wrapper

class Mapping:
    def __allToList(value) -> list:
        if type(value) != list: return [value]
        return value

    @staticmethod
    def all(command, *args, **kwargs):
        def decorator(func):
            def wrapper(*args, **kwargs):
                l = Mapping.__allToList(command)
                msg = kwargs.get("msg")
                if type(msg) == str: msg = msg.strip()
                
                #print("="*10)
                #print(f"指令(raw): {command}")
                #print(f"指令(list): {l}")
                #print(f"消息: {msg}")
                #print("="*10)
                if msg == None or len(msg) == 0: raise Exception("缺少msg")
                
                # 判断消息是否存在于指令列表之中
                kwargs["value"] = False
                if msg in l: kwargs["value"] = True
                
                return Data(100, 2, func, args, kwargs, "匹配: 所有")
            return wrapper
        return decorator
    
    @staticmethod
    def prefix(command, separator=" ", *args, **kwargs):
        def decorator(func):
            def wrapper(*args, **kwargs):
                l = Mapping.__allToList(command)
                msg = kwargs.get("msg")
                if type(msg) == str: msg = msg.strip()
                
                kwargs["value"] = False
                kwargs["message"] = ""
                kwargs["params"] = []

                # 判断消息是否符合指令列表之中的前缀
                for i in l:
                    # 消息长度 > 指令长度, 直接开始下一轮
                    if len(msg) < len(i): continue

                    if i == msg[:len(i)]:
                        kwargs["value"] = True
                        kwargs["message"] = f"{msg[len(i):]}".strip()
                        kwargs["params"] = f"{msg[len(i):]}".strip().split(separator)
                
                return Data(100, 2, func, args, kwargs, "匹配: 前缀")
            return wrapper
        return decorator

    @staticmethod
    def suffix(command, separator=" ", *args, **kwargs):
        def decorator(func):
            def wrapper(*args, **kwargs):
                l = Mapping.__allToList(command)
                msg = kwargs.get("msg")
                
                kwargs["value"] = False
                kwargs["params"] = []

                # 判断消息是否符合指令列表之中的前缀
                for i in l:
                    # 消息长度 > 指令长度, 直接开始下一轮
                    if len(msg) < len(i): continue

                    if i == msg[-len(i):]:
                        kwargs["value"] = True
                        kwargs["params"] = f"{msg[:-len(i)]}".strip().split(separator)
                
                return Data(100, 2, func, args, kwargs, "匹配: 后缀")
            return wrapper
        return decorator

    @staticmethod
    def approved(*args, **kwargs):
        def decorator(func):
            def wrapper(*args, **kwargs):
                msg = kwargs.get("msg")
                if type(msg) == str: msg = msg.strip()
                
                if msg == None or len(msg) == 0: raise Exception("缺少msg")
                
                kwargs["value"] = True
                return Data(100, 2, func, args, kwargs, "匹配: 通过")
            return wrapper
        return decorator

class Utils:
    class Data:
        def __init__(self, func, decorator) -> None:
            self.func = func
            self.decorator = decorator
    @staticmethod
    def timer(func):
        def func_in() -> Utils.Data:
            startTime = time.time()
            r = func()
            endTime = time.time()
            spendTime = (endTime - startTime) / 60
            return Utils.Data(r, spendTime)
        return func_in


@Meta.order(20)                         # 执行顺序: 20
@Meta.jurisdiction(0)                   # 使用权限: 0
@Event.messagePrivate()                 # CQ事件: 私聊
@Event.messageGroup()                   # CQ事件: 群聊
@Event.messageRecall()                  # CQ事件: 消息撤回
@Mapping.all("签到")                    # 匹配: 所有        test("签到")        -> 匹配成功(params=None)        -> 签到成功
#@Mapping.all(["签到", ".sign"])         # 匹配: 所有        test("签到114514")  -> 匹配失败(params=None)        -> 签到失败
#@Mapping.prefix("点歌")                 # 匹配: 前缀        test("点歌")        -> 匹配成功(params=None)        -> 点歌成功
#@Mapping.prefix(["点歌", ".music"])     # 匹配: 前缀        test("点歌123")     -> 匹配成功(params=123)         -> 点歌成功(歌名123)
#@Mapping.suffix("喵")                   # 匹配: 后缀        test("点赞喵")      -> 匹配成功(params=点赞)        -> 不准带喵说话!
def test():
    return "123"


def mapping(value=""):
    def isTriggerInstruction(text, instruction):
        # 将前缀指令转为列表
        if type(instruction) != list:
            tmp = instruction
            instruction = []
            instruction.append(tmp)
        
        switch = False
        for i in instruction:
            if i == False or i == None or i == '' or i == []:
                switch = True
                break
            if i == text[:len(i)]:
                switch = True
                result = text[len(i):]
                break

        # 如果没触发指令
        if not switch: return False
        
        # 如果触发了指令
        return result.rstrip().lstrip()

    def mapping_decorator(func):
        def warpper(*args, **kwargs):
            # 获取传进来的消息
            message = args[0]
            # message = kwargs["message"]

            # 判断是否触发指令
            result: str = isTriggerInstruction(message, value)
            if (result == False): return None

            # 删除前后空格
            result.strip()

            return func(message=result)
        return warpper
    return mapping_decorator
