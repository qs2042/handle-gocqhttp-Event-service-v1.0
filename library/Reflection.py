# 带有大量反射方法
import inspect, types


class ReflectionUtil:
    @staticmethod
    def isFunction(variable):
        '''判断是否为方法'''
        a1 = isinstance(variable, types.FunctionType)

        a2 = callable(variable)

        a3 = hasattr(variable, "__call__")
        return a1 == True and a2 == True and a3 == True

    @staticmethod
    def getAnnotationsByFunction(func):
        '''获取方法的注解'''
        return func.__annotations__

    @staticmethod
    def getAnnotationsByClass(cla):
        '''获取类的注解'''
        return cla.__dict__.get("__annotations__")

    @staticmethod
    def getDocByInstance(instance):
        return instance.__doc__

class Reflection:
    def __init__(self, targetObject) -> None:
        self.obj = targetObject

        self.python = { "function": {}, "variable": {} }
        self.hidden = { "function": {}, "variable": {} }
        self.public = { "function": {}, "variable": {} }
        self.all = {}
        self.__analysis(self.obj.__dict__)

    def __analysis(self, data: dict):
        self.all = dict(data)
        for k in data:
            v = data.get(k)
            vType = "variable"

            if k[:2] == "__":
                if ReflectionUtil.isFunction(v): vType = "function"
                self.python[vType][k] = v
                continue
            if k[:1] == "_":
                if ReflectionUtil.isFunction(v): vType = "function"
                self.hidden[vType][k] = v
                continue
            
            if ReflectionUtil.isFunction(v): vType = "function"
            self.public[vType][k] = v
        return None
    
    # 获取类成员
    def getAttribute(self, attributeName:str):
        try:
            return self.obj.__getattribute__(attributeName)
        except:
            return None

    # 设置类成员
    def setAttribute(self, attributeName:str, value):
        self.obj.__setattr__(attributeName, value)

    # 删除类成员
    def delAttribute(self, attributeName:str):
        try:
            return self.obj.__delattr__(attributeName)
        except:
            return None


if __name__ == "__main__":
    class Person:
        qq = 2042136767
        author: str = 'R'
        def t1(self, t): return "t1"
        def t2(self, t:int): return "t2"
        def t3(self, t=20): return "t3"
        def t4(self, *args): return "t4"
        def t5(self, **kwargs): return "t5"
        def _t6(self): return "t6"
        def __t7(self): return "t7"
        def t8(self):
            '''test'''
            return "t8"

    r = Reflection(Person)