# 带有大量反射方法
import inspect




class Reflection:
    def __init__(self, targetObject) -> None:
        self.obj = targetObject
    
    # 获取类成员(所有)
    def getVariables(self):
        # core: __dict__
        data = self.obj.__dict__

        result = { "python": {}, "hidden": {}, "public": {} }
        
        # 如果为 0
        if len(data) == 0: return result

        # 如果不为0
        for i in data:
            if i[:2] == "__":
                result["python"][i] = data[i]
                continue
            if i[:1] == "_":
                result["hidden"][i] = data[i]
                continue
            result["public"][i] = data[i]

        return result
    
    # 获取类方法名称(所有)
    def getMethods(self):
        data = dir(self.obj)

        result = {
            "python":[], "hidden":[], "public":[]
        }

        for i in data:
            if i[:2] == "__":
                result["python"].append(i)
                continue
            if i[:1] == "_":
                result["hidden"].append(i)
                continue

            result["public"].append(i)
        return result

    # 获取方法注解(指定)
    def getMethodAnnotations(self, func):
        return func.__annotations__
    
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
        def t1(self): return "t1"
        def t2(self): return "t2"
        def t3(self): return "t3"
        def _fun(self): return "fun"

    r = Reflection(Person)