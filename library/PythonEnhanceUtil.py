



class PythonEnhanceUtil:
    @staticmethod
    def getByList(l: list, index: int, type=str, default = None):
        try:
            return type(l[index])
        except:
            return default
    