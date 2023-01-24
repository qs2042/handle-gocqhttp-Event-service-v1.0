class StringUtil:
    # 分割并转换为字符串
    @staticmethod
    def splitToString(tmp: str, separator=".", mode=0) -> str:
        '''
        [mode]
        0 获取最前一个
        1 获取最后一个

        2 排除最后一个
        3 排除最前一个
        '''
        l = tmp.split(f"{separator}")
        if mode == 0: return l[0]
        if mode == 1: return l[-1]
        if mode == 2: return f"{separator}".join(l[:-1])
        if mode == 3: return f"{separator}".join(l[1:])

    @staticmethod
    def equals(tmpA: str, tmpB: str, mode=0) -> bool:
        '''
        [mode]
        0 完全对比
        1 只对比前缀
        2 只对比后缀
        '''
        if mode == 0: return tmpA == tmpB

        length = 0
        if len(tmpA) > len(tmpB):
            length = len(tmpB)
        else:
            length = len(tmpA)

        if mode == 1: return tmpA[:length] == tmpB[:length]
        if mode == 2: return tmpA[-length:] == tmpB[-length:]



import os
# TODO: 暂时摆在这里
class PathUtil:
    '''
    # 获取当前目录
    print(os.getcwd())
    print(os.path.dirname(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    # 获取上级目录
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.dirname(os.getcwd())))
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    # 获取上上级目录
    print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

    # 获取上上上级目录
    print(os.path.abspath(os.path.join(os.getcwd(), "../../..")))

    # 以此类推...
    '''
    @staticmethod
    def getcwd():
        return os.getcwd()
    
    @staticmethod
    def getFile():
        return __file__
