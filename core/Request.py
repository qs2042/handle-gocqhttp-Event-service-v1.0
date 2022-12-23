import json

class Request:
    # 路由, 方法, 版本, 头, 数据, conn, 原始数据
    url = None
    method = None
    version = None
    headers = {}
    data = {}
    conn = None
    source = None

    def __init__(self, conn, source) -> None:
        self.conn = conn
        self.source = source
        self.analysisSource(self.source)
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def analysisSource(self, source:str):
        # 获取第一行(method url version)
        if (len(source.splitlines()) == 0):
            self.source = None
            return 
        requestLine = source.splitlines()[0]
        self.method = requestLine.split(" ")[0]
        self.url = requestLine.split(" ")[1]
        self.version = requestLine.split(" ")[-1]

        # GET
        if self.method == "GET":
            # 获取第二行(headers)
            requestHeaders = {}
            for i in source.splitlines()[1:]:
                if i == "":
                    continue
                entry = i.split(": ")
                requestHeaders[entry[0]] = entry[-1]
            self.headers = requestHeaders

            # 获取第三行(空行)
            emptyLine = None
            
            # 获取第四行(Body)(只有POST才有)
            body = None
            if "?" in self.url:
                self.data = {}
                data = self.url.split("?")[-1]
                self.url = self.url.split("?")[0]
                for i in data.split("&"):
                    k = i.split("=")[0]
                    v = i.split("=")[-1]
                    self.data[k] = v

        # POST
        if self.method == "POST":
            # 获取第二行(headers)
            requestHeaders = {}
            for i in source.split("\r\n\r\n")[0].splitlines()[1:]:
                if i == "":
                    continue
                entry = i.split(": ")
                requestHeaders[entry[0]] = entry[-1]
            self.headers = requestHeaders

            # 获取第三行(空行)
            emptyLine = None

             # 获取第四行(Body)(只有POST才有)
            body = None
            
            data = source.split("\r\n\r\n")[-1]

            try:
                self.data = json.loads(data)
            except:
                print("无法解析该POST请求的source")
                try:
                    print("正在进行第二次解析")
                    # 第一种情况: message缺少"} 这几个字符
                    self.data = json.loads("%s\"}" % data)
                except:
                    try:
                        print("正在进行第三次解析")
                        # 第二种情况: message缺少":""} 这几个字符
                        self.data = json.loads("%s\":\"\"}" % data)
                    except:
                        print("三种方法都解析失败, 请提交BUG")
                        print(source)
                        print()