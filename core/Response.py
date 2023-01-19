class Response:
    def __init__(self) -> None:
        # 版本
        self.agreement = "HTTP"
        self.version = "1.1"

        # 状态码
        self.statusCode = "200"
        
        # 返回值
        self.text = []

        # 头
        self.headers = {
            "Content-Type": "text/html;charset=utf-8",
        }
        
    def __str__(self) -> str:
        return str(self.__dict__)

    def _getHeaders(self):
        s = ""
        for i in self.headers:
            s += "%s: %s\n" % (i, self.headers[i])
        return s[:-1]
    
    def _getText(self):
        if (len(self.text) == 0): return ["<h1> 默认返回值 </h1>"]
        return self.text

    def result(self):
        r = "<br>".join(str(x) for x in self._getText())
        res = f"{self.agreement}/{self.version} {self.statusCode} OK \n{self._getHeaders()}\r\n\r\n{r}"
        return res

    def modeText(self):
        self.headers = { "Content-Type": "text/html;charset=utf-8" }
    
    def modeImage(self, fileName):
        self.headers = {
            # 压缩媒体类型
            "Content-Encoding": "gzip/trunked/base64",
            #Content-Language(描述旨在为观众的语言)
            #Content-Length 
            #Content-Location 
            #Content-MD5 
            #Content-Range 
            #Content-Type 
            #Expires 
            #Last-Modified 
            #extension-header

            # 正常
            #"Content-Type": "image/x-icon",
            "Content-Type": "image/jpeg",
            "Accept-Ranges": "bytes",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Expires": "0",
            "X-Sendfile": fileName
        }
