import threading, sys, os, time

class Log:
    def __init__(self, applicationName:str) -> None:
        self.applicationName = applicationName

        self.text = ""

    def _message(self, status: str, info: str, isTime = False, isThread = False):
        self.text = "[status][application][time][thread] [info]"
        self.text = self.text.replace("status", status)
        self.text = self.text.replace("application", self.applicationName)

        if (isTime):
            self.text = self.text.replace("time", str(time.localtime()))
        else: self.text = self.text.replace("[time]", "")
        
        if (isThread):
            self.text = self.text.replace("thread", "%s-%s" % (threading.currentThread().getName(), threading.currentThread().ident))
        else: self.text = self.text.replace("[thread]", "")
        
        self.text = self.text.replace("[info]", str(info))
        
    def test(self, info):
        self._message("TEST", info, False, True)
        print(self.text)

    def info(self, info):
        self._message("INFO", info, False, True)
        print(self.text)

    def error(self, info):
        self._message("ERROR", info, False, True)
        print(self.text)

    def debug(self, info):
        self._message("DEBUG", info, False, True)
        print(self.text)
    


if __name__ == "__main__":
    log = Log("logTest")
