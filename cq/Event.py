from core.Response import Response
from core.Request import Request

# context
from core.RequestContext import RequestContext
from core.SessionContext import SessionContext
from core.ApplicationContext import ApplicationContext

from library.Log import Log
from library.Reflection import Reflection
from library.Decorator import Data

from cq.API import API
from cq.core.MessageBean import MessageBean
from cq.core.MessageBean import Type as MessageBeanType

from library.SocketUtil import SocketUtil


class Event:
    def __init__(self, request: Request, response: Response, requestContext: RequestContext, sessionContext: SessionContext, applicationContext: ApplicationContext) -> None:
        self.request = request
        self.response = response
        self.requestContext = requestContext
        self.sessionContext = sessionContext
        self.applicationContext = applicationContext

        self.log = Log("CQ-Event")

        self.api = API()
        self.messageBean = None

    def showDatabaseMessage(self, data):
        # 群聊匿名
        if data.get("anonymous") != None:
            other = f"""
                收到来自群聊(匿名)的消息
                消息来自      : {data.get('group_id')}
                发送者        : {data.get('sender_nickname')}({data.get('user_id')})
                群昵称        : {data.get('sender_card')}
                群等级        : {data.get('sender_level')}
                身份          : {data.get('sender_role')} 
                性别          : {data.get('sender_age')}
                头衔          : {data.get('sender_title')}
                消息内容      : {data.get('message')}
                消息内容(raw) : {data.get('raw_message')}
                消息ID        : {data.get('message_id')}
                anonymous     : {data.get('anonymous')}""".replace("                ", "")
            self.log.info(other)
            return None
        
        # 群聊
        if data.get("message_type") == "group":
            sender: dict = data.get("sender")
            other = f"""
            收到来自群聊的消息
            消息来自      : {data.get('group_id')}
            发送者        : {sender.get('nickname')}({data.get("user_id")})
            群昵称        : {sender.get('card')}
            群等级        : {sender.get('level')}
            身份          : {sender.get('role')}
            性别          : {sender.get('age')}
            头衔          : {sender.get('title')}
            消息内容      : {data.get('message')}
            消息内容(raw) : {data.get('raw_message')}
            消息ID        : {data.get('message_id')}
            anonymous     : {data.get('anonymous')}""".replace("            ", "")
            self.log.info(other)
        
        # 私聊
        if data.get("message_type") == "private":
            other = f"""
            收到来自私聊的消息
            消息来自      : {data["sender"]["nickname"]}({data["user_id"]})
            年龄          : {data["sender"]["age"]}
            性别          : {data["sender"]["sex"]}
            消息内容      : {data["message"]}
            消息内容(raw) : {data["raw_message"]}
            消息ID        : {data["message_id"]}""".replace("            ", "")
            self.log.info(other)
    
    def showDatabaseNotice(self, data):
        noticeType = data.get("notice_type")
        # 群管理(group_admin-set, group_admin-unset)
        # 禁言(group_ban-ban, group_ban-lift_ban)
        # 群员变动(group_increase-approve, group_decrease-leave, group_decrease-kick)
        # 群文件上传(group_upload)

        map = {
            "friend_recall": "撤回",
            "group_ban": "群禁言",  # ban， lift_ban
        }
        
        self.log.info(f"""收到{map.get(data.get('notice_type'))}事件
            群ID        : {data.get("group_id")}
            执行人员    : {data.get("operator_id")}
            被执行人    : {data.get("user_id")}
            执行方法    : {data.get("notice_type")}({data.get("sub_type")})
            执行数值    : {data.get("duration")}
            执行时间    : {data.get("time")}
        """.replace("            ", ""))

    def showDatabaseRequest(self, data):
        # 如果是群加入
        '''
        if data.get("request_type") == "group" and data.get("sub_type") == "add":
            self.log.info(
                f"已自动同意加群({data.get('group_id')})申请"
            )
            data.get("comment")     # 附加消息
            self.api.setGroupAddRequest(data.get("flag"), data.get("sub_type"))
        '''

    def sendMessage(self):
        if len(self.response.text) == 0: return None
        for i in self.response.text:
            self.api.sendMessage(self.messageBean.raw_data.get("message_type"), self.messageBean.user_id, self.messageBean.group_id, i)
        return None

    def handlerMessage(self) -> MessageBean:
        data = self.request.data

        m = MessageBean(data)

        # 元事件, 事件, 请求, 消息
        post_type = data.get("post_type")
        if post_type == "meta_event": m.type = MessageBeanType.META_EVENT
        if post_type == "notice": m.type = MessageBeanType.NOTICE
        if post_type == "request": m.type = MessageBeanType.REQUEST
        if post_type == "message": 
            m.type = MessageBeanType.MESSAGE
            messageType = data.get("message_type")
            anonymous = data.get("anonymous")

            # 群聊匿名, 群聊, 私聊
            if (anonymous != None): m.sub_type = 0
            if (messageType == "group"): m.sub_type = 1
            if (messageType == "private"): m.sub_type = 2

            m.message = data.get("message")
            m.message_id = data.get("message_id")
            m.group_id = data.get("group_id")
            
            m.user_id = data.get("sender").get("user_id")
            m.user_card = data.get("sender").get("card")
            m.user_nick = data.get("sender").get("nickname")

        return m



    def funMetaEvent(self):
        self.requestContext.isLog = False
        # 轮询心跳事件
        #if data.get("meta_event_type") == "heartbeat":
        #    self.requestContext.isLog = False
        #    isTrigger = True
        return False

    def funNotice(self):
        self.showDatabaseNotice(self.messageBean.raw_data)

    def funRequest(self):
        self.showDatabaseRequest(self.messageBean.raw_data)
    
    def funSpecial(self):
        # TODO: 1.换成正则表达式来解析类型  2.只做了拦截, 暂未写其他逻辑
        data = self.messageBean.raw_data
        message = data.get("message")
        isTrigger = False

        if not isTrigger and len(message)==0:
            isTrigger = True
            self.log.info("触发抖一抖")

        video = "[CQ:video,file="
        if not isTrigger and message[:len(video)] == video: 
            isTrigger = True
            self.log.info("已获取视频链接: " + message)

        audio = "[CQ:record,file="
        if not isTrigger and message[:len(audio)] == audio: 
            isTrigger = True
            self.log.info("已获取音频链接: " + message)

        image = "[CQ:image,file="
        if not isTrigger and message[:len(image)] == image: 
            isTrigger = True
            self.log.info("已获取图片链接: " + message)

        reply = "[CQ:reply,id="
        if not isTrigger and message[:len(reply)] == reply: 
            isTrigger = True
            self.log.info("已获取回复信息: " + message)

        at = "[CQ:at,qq=%s]" % data.get("self_id")
        if not isTrigger and message[:len(at)] == at: 
            isTrigger = True
            self.log.info("已获取被AT信息: " + message)
        
        face = "[CQ:face,id="
        if not isTrigger and message[:len(face)] == face: 
            isTrigger = True
            self.log.info("已获取被QQ表情信息: " + message)
        
        if not isTrigger: return False
        return True

    def funMessage(self):
        data = self.messageBean.raw_data
        messageType = data.get("message_type")

        # 是否为: 群聊匿名, 群聊, 私聊
        if (data.get("anonymous") != None):pass
        if (messageType == "group"): pass
        if (messageType == "private"): pass

        # 获取插件列表
        pluginList = self.applicationContext.plugins.get("cq")

        # 循环插件中的方法
        for plugin in pluginList:
            r = Reflection(plugin)
            # 获取排除选项
            excludeList = r.getAttribute("excludeList")
            shieldingWords = self.applicationContext.plugins.get("shieldingWords")
            if excludeList != None: shieldingWords += excludeList

            # 获取方法列表, 并排除掉一些选项
            l = [x for x in r.public.get("variable") if x not in shieldingWords]
            
            # 注入数据
            r.setAttribute("request", self.request)
            r.setAttribute("response", self.response)
            r.setAttribute("requestContext", self.requestContext)
            r.setAttribute("sessionContext", self.sessionContext)
            r.setAttribute("applicationContext", self.applicationContext)
            r.setAttribute("messageBean", self.messageBean)
            # print(r.public)
            # print(l)

            # 循环方法列表
            for methodName in l:
                method: Data = r.getAttribute(methodName)
                meta = method.get("0")
                event = method.get("1")
                func = method.getFunc()

                # 0.判断是否有meta信息
                if meta == None: pass 

                # 1.判断事件信息是否和CQ事件对上
                if event == None: continue

                # 2.调用外层的mapping
                res: Data = func(msg=data.get("message"))

                # 3.mapping执行失败
                if not res.kwargs["value"]:
                    #self.log.info(f"执行失败(100) -> {plugin.__name__} -> {methodName}")
                    continue

                # 4.mapping执行成功
                status = res.func(kv = res.kwargs)
                # True=执行成功, False=执行失败, None=继续往下执行
                if status == False: 
                    #self.log.info(f"执行失败(101) -> {plugin.__name__} -> {methodName} -> {res.kwargs}")
                    continue

                if status == None:
                    #self.log.info(f"执行失败(102) -> {plugin.__name__} -> {methodName} -> {res.kwargs}")
                    continue
                
                if status == True:
                    print(f"{methodName}: {status}")
                    #self.log.info(f"执行成功(200) -> {plugin.__name__} -> {methodName} -> {res.kwargs}")
                    # break 这个只会跳出一层循环
                    return None
        # 打印日志
        self.showDatabaseMessage(data)


    
    def main(self):
        # 包装消息实体类
        self.messageBean = MessageBean(self.request.data)

        # 元事件
        # self.applicationContext.plugins_cq["0"]

        # 事件
        # self.applicationContext.plugins_cq["1"]

        # 请求
        # self.applicationContext.plugins_cq["2"]

        # 消息
        # self.applicationContext.plugins_cq["3"]

        # 元事件, 事件, 请求: TODO
        if self.messageBean.type == MessageBeanType.META_EVENT: 
            if self.funMetaEvent() == False: return None
        if self.messageBean.type == MessageBeanType.NOTICE: self.funNotice()
        if self.messageBean.type == MessageBeanType.REQUEST: self.funRequest()

        # 消息
        if self.messageBean.type == MessageBeanType.MESSAGE:
            # 特殊情况: 抖一抖, 分享(app), 视频, 语音, 图片, 被@, 被回复, QQ表情
            if not self.funSpecial(): self.funMessage()

        # 发送信息
        if self.requestContext.isTriggerModule != "CQTest":
            self.sendMessage()
        
        # 返回数据
        SocketUtil.sendAll(self.request, self.response)

        if self.requestContext.isTriggerModule == "CQTest":
            SocketUtil.close(self.request)