import requests


class APIPRO:
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:5700"
        self.uri = ""
        self.params = {}
        # TODO
        '''
        send_private_msg        发送私聊消息            鸡肋
        send_group_msg          发送群消息              鸡肋
        send_group_forward_msg  发送合并转发(群)        懒得写
        get_msg                 获取消息                鸡肋
        get_forward_msg         获取合并转发内容        懒得写
        get_image               获取图片信息            懒得写
        mark_msg_as_read        标记消息已读            鸡肋
        set_group_anonymous     群组匿名                gocq暂未支持
        qidian_get_account_info 获取企点账号信息        只有企点协议可用
        get_cookies             获取 Cookies            gocq暂未支持
        get_csrf_token          获取 CSRF Token         gocq暂未支持
        get_credentials         获取 QQ 相关接口凭证    gocq暂未支持
        get_record              获取语音                gocq暂未支持
        clean_cache             清理缓存                gocq暂未支持

        # 获取群图片, group_id 为群号
        https://p.qlogo.cn/gh/{group_id}/{group_id}/100
        '''
    
    def send(self, method="GET"):
        if method == "GET": 
            return requests.get(f"{self.url}/{self.uri}", self.params)

        return False

    # 发送消息 -> message_id
    def send_msg(self, message_type: str, user_id: int, group_id: int, message: str, auto_escape=False): 
        self.uri = "send_msg"
        self.params = {
            "message_type": message_type,
            "user_id": user_id,
            "group_id": group_id,
            "message": message,
            "auto_escape": auto_escape
        }
        return self.send()

    # 撤回消息 -> None
    def delete_msg(self, message_id: int): 
        self.uri = "delete_msg"
        self.params = {
            "message_id": message_id
        }
        return self.send()

    # 群组踢人 -> None
    def set_group_kick(self, group_id:int, user_id:int, reject_add_request=False): 
        self.uri = "set_group_kick"
        self.params = {
            "group_id": group_id,
            "user_id": user_id,
            "reject_add_request": reject_add_request
        }
        return self.send()

    # 群组单人禁言 -> None
    def set_group_ban(self, group_id:int, user_id:int, duration=1800): 
        self.uri = "set_group_ban"
        self.params = {
            "group_id": group_id,
            "user_id": user_id,
            "duration": duration,
        }
        return self.send()

    # 群组匿名用户禁言 -> None
    def set_group_anonymous_ban(self, group_id: int, flag, duration=1800): 
        self.uri = "set_group_anonymous_ban"
        self.params = {
            "group_id": group_id,
            "flag": flag,
            "duration": duration,
        }
        return self.send()

    # 群组全员禁言 -> None
    def set_group_whole_ban(self, group_id, enable=True): 
        self.uri = "set_group_whole_ban"
        self.params = {
            "group_id": group_id,
            "enable": enable,
        }
        return self.send()
    
    # TODO: 群组设置管理员 -> None
    def set_group_admin(self): 
        self.uri = "set_group_admin"
        self.params = {
        }
        return self.send()
        
    # 设置群名片 -> None
    def set_group_card(self): 
        self.uri = "set_group_card"
        self.params = {
        }
        return self.send()
        
    # 设置群名 -> None
    def set_group_name(self): 
        self.uri = "set_group_name"
        self.params = {
        }
        return self.send()
        
    # 退出群组 -> None
    def set_group_leave(self): 
        self.uri = "set_group_leave"
        self.params = {
        }
        return self.send()
        
    # 设置群组专属头衔 -> None
    def set_group_special_title(self): 
        self.uri = "set_group_special_title"
        self.params = {
        }
        return self.send()
        
    # 群打卡 -> None
    def send_group_sign(self): 
        self.uri = "send_group_sign"
        self.params = {
        }
        return self.send()

    # 处理加好友请求 -> None
    def set_friend_add_request(self): 
        self.uri = "set_friend_add_request"
        self.params = {
        }
        return self.send()
        
    # 处理加群请求/邀请 -> None
    def set_group_add_request(self): 
        self.uri = "set_group_add_request"
        self.params = {
        }
        return self.send()
        
    # 获取登录号信息 -> user_id, nickname
    def get_login_info(self): 
        self.uri = "get_login_info"
        self.params = {
        }
        return self.send()    

    # 设置登录号资料 -> None
    def set_qq_profile(self): 
        self.uri = "set_qq_profile"
        self.params = {
        }
        return self.send()
        
    # 获取陌生人信息 -> user_id, nickname, sex, age, qid, qid, login_days
    def get_stranger_info(self): 
        self.uri = "get_stranger_info"
        self.params = {
        }
        return self.send()
                
    # 获取好友列表 -> user_id, nickname, remark
    def get_friend_list(self): 
        self.uri = "get_friend_list"
        self.params = {
        }
        return self.send()
                
    # 获取单向好友列表 -> user_id, nickname, source
    def get_unidirectional_friend_list(self): 
        self.uri = "get_unidirectional_friend_list"
        self.params = {
        }
        return self.send()
                
    # 删除好友 -> None
    def delete_friend(self): 
        self.uri = "delete_friend"
        self.params = {
        }
        return self.send()

    # 获取群信息 -> group_id, group_name, group_memo, group_create_time, group_level, member_count, max_member_count
    def get_group_info(self): 
        self.uri = "get_group_info"
        self.params = {
        }
        return self.send()

    # 获取群列表 -> [get_group_info, get_group_info...]
    def get_group_list(self): 
        self.uri = "get_group_list"
        self.params = {
        }
        return self.send()

    # 获取群成员信息 -> group_id, user_id, nickname, card, sex, age, area, join_time, last_sent_time, level, role, unfriendly, title, title_expire_time, card_changeable, shut_up_timestamp
    def get_group_member_info(self): 
        self.uri = "get_group_member_info"
        self.params = {
        }
        return self.send()

    # 获取群成员列表 -> [get_group_member_info, get_group_member_info...]
    def get_group_member_list(self): 
        self.uri = "get_group_member_list"
        self.params = {
        }
        return self.send()

    # 获取群荣誉信息 -> TODO
    def get_group_honor_info(self): 
        self.uri = "get_group_honor_info"
        self.params = {
        }
        return self.send()

    # 检查是否可以发送图片 -> yes
    def can_send_image(self): 
        self.uri = "can_send_image"
        self.params = {
        }
        return self.send()

    # 检查是否可以发送语音 -> yes
    def can_send_record(self): 
        self.uri = "can_send_record"
        self.params = {
        }
        return self.send()

    # 获取版本信息 -> TODO
    def get_version_info(self): 
        self.uri = "get_version_info"
        self.params = {
        }
        return self.send()

    # 重启 go-cqhttp -> None
    def set_restart(self, delay: 2000): 
        self.uri = "set_restart"
        self.params = {
            "delay": delay
        }
        return self.send()

    # 设置群头像 -> None
    def set_group_portrait(self): 
        self.uri = "set_group_portrait"
        self.params = {
        }
        return self.send()

    # template -> None
    def template(self): 
        self.uri = "template"
        self.params = {
        }
        return self.send()

    # template -> None
    def template(self): 
        self.uri = "template"
        self.params = {
        }
        return self.send()

    # template -> None
    def template(self): 
        self.uri = "template"
        self.params = {
        }
        return self.send()

    # template -> None
    def template(self): 
        self.uri = "template"
        self.params = {
        }
        return self.send()

    # template -> None
    def template(self): 
        self.uri = "template"
        self.params = {
        }
        return self.send()


