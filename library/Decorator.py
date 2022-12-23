


# TODO: order
# 方法执行顺序
 
# TODO: chat_group && chat_private
# 仅限于群聊触发 && 仅限于私聊触发
 
# TODO: jurisdiction
# 权限 


# 判断指令, 并截取指令后的参数
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













