import requests







qq = "2042136767"
robotQQ = "2803197643"
group = "123456789"

headers = {
    'Host': '127.0.0.1:5701', 
    'User-Agent': 'Test/1.0', 
    'Content-Type': 'application/json', 
    'X-Self-Id': robotQQ, 
    'Accept-Encoding': 'gzip'
    }
data = {
    'post_type': 'message', 
    'message_type': 'private', 
    'time': 1671806464, 
    'self_id': robotQQ, 
    'sub_type': 'friend', 
    'message_id': -332495319, 
    'user_id': qq, 
    'target_id': robotQQ, 
    'message': '', 
    'raw_message': '', 
    'font': 0, 
    'sender': {
        'age': 0, 'nickname': 'TEST', 'sex': 'unknown', 'user_id': qq
    }
}


while True:
    i = input("[text] ")

    data["message"] = i
    data["raw_message"] = i
    try:
        requests.post("http://localhost:5701", headers=headers, json=data, timeout=1)
    except:
        pass
