# 介绍
项目依赖于gocq-http  

0.处理流程
```text
QQ -> gocqhttp -> RQ(server) -> RQ(conn -> request)
↓
dispatcher
↓
-> event(h5) -> plugins -> function(api)
-> event(cq) -> plugins -> function(api)
↓
response(result)
```

1.TODO
```text
1.CQ模块            事件, 特殊消息解析
2.CQ模块            自定义事件
3.CQ模块            新版API
4.@mapping          增加全匹配模式
5.@order            咕咕咕
6.@chat_group       咕咕咕
7.@chat_private     咕咕咕
8.@jurisdiction     咕咕咕
9.bootstrap.json    咕咕咕
```


# 使用方法
0.配置python
[python 3.8.10](https://www.python.org/)

1.下载gocq
[gocq下载地址](https://github.com/Mrs4s/go-cqhttp/releases)

2.配置gocq
[gocq文档](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)  

3.双击本项目中的Server.py即可运行


