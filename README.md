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


# 配置步骤
0.配置python  
[python 3.8.10](https://www.python.org/)  
Tips: 也可使用相差不大的版本

1.下载gocq  
[gocq下载地址](https://github.com/Mrs4s/go-cqhttp/releases)

2.配置gocq  
[gocq文档](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)  
Tips: 一定要配置config.yml中的http通信设置(为post添加url, 本地+5701端口)
```yaml
servers:
  - http: # HTTP 通信设置
      address: 0.0.0.0:5700 # HTTP监听地址
      timeout: 5      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
        - url: http://127.0.0.1:5701/
          max-retries: 0         # 最大重试，0 时禁用
```

3.运行本项目中的Server.py文件


