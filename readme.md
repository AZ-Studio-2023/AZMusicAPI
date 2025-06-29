# AZMusicAPI
轻松访问音乐信息和歌曲音频链接 | Easy access to music information and song audio links

### AZ Studio版权所有
### 该项目仅供娱乐 请勿用于违法事业 违者与AZ Studio无关
# AZMusicAPI模块使用指南

## 安装

```pip install AZMusicAPI```

## 导入

``` import AZMusicAPI```

## 函数使用

### 获得指定关键词的歌曲

```AZMusicAPI.getmusic(keyword,api,cookie,number,server)```


* keyword：关键词 number:返回歌曲数量,可选,默认20 api:自行部署音乐服务器的地址，bili无需 cookie:访问API携带的Cookie，可选 server: 使用的API（可选，默认ncma。可选值：ncma，qqma，bili）

* 关键词可为 歌手/歌曲名/专辑名  bili通道不可以为BV号！！

#### 返回值类型：列表  
### 获取音乐的音频地址

```geturl(id,api,cookie,server)```

* id：歌曲ID api：自行部署API的地址 cookie:访问API携带的Cookie，可选 server: 使用的API（可选，默认ncma。可选值：ncma，qqma）

> bili通道不支持！请自行使用其他库编写


* id：歌曲的id

#### 返回值类型：字符串 


## 错误返回
* "Error 0"：没有结果 
* "Error 1":用户未输入
* "NetworkError":网络错误 / 服务器宕机 / IP被封禁


