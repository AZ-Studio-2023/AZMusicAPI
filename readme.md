# AZMusicAPI
轻松访问音乐信息和歌曲音频链接 | Easy access to music information and song audio links

### AZ Studio版权所有
### 该项目仅供娱乐 请勿用于违法事业 违者与AZ Studio无关
> 这是过时的说明文档
# AZMusicAPI模块使用指南

## 安装

```pip install AZMusicAPI```

## 导入

``` import AZMusicAPI```

## 函数使用


```AZMusicAPI.getmusic(keyword,api,cookie,number)```

### 作用：获得指定关键词的歌曲

* keyword：关键词 number:返回歌曲数量,可选,默认20 api:自行部署neteasecloudmusicapi的地址 cookie:访问API携带的Cookie，可选 server: 使用的API（可选，默认ncma）

* 关键词可为 歌手/歌曲名/专辑名

### 返回值类型：列表  

```geturl(id,api,cookie,server)```

* id：歌曲ID api：自行部署API的地址 cookie:访问API携带的Cookie，可选 server: 使用的API（可选，默认ncma）

### 作用：获取音乐的音频地址

* id：歌曲的id

### 返回值类型：字符串 


## 错误返回
* "Error 0"：没有结果 
* "Error 1":用户未输入
* "NetworkError":网络错误 / 服务器宕机 / IP被封禁
* "Error 3":歌曲需要单曲付费或rid/reqId不正确


