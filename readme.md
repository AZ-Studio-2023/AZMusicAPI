# AZMusicAPI
轻松访问音乐信息和歌曲音频链接 | Easy access to music information and song audio links

# AZ Studio版权所有
# 该项目仅供娱乐 请勿用于违法事业 违者与AZ Studio无关

# 安装

```pip install AZMusicAPI```

# AZMusicAPI模块使用指南

```
AZMusicAPI.getmusic(keyword)
```

## 作用：获得指定关键词的歌曲

* keyword：关键词

* 关键词可为 歌手/歌曲名/专辑名

### 返回值说明：正常返回列表  "Error 0"：没有结果 "Error 1":用户未输入

```
AZMusicAPI.geturl(rid,reqId)
```

## 作用：获取音乐的音频地址

* rid:你要解析的歌曲在getmusic返回的rid    
* reqId:你要解析的歌曲在getmusic返回的reqId

### 返回值：正常返回音频链接 "Error 3":歌曲需要单曲付费或rid/reqId不正确

## 代码示例
#### 仅需7行代码即可完成一个音乐音频地址获取器

```
import AZMusicAPI as MusicAPI 
u=input("请输入您需要的歌曲名称：")
data=MusicAPI.getmusic(u)
song=data[0]["songname"]
singer=data[0]["singer"]
print("歌曲名：{}  歌手：{}".format(song,singer))
print(MusicAPI.geturl(data[0]["rid"],data[0]["reqId"]))
```
