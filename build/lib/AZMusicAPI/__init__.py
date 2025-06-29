import re
from collections import Counter
import requests
from bilibili_api import search, sync, video_zone

# AZ Studio版权所有
# 该项目仅供学习研究 请勿用于违法事业 违者与AZ Studio无关

def extract_keyword(text):
    # 使用正则表达式提取所有<em class="keyword"></em>标签中的内容
    keywords = re.findall(r'<em class="keyword">(.*?)</em>', text)

    # 如果有书名号格式的标签，优先返回其中的内容
    for keyword in keywords:
        if '《' in keyword and '》' in keyword:
            return keyword

    # 如果没有书名号格式的标签，返回出现最多的关键词
    if keywords:
        most_common_keyword = Counter(keywords).most_common(1)[0][0]
        return most_common_keyword

    # 如果没有关键词，返回空字符串
    return ""

async def search_by_order(keyword, num):
    return await search.search_by_type(
        keyword,
        search_type=search.SearchObjectType.VIDEO,
        order_type=search.OrderVideo.SCORES,
        time_range=10,
        video_zone_type=video_zone.VideoZoneTypes.MUSIC,
        page=num,
    )

def min_multiples_to_exceed(n):
    multiplier = 1
    while 17 * multiplier <= n:
        multiplier += 1
    return multiplier

def getmusic(keyword, api, cookie="", number=20, server="ncma"):
    number = int(number)
    headers = {
        'Cookie': cookie
    }
    # 获得指定关键词的歌曲 关键词可为 歌手/歌曲名/专辑名
    # keyword：关键词 number:返回歌曲数量,可选,默认20 api:自行部署ncma或qqma的地址，bili留空
    # server：可选，默认ncma，可选值：ncma，qqma，bili
    # 返回值说明：正常返回列表  "Error 0"：没有结果 "Error 1":用户未输入
    search_url = api + "search"
    if server == "ncma":
        search_data = {"keywords": keyword}
        if len(keyword) > 0:
            try:
                response_data = requests.get(search_url, params=search_data, timeout=20, headers=headers).json()
            except:
                return "NetworkError"
            songs_data = response_data['result']['songs']
            if len(response_data['result']['songs']) <= 0:
                return "Error 0"
            else:
                data = []
                try:
                    for i in range(len(songs_data)):
                        artists = ""
                        for y in range(len(songs_data[i]["artists"])):
                            if y != 0:
                                artists = artists + ","
                            artists = artists + songs_data[i]["artists"][y]["name"]
                        data.append({"id": songs_data[i]['id'], "name": songs_data[i]['name'], "artists": artists,
                                     "album": songs_data[i]['album']["name"]})
                except:
                    data.append({"id": '-1', "name": 'error', "artists": 'error',
                                 "album": 'error'})
                if len(data) > number:
                    data = data[:number]
                return data
        else:
            return "Error 1"
    elif server=="bili":
        pages = min_multiples_to_exceed(number)
        if len(keyword) > 0:
            try:
                res = sync(search_by_order(keyword, pages))
            except:
                return "NetworkError"
            try:
                ret = res["result"]
            except:
                return "Error 0"
            if len(ret) <= 0:
                return "Error 0"
            else:
                data = []
                try:
                    for i in ret:
                        data.append({"id": i["bvid"], "name": extract_keyword(i["title"]), "artists": str(i["author"]).replace("《", "").replace("》", ""),"album": str(i["title"]).replace('<em class="keyword">', "").replace('</em>', "")})
                except:
                    data.append({"id": '-1', "name": 'error', "artists": 'error',
                                 "album": 'error'})
                if len(data) > number:
                    data = data[:number]
                return data

    else:
        if len(keyword) == 0:
            return "Error 1"
        search_data = {"key": keyword, "pageSize": number}
        try:
            data = requests.get(search_url, params=search_data, timeout=20).json()
        except:
            return "NetworkError"
        if data["result"] != 100:
            return "Error 1"
        else:
            data_r = []
            for i in data["data"]["list"]:
                artists = ''
                for j in range(len(i["singer"])):
                    if j == 0:
                        artists = i["singer"][j]["name"]
                    else:
                        artists = artists + i["singer"][j]["name"]

                data_r.append({"id": i["songmid"], "name": i["name"], "album": i["albumname"], "artists": artists})
        return data_r


def geturl(id, api, cookie="", server="ncma", level="standard"):
    # 获取音乐的音频地址
    # id:歌曲的id值 level:返回音频的音质，仅NCMA api:自行部署ncma或qqma的地址，bili留空
    # server：可选，默认ncma，可选值：ncma，qqma
    # bili渠道不能走这里
    # 返回值：正常:返回音频链接  "Error 3":id不正确或无版权  "Error 4":获取链接失败，建议检查是否登录
    headers = {
        'Cookie': cookie
    }
    if server == "ncma":
        search_url = api + "song/url/v1"
        search_data = {"id": id, "level": level}
        try:
            response_data = requests.get(search_url, params=search_data, headers=headers).json()
        except:
            return "NetworkError"
        try:
            song_url = response_data['data'][0]["url"]
        except:
            return "Error 3"
        return song_url
    else:
        search_url = api + "song/urls"
        search_data = {"id": id}
        try:
            response_data = requests.get(search_url, params=search_data).json()
        except:
            return "NetworkError"
        if response_data["result"] != 100:
            return "Error 4"
        try:
            song_url = response_data['data'][id]
        except:
            return "Error 3"
        return song_url

