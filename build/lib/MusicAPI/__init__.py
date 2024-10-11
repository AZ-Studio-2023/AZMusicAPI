import requests

# AZ Studio版权所有
# 该项目仅供娱乐 请勿用于违法事业 违者与AZ Studio无关

def getmusic(keyword):
    #获得指定关键词的歌曲 关键词可为 歌手/歌曲名/专辑名
    #keyword：关键词
    #返回值说明：正常返回列表  "Error 0"：没有结果 "Error 1":用户未输入
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690028471; _ga=GA1.2.291025627.1690028471; _gid=GA1.2.1906759595.1690028471; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690028564; _gat=1; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=WjT5ktibAJwfEFyQFeJAEFcTxpwYHCeK; _ga_ETPBRPM9ML=GS1.2.1690028471.1.1.1690028577.47.0.0",
        "Host": "www.kuwo.cn",
        "Referer": "https://www.kuwo.cn/search/list?key=%E7%AC%BC",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Secret": "09362e5991f0846bff719a26e1a0e0ac7bd0b3c9f8ab5fdf000c7b88ecfa727000a0ba6e",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    search_url = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
    search_data = {
        'key': keyword,
        'pn': '1',
        'rn': '20',
        'httpsStatus': '1',
        'reqId': '7d9e2c60-288a-11ee-9cdf-3f476f1ba25e',
        "plat":"web_www"
    }
    if len(keyword)>0:
        response_data = requests.get(search_url, params=search_data, headers=headers, timeout=20).json()
        songs_data = response_data['data']['list']
        if int(response_data['data']['total']) <= 0:
            return "Error 0"
        else:
            data=[]
            for i in range(len(songs_data)):      
                try:       
                    data.append({"songname":songs_data[i]['name'],"singer":songs_data[i]['artist'],"album":songs_data[i]['album'],"pic":songs_data[i]['albumpic'],"rid":songs_data[i]['rid'],"reqId":response_data['reqId']})
                except:
                    pass                                                                        
            return data
    else:
        return "Error 1"

def geturl(rid,reqId):
    #获取音乐的音频地址
    #rid:你要解析的歌曲在getmusic返回的rid reqId:你要解析的歌曲在getmusic返回的reqId
    #返回值：正常返回音频链接 "Error 3":歌曲需要单曲付费或rid/reqId不正确
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690028471; _ga=GA1.2.291025627.1690028471; _gid=GA1.2.1906759595.1690028471; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1690028564; _gat=1; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=WjT5ktibAJwfEFyQFeJAEFcTxpwYHCeK; _ga_ETPBRPM9ML=GS1.2.1690028471.1.1.1690028577.47.0.0",
        "Host": "www.kuwo.cn",
        "Referer": "https://www.kuwo.cn/search/list?key=%E7%AC%BC",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Secret": "09362e5991f0846bff719a26e1a0e0ac7bd0b3c9f8ab5fdf000c7b88ecfa727000a0ba6e",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    music_url = 'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId={}&plat=web_www&from='.format(rid, reqId)
    response_data = requests.get(music_url,headers=headers).json()
    try:
        song_url = response_data['data'].get('url')
    except:
        return "Error 3"
    return song_url
