import requests
import telebot
import user_agent
import uuid
from uuid import uuid4
from telebot import types
import os
from json import dumps
from user_agent import generate_user_agent
from time import sleep

token = input("5569138339:AAFPifJL8KvfHAjwIjyVx6EzMMlGrwWvPmw")
bot = telebot.TeleBot(token)

url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    'Accept': "*/*",
    'Cookie': 'missing',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-Connection-Type': 'WIFI',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com'}
b1  = types.InlineKeyboardButton(text="- Auto Story Watch ⚜️.",callback_data="w")
b2 = types.InlineKeyboardButton(text="- Delete Chats ⚜️.",callback_data="d")
b3 = types.InlineKeyboardButton(text="- Delete Following ⚜️.",callback_data="df")
b4 = types.InlineKeyboardButton(text="- Auto Follow From List ⚜️.",callback_data="af")
b5 = types.InlineKeyboardButton(text="- Auto Post Delete ⚜️.",callback_data="dp")
b6 = types.InlineKeyboardButton(text="- Get Users From Word ⚜️.",callback_data="g")
b7 = types.InlineKeyboardButton(text='- Get Your Acount Info ⚜️.',callback_data="us")
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,text=f"<strong>- ⚜️ Hi ,\n================\n- 🔶 To Login Now You Need To Something!💯\n- 🔶 Send Your Username Now!✅\n================\n- @trprogram</strong>",parse_mode="html")

@bot.callback_query_handler(func=lambda call:True)
def qwO(call):
    if call.data == "w":
        wt(call.message)
    if call.data == "d":
        dt(call.message)
    if call.data == "df":
        df(call.message)
    if call.data == "af":
        af(call.message)
    if call.data == "dp":
        dp(call.message)
    if call.data == "g":
        g(call.message)
    if call.data == "us":
        rep(call.message)
@bot.message_handler(func=lambda m: True)
def mounth(message):
    global msg1, sent
    msg1 = message.text
    sent = bot.send_message(message.chat.id, text=f"<strong>- Send Password Now!</strong>", parse_mode="html")
    bot.register_next_step_handler(sent, send)


def send(message):
    global key , cookie , csrf , coo , ms , pp , msg1
    ms = msg1
    pp = message.text
    uid = str(uuid4())
    data = {
        "password": pp,
        "username": msg1,
        "device_id": uid,
        "from_req": "false",
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }
    req = requests.post(url, headers=headers, data=data)
    print(req.text)
    if 'logged_in' in req.text:
        rw = req.cookies
        coo = rw.get_dict()
        csrf = coo['csrftoken']
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
        with open("cookies.txt","w")as x:
            x.write(f"{cookie}")
            x.close()
        key = types.InlineKeyboardMarkup()
        key.row_width = 1
        key.add(b1,b2,b3,b4,b5,b6,b7)
        bot.send_message(message.chat.id,f"<strong>Hello Sir , Your Account Control .</strong>",parse_mode="html",reply_markup=key)
    if 'challenge_required' in req.text:
        bot.send_message(message.chat.id, f"<strong>Done Login Sir , But Secureid Account ..</strong>",parse_mode="html")
    if "bad_password" in req.text:
        bot.send_message(message.chat.id, f"<strong>Error Login Sir .</strong>", parse_mode="html")
    else:
        pass
def wt(message):
    get_id = f'https://www.instagram.com/{msg1}/?__a=1'
    re = requests.get(get_id, cookies=coo).json()
    idd = re['logging_page_id'].split('_')[1]
    count = str(re['graphql']['user']['edge_follow']['count'])
    option = 'following'
    url = f'https://i.instagram.com/api/v1/friendships/{idd}/{option}/?count={count}'

    hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': cookie,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
        'x-asbd-id': '437806',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',
    }

    xx = requests.get(url, headers=hed).json()['users']

    for ig in xx:
        uuss = ig['username']
        try:
            hid = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'cookie': cookie,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
            }
            s = f'https://www.instagram.com/{uuss}/?__a=1'
            x = requests.get(s, headers=hid).json()
            iid = x['logging_page_id'].split('_')[1]
            surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{iid}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
            xx = requests.get(surl, headers=hid).json()
            story_count = len(xx["data"]["reels_media"][0]["items"])
            for i in range(0, story_count):
                id_story = xx["data"]["reels_media"][0]["items"][i]['id']
                taken_at_timestamp = xx["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
                stories_page = f"https://www.instagram.com/stories/reel/seen"
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '127',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': cookie,
                    "origin": "https://www.instagram.com",
                    "referer": f"https://www.instagram.com/stories/{uuss}/{id_story}/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "x-csrftoken": csrf,
                    "x-ig-app-id": "936619743392459",
                    "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                    "x-instagram-ajax": "d3d3aea32e75",
                    "x-requested-with": "XMLHttpRequest"
                }

                data = {
                    'reelMediaId': id_story,
                    'reelMediaOwnerId': iid,
                    'reelId': iid,
                    'reelMediaTakenAt': taken_at_timestamp,
                    'viewSeenAt': taken_at_timestamp
                }
                hn = 0
                v=0
                fx = 0
                xxx = requests.request("POST", stories_page, headers=headers, data=data).status_code
                if xxx == 200:
                    v +=1
                    bot.send_message(message.chat.id,f"Done Watch {uuss} Story!")


        except:
            pass
def dt(message):
    alll = 0
    while True:
        alll += 1
        urinbox = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
        hed1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid=' +coo['sessionid'],
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'
        }
        start = requests.get(urinbox, headers=hed1)
        try:
            fothr = str(start.json()['inbox']['threads'][0]['thread_id'])
            foothr = str(start.json()['inbox']['threads'][0]['users'][0]['username'])
            url1 = 'https://i.instagram.com/api/v1/direct_v2/threads/{}/hide/'.format(fothr)
            hed1 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid=' +coo['sessionid'],
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
                'x-instagram-ajax': '753ce878cd6d'}

            start = requests.post(url1, headers=hed1)

            if '"status":"ok"' in start.text:
                bot.send_message(message.chat.id,f"Done Delete {fothr} Chat!")
            else:
                bot.send_message(message.chat.id,f"You Are BLocked!!!")
        except IndexError:
            bot.send_message(message.chat.id,f"Done Delete All Chats Sir!")
            send(message)
def df(message):
    hid = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
    }
    s = f'https://www.instagram.com/{msg1}/?__a=1'
    x = requests.get(s, headers=hid).json()
    idd = x['logging_page_id'].split('_')[1]
    while True:
        cook = coo['sessionid']
        tok = 'd04b0a864b4b54837c0d870b0e77e076'
        cookies = {"sessionid": cook, }

        variables = {"id": idd, "first": 50}

        params = {"query_hash": tok, "variables": dumps(variables)}

        req1 = requests.get("https://www.instagram.com/graphql/query/", params=params, cookies=cookies)
        try:
            foId = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['id'])
            foou = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['username'])
            url = 'https://www.instagram.com/web/friendships/{}/unfollow/'.format(foId)

            hed1 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; sessionid=' + cook,
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{msg1}/following/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
                'x-instagram-ajax': '753ce878cd6d',
                'x-requested-with': 'XMLHttpRequest'}

            done = requests.post(url, headers=hed1)

            if '"status":"ok"' in done.text:
                bot.send_message(message.chat.id,f"<strong>Done Delete {foou}</strong>",parse_mode="html")
                sleep(16)
            elif 'Please' in done.text:
                bot.send_message(message.chat.id,f"<strong>Banned!</strong>",parse_mode="html")
            else:
                print(done.text)
        except IndexError:
            bot.send_message(message.chat.id,f"<strong> No Accounts Yet .</strong>",parse_mode="html")
def af(message):
    target = msg1
    try:
        accs = open('accounts.txt', 'r').read().splitlines()
    except:
        bot.send_message(message.chat.id,f"<strong>File accounts.txt Not Found!</strong>",parse_mode="html")
        send(message)
    for acc in accs:
        user = acc.split(':')[0]
        pasw = acc.split(':')[1]
        uid = str(uuid4())
        data = {
            "password": pasw,
            "username": user,
            "device_id": uid,
            "from_req": "false",
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'
        }
        dq = requests.post(url, headers=headers, data=data)
        if "logged_in" in dq.text:
            login = dq.cookies
            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
            hid = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'cookie': cookie,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
            }
            s = f'https://www.instagram.com/{target}/?__a=1'
            x = requests.get(s, headers=hid).json()
            idd = x['logging_page_id'].split('_')[1]
            url2 = f'https://www.instagram.com/web/friendships/{idd}/follow/'

            head2 = {
                'accept': '*/*',
                'accept-encoding': 'gzip,deflate,br',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://www.instagram.com',
                'referer': f'https://www.instagram.com/{target}/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': generate_user_agent(),
                'x-asbd-id': '437806',
                'x-csrftoken': coo['csrftoken'],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9Rcy',
                'x-instagram-ajax': '0019e974ed32',
                'x-requested-with': 'XMLHttpRequest',
            }
            try:
                follow = requests.post(url2, headers=head2, cookies=coo).text

                if '"status":"ok"' in follow:
                    bot.send_message(message.chat.id,f"<strong>Done Follow {msg1} By {user}!")
                    sleep(12)
                else:
                    pass
            except:
                pass
def dp(message):
    alll = 0
    while True:
        alll += 1
        ur = 'https://www.instagram.com/{}/?__a=1'.format(msg1)

        hedID = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cache-control': 'no-cache',
            'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid=' +
                      coo['sessionid'],
            'pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'
        }
        idu = requests.get(ur, headers=hedID)
        try:
            idd = idu.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['id']
            urld = 'https://www.instagram.com/create/{}/delete/'.format(idd)

            hed1 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid=' +
                          coo['sessionid'],
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/p/CM5_0EfBliscG9z8SJBY1iasqct_jP0jEJsNCU0/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEvg3',
                'x-instagram-ajax': '753ce878cd6d',
                'x-requested-with': 'XMLHttpRequest'}

            dlete = requests.post(urld, headers=hed1)
            if '"status":"ok"' in dlete.text:
                bot.send_message(message.chat.id,f"<strong>Done Delete {alll} !</strong>",parse_mode="html")
                sleep(16)
            else:
                bot.send_message(message.chat.id,f"<strong>Error</strong>",parse_mode="html")
        except IndexError:
            bot.send_message(message.chat.id,f"<strong>Done Delete ALL Posts</strong>",parse_mode="html")
            send(message)
def g(message):
    bot.send_message(message.chat.id,f"<strong>Wait .. Bot Working Now!</strong>",parse_mode="html")
    words = ("iraq-love-ukrane-russia-war-har-hear-about-king-usa-2013-2011-2010-best")
    for w in words.split('-'):
        w = w.replace(' ', '')
        url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.43773004634682566&include_reel=true'

        response = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'}).json()['users']

        for ig in response:
            with open("users1.txt","w")as x:
                x.truncate(0)
            user = ig['user']['username']
            file = open('users1.txt', 'a').write(f'{user}\n')
        users = len(open('users1.txt', 'r').read().splitlines())
        bb = open("users1.txt","r")

    bot.send_document(message.chat.id,bb,caption=f"Done Gen")
    with open("users1.txt", "w") as x:
        x.truncate(0)
        pass
bot.infinity_polling()