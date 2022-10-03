import random
import urllib
import requests
from threading import Thread
import telebot,time
from telebot import types

views = 0
t = input(' ENTAR TOKEN BOT : ')
bot = telebot.TeleBot(t)

@bot.message_handler(commands=['start']) 
def start(message):
	topac = types.InlineKeyboardMarkup()
	top = types.InlineKeyboardButton("- Dev", url = "t.me/iiit5")
	topac.add(top)
	idph = f"https://t.me/{message.from_user.username}"
	bot.send_photo(message.chat.id,idph,'''
هلا حبي بوت انه بوت ادزلك مشاهدات للبوست مالتك
اكتب ارسل و رابط المنشور\nمثل :- ارسل https://t.me/m32bot/158
''', parse_mode="markdown",reply_markup=topac)

views = 0

https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0",
                     proxies=urllib.request.getproxies(), ).text
http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0",
                    proxies=urllib.request.getproxies(), ).text
prox_list = (https+http).split()
def send_seen(channel, msgid, proxy):
    s = requests.Session()
    proxies = {'http': proxy, 'https': proxy}
    try:
        a = s.get("https://t.me/"+channel+"/"+msgid,
                  timeout=10, proxies=proxies)
        cookie = a.headers['set-cookie'].split(';')[0]
    except Exception as e:
        return
    h1 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Content-Length": "5", "Content-type": "application/x-www-form-urlencoded",
          "Cookie": cookie, "Host": "t.me", "Origin": "https://t.me", "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome"}
    d1 = {"_rl": "1"}
    try:
        r = s.post('https://t.me/'+channel+'/'+msgid+'?embed=1',
                   json=d1, headers=h1, proxies=proxies)
        key = r.text.split('data-view="')[1].split('"')[0]
        now_view = r.text.split('<span class="tgme_widget_message_views">')[
            1].split('</span>')[0]
        if now_view.find("K") != -1:
            now_view = now_view.replace("K", "00").replace(".", "")
    except Exception as e:
        return
    h2 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me",
          "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome", "X-Requested-With": "XMLHttpRequest"}
    try:
        i = s.get('https://t.me/v/?views='+key, timeout=10,
                  headers=h2, proxies=proxies)
        if(i.text == "true"):
            print(' - عدد المشاهدات :'+now_view)
            views += 1
    except Exception as e:
        return
    try:
        h3 = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7",
              "Cache-Control": "max-age=0", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Chrome"}
        s.get("https://t.me/"+channel+"/"+msgid, headers=h3,
              timeout=10, proxies=proxies)
    except Exception as e:
        return

@bot.message_handler(func=lambda message: True)
def main(message):
	tt = random.randint(1,2314)
	url = f"https://t.me/AC2AA/{tt}"
	topac = types.InlineKeyboardMarkup()
	top = types.InlineKeyboardButton("- Dev", url = "t.me/iiit5")
	to = types.InlineKeyboardButton("- voice", url = url)
	
	topac.add(top,to)
	if message.text.startswith("ارسل "):
		link = message.text.replace('ارسل ', '')
		list = ["https","http", "://"]
		for e in list:
			if e in link:
					
					bot.send_audio(message.chat.id,url,"سيتم الرشق…",parse_mode="markdown",reply_markup=topac)
					for i in range(100000):
				  			try :
				  		  			time.sleep(float(0.1))
				  		  			th = Thread(target=send_seen, args=(link.split("/")[3], link.split("/")[4], random.choice(prox_list)))
				  		  			th.start()
				  			except:
		        						pass
					bot.reply_to(message,"تم الانتهاء من الرشق")
			else:
				bot.reply_to(message, "يرجى وضع رابط صحيح")

	else:
			bot.reply_to(message, "يرجى وضع رابط صحيح")		
bot.polling()