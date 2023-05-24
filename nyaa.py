from pyrogram import Client
import time, requests, feedparser
from pyrogram import Client
from bs4 import BeautifulSoup

dic = {'aa': [0,[],[],'https://nyaa.si/?page=rss&u=AkihitoSubsWeeklies'],
       'bb': [0,[],[],'https://nyaa.si/?page=rss&q=%5Bproject-gxs%5D&c=0_0&f=0'], 
       'cc': [0,[],[],'https://nyaa.si/?page=rss&u=Ember_Encodes'], 
       'dd': [0,[],[],'https://nyaa.si/?page=rss&q=%5BOhys-Raws%5D+BD&c=0_0&f=0'], 
       'ee': [0,[],[],'https://nyaa.si/?page=rss&q=judas+batch&c=0_0&f=0'],
       'gg': [0,[],[],'https://nyaa.si/?page=rss&q=Uncensored&c=0_0&f=0&u=sff'],
       'hh': [0,[],[],'https://nyaa.si/?page=rss&u=Uruz7Laevatein'],
       'ii': [0,[],[],'https://nyaa.si/?page=rss&u=animencodes'],
       'jj': [0,[],[],'https://nyaa.si/?page=rss&u=Commie'],
       'kk': [0,[],[],'https://nyaa.si/?page=rss&u=Tenrai_Sensei'],
       'll': [0,[],[],'https://nyaa.si/?page=rss&u=seelevollerei'],
       'mm': [0,[],[],'https://nyaa.si/?page=rss&u=yakubo'],
       'nn': [0,[],[],'https://nyaa.si/?page=rss&u=Cerberus'],
       'oo': [0,[],[],'https://nyaa.si/?page=rss&u=matsayajinms'],
       'pp': [0,[],[],'https://nyaa.si/?page=rss&q=%5Bbonkai77%5D&c=0_0&f=0'],
       'qq': [0,[],[],'https://nyaa.si/?page=rss&u=JRR'],
       'rr': [0,[],[],'https://nyaa.si/?page=rss&u=ThatWaxEllo'],
       'ss': [0,[],[],'https://nyaa.si/?page=rss&q=%5BiFU%5D&c=0_0&f=0'],
       'tt': [0,[],[],'https://nyaa.si/?page=rss&u=GuoManTeam'],
       'uu': [0,[],[],'https://nyaa.si/?page=rss&u=Squiggy'],
       'vv': [0,[],[],'https://nyaa.si/?page=rss&u=Sauron'],
       'ww': [0,[],[],'https://nyaa.si/?page=rss&u=GuodongSubs'],
       'yy': [0,[],[],'https://nyaa.si/?page=rss&u=VipapkStudios'],
       'zz': [0,[],[],'https://nyaa.si/?page=rss&u=sxales'],}



def nyaa():        
    while(True):
        try:
            for i in dic:
                time.sleep(10)
                all = dic[i]
                nyaa = feedparser.parse(all[3])
                for item in nyaa.entries:
                    all[1].append(item.link)
                all[1] = list(set(all[1]))
                if all[0] == 0:
                    all[2] = all[1].copy()
                    all[0] = 1
                elif all[0] == 1:
                    for loop in range(len(all[1])):
                        number = all[1].pop(0)
                        if number not in all[2]:
                            all[2].append(number)
                            print(number) 
        except Exception as e:
            print(e)
            #time.sleep(int(str(e).split("A wait of ")[1].split(" seconds is")[0]))
            pass
