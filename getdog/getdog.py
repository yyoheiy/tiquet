from bs4 import BeautifulSoup
import urllib.request
import re

class Getdog:
    def __init__(self):
        self.url=("http://www.aomori-animal.jp/02_JOTO/INU/Joto.html")
    def getitems(self):
        html=urllib.request.urlopen(self.url)
        bs=BeautifulSoup(html,"html.parser")
        tr=bs.find_all("tr")
        tr.pop(0)
        lst=[]
        for i in tr:
            td=i.find_all("td")
            breed=td[1].string
            color=td[2].string
            sex=td[3].string
            memo=td[5].string
            img=i.find("img").get("src")
            items=[breed,color,sex,memo,img]
            lst.append(items)
        return lst
        
