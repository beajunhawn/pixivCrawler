import urllib
import os
import sys
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse


#r = requests.get("http://www.pixiv.net/search.php?s_mode=s_tag&word=%E3%82%81%E3%81%90%E3%81%BF%E3%82%93")
#soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
#rint(soup.find_all('img'))
#print(soup.prettify)
class crawl():
    def urlCrawl(self, url):
        page = 1
        S = ''  # 해당 페이지의 소스
        urList = []  # 크롤링한 url리스트들
        while page < 2:
            Start_point = 0  # find 시작점
            r= urllib.request.Request.add_header();
            r = r.requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
            S = str(soup.prettify)
            while 1:
                if (S.find('href="http') == -1):
                    break
                Start_point = S.find('href="http') + 6
                S = S[Start_point:]
                End_point=S.find('"')
                print(End_point)
                urList.append(''+str(S[:End_point],'utf-8'))
            page+=1
        return urList
    def imgUrlCrawl(self, url):
        page = 1
        S = ''  # 해당 페이지의 소스
        urList = []  # 크롤링한 url리스트들
        while page < 5:
            U=url
            if page>1:
                U=str(url)+"&p="+str(page)
            Start_point = 0  # find 시작점
            session = requests.Session()
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                       }
            r = session.get(U, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
            S = str(soup.find_all("img"))
            while 1:
                if (S.find('data-src="') == -1):#data-src로 시작하는 부분을 찾은
                    break
                Start_point = S.find('data-src="') + 10
                S = S[Start_point:]#시작점부터
                if(S.find('.jpg"')==-1):
                    break
                End_point=S.find('.jpg"')
                print(End_point)
                urList.append(''+S[:End_point+4])#리스트에 추가
            page+=1
        return urList

    #사진을 다운로드하는 메소드
    def download_photo(self, img_url, filename):
        #"Host": "source.pixiv.net",
        file_path = "C://Users\배준환/Desktop/새 폴더/"+ filename+".jpg"
        headers = {"User-Agent": "Mozilla/5.0 (MSIE 11.0;Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Encoding":" gzip, deflate",
                   "Accept-Language":" ko, ja; q=0.5",
                   "Referer":"http://www.pixiv.net/search.php?s_mode=s_tag&word=%E3%82%81%E3%81%90%E3%81%BF%E3%82%93"}
        r = urllib.request.Request(img_url,headers=headers)
        img=urllib.request.urlopen(r).read()
        downImg=open(file_path,"wb")
        print(str(img))
        downImg.write(bytes(img))
        downImg.close()
        return file_path

#call
c= crawl()
urList=c.imgUrlCrawl("http://www.pixiv.net/search.php?s_mode=s_tag&word=%E3%82%81%E3%81%90%E3%81%BF%E3%82%93")
print(urList)
a=0
for i in urList:
    a+=1
    c.download_photo(i,str(a))