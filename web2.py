# web2.py
#웹 서버와 통신
from typing import Text
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup
#파일에 저장
f= open("c:\\work\\webtoon.txt","wt",encoding="utf-8")

#페이징 처리가 된 경우
for i in range(1,6):
   url="http://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" +str(i)
   data = urllib.request.urlopen(url)

#검색을 할 객체를 생성
soup = BeautifulSoup(data, "html.parser")
# <td class="title">
# <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" >마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td",class_="title")
# print("갯수:{0}".format(len(cartoons)))
# title = cartoons[0].find("a").Text
# link = cartoons[0].find("a")["href"]
# print(title)
# print(link)
#전체 리스트
for item in cartoons:
    title = item.find("a").text
    print(title.strip())
    f.write(title.strip()+"\n")

f.close()