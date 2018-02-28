import requests  
import re  
import sys
from bs4 import BeautifulSoup  
  
      
url="https://cnbtkitty.net"  
header={  
    "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",  
    "Accept-Encoding":"gzip, deflate, br",  
    "Accept-Language":"zh-CN,zh;q=0.9",  
    "Cache-Control":"max-age=0",  
    "Connection":"keep-alive",  
    "Content-Length":"65",  
    "Content-Type":"application/x-www-form-urlencoded",  
    "Host":"cnbtkitty.net",  
    "Referer":"cnbtkitty.net",  
    "Upgrade-Insecure-Requests":"1",  
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

while True:  
    word=input("输入搜索关键词:\n->")  
    data={  
        "keyword":word,  
        "hidden":"true"  
        }  
    res=requests.post(url,data=data,headers=header)  
    #print(res.url)
    bs=BeautifulSoup(res.text,"lxml")  
    itemInfo=bs.find_all("dd",class_="option")  
    torrent={} 
    for item in itemInfo:  
        magnet=item.find_next("a",href=re.compile("magnet.*")).attrs["href"]  
        name=item.find_previous("a",href=re.compile("cnbtkitty.net/.*\.html")).text  
        size=item.find_next(text=re.compile("\u6587\u4ef6\u5927\u5c0f")).find_next("b").text  
        time=item.find_next(text=re.compile("\u6536\u5f55\u65f6\u95f4")).find_next("b").text  
        hot=item.find_next(text=re.compile("\u4eba\u6c14")).find_next("b").text  
       # torrent[name]=[name,time,size,hot,magnet]  
        print("名称：",name)  
        print("发布时间：",time)  
        print("大小：",size)  
        print("热度：",hot)  
        print("磁力链接：",magnet,'\n')     
    ex = input("输入-1结束程序，若继续搜索请输入除-1外任意内容\n->")
    if (ex == "-1"):
        exit()
'''
for item in torrent:  
    print("名称：",torrent[item][0])  
    print("发布时间：",torrent[item][1])  
    print("大小：",torrent[item][2])  
    print("热度：",torrent[item][3])  
    print("磁力链接：",torrent[item][4],'\n')     
    '''