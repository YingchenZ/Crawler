# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import html.parser
import sqlite3

# 得到指定网页的内容 
def askURL(url):
    # 模拟浏览器向服务器发送消息
    head = {
        # 用户代理: 告诉服务器我们可以接受什么水平的文件内容
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
    }
    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "lxml")
        # 查找符合要求的字符串，形成列表
        for item in soup.find_all('div', class_ = "item"):
            data = []
            item = str(item)
            
            link = re.findall(findLink, item)[0]
            print(link)


    return datalist

def saveData(savepath):
    pass


findLink = re.compile(r'<a href="(.*?)">')
findName = re.compile(r'<span class="title">')
if __name__ == "__main__":
    # 目标网页
    baseurl = "https://movie.douban.com/top250?start="

   
    # 爬取网页
    datalist = getData(baseurl)

    # 保存数据
    # savepath = ".\\result.xls"
    # saveData(savepath)