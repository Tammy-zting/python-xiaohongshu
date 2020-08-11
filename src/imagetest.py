#coding=utf-8
# import ssl
import re
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

#获取页面信息
def getHtml(url):
    #Urllib 模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据。
    # response = urllib.request.urlopen(request)
    # page_html= response.read()
    # page_soup = urllib.request(page_html, "html.parser")
    # print (page_soup)
    # return page_soup

    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE

    # request = Request(url)
    response = urlopen(url)
    print(response)
    page_html = response.read()
    print(page_html)
    page_soup = soup(page_html, "html.parser")
    return page_soup

#获取图片并下载
def getImg(html):
    #正则筛选信息 下面的正则是根据小红书自己定义的 如果要抓取其他的 要自行根据规则修改
    reg = r'style="background-image:url\((\/\/.+?)\)\;"'  
    imgre = re.compile(reg)
    #读取html中符合我们正则表达式的数据
    imglist = re.findall(imgre,html)
    print (imglist)
    #循环访问图片地址保存到本地
    x= 0
    for imgurl in imglist:
       
        try:
            pic = requests.get("http:" + imgurl, timeout=10)

        except requests.exceptions.ConnectionError:
            print('error！！')
            continue
        dir = '../images/'+ str(x) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        x += 1

    if len(imglist) > 0 :
        print ('download success!!')
    else :
        print ('Error!! refresh your web url!!')
    
# 例如输入=》"https://www.xiaohongshu.com/discovery/item/592eb73114de411fb5c7a6b0?appinstall=0"  记住输入时要带双引号
url = input('Input url:')

html = getHtml(url)  

getImg(html)