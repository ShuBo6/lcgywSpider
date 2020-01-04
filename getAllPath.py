# -- coding:UTF-8 --
import requests
from bs4 import BeautifulSoup
import json
import os

'''
思路：获取网址
      获取图片地址
      爬取图片并保存
'''
# headers = {
#     "cookie": "YOUR_COOKIE",
#     'upgrade-insecure-requests': "1",
#     'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
#     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     'cache-control': "no-cache",
# }

# 主函数
if __name__ == '__main__':
    # read = requests.get("http://blog.sina.com.cn/s/articlelist_3266811917_0_1.html")  # 获取url1
    read = requests.get("http://blog.sina.com.cn/s/articlelist_3266811917_0_2.html")
    read.raise_for_status()  # 状态响应 返回200连接成功
    read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
    html_url = read.text
    soup = BeautifulSoup(html_url, "html.parser")
    all_url = soup.find('div', class_='articleList').find_all('a')
    dict = {}
    src = '['
    for a in all_url:
        src += '\"'
        src += a['href']
        src += "\",\n"
        dict[a.string] = src
        # resultlist.append()
    src += "]"
    print(src)
    print(dict)
    try:
        path = "getAllPath/"
        if not os.path.exists(path):  # 判断是否存在文件并下载img
            os.mkdir(path)
        if os.path.exists(path + "result.json"):
            os.remove(path + "result.json")
            print("文件已存在！")
            f = open(path + "result.json", "w")
            f.write(src)
            f.close()
            print("文件保存成功！")
        else:
            f = open(path + "result.json", "w")
            f.write(src)
            f.close()
            print("文件保存成功！")
    except:
        print("文件保存失败！")

# if __name__ == '__main__':
#     url = "http://blog.sina.com.cn/s/blog_c2b7980d01030ztr.html"
#     read = requests.get(url)  # 获取url
#     read.raise_for_status()  # 状态响应 返回200连接成功
#     read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
#     html_url = read.text
#     soup = BeautifulSoup(html_url, "html.parser")
#     # all_url = soup.find('div',class_='articleList').find_all('a')
#     title = soup.find('div', class_='articalTitle').find_all('h2')  # img为图片的标签
#     print(title[0].string)
