# -- coding:UTF-8 --
import requests
from bs4 import BeautifulSoup
import os

'''
思路：获取网址
      获取图片地址
      爬取图片并保存
'''
headers = {
    "cookie": "YOUR_COOKIE",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'cache-control': "no-cache",
    }


# 获取网址
def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


# 获取图片地址并保存下载
def getPic(html):
    soup = BeautifulSoup(html, "html.parser")
    # 通过分析网页内容，查找img的统一父类及属性
    all_img = soup.find('div', class_='articalContent').find_all('img')  # img为图片的标签
    index = 0
    for img in all_img:
        index += 1
        src = img['real_src']  # 获取img标签里的src内容
        img_url = src
        # img_origin = "http://s15.sinaimg.cn/orignal/"
        img_origin = "http://album.sina.com.cn/pic/"
        img_name = img_url.split('/')[-1]
        print("img_url:"+img_url)
        root = "燕昭王求士/"  # 保存的路径
        path = root + img_name # 获取img的文件名
        filename = root + str(index)
        print("path:"+path)
        print("img_origin+name:"+img_origin + img_name)
        try:
            if not os.path.exists(root):  # 判断是否存在文件并下载img
                os.mkdir(root)
            if not os.path.exists(path):
                read = requests.get(img_origin + img_name, headers=headers, allow_redirects=False)
                new_url=read.headers['Location'].replace(".cn", ".in")
                print("new_url",new_url)
                read = requests.get(new_url, headers=headers)
                # with open(path, "wb")as f:
                with open(filename, "wb")as f:
                    f.write(read.content)
                    f.close()
                    print("文件保存成功！")
            else:
                print("文件已存在！")
        except:
            print("文件爬取失败！")


# 主函数
if __name__ == '__main__':
    html_url = getUrl("http://blog.sina.com.cn/s/blog_c2b7980d01030ztr.html")
    getPic(html_url)