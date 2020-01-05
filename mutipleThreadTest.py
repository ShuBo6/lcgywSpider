# -- coding:UTF-8 --
import concurrent.futures
import requests
from bs4 import BeautifulSoup
import os

'''
思路：获取网址
      获取图片地址
      爬取图片并保存
'''
pagelist1 = ["http://blog.sina.com.cn/s/blog_c2b7980d010312d5.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312d4.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312cm.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312c0.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312bl.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312bj.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312av.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312an.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312a6.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010312a5.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103129w.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103129v.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103129m.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103129i.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103129h.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d01031277.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d01031274.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0102y888.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103124u.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103124t.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103124k.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311yo.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311ya.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311xp.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311wl.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311wm.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311wb.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311w7.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311w4.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311w3.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311vy.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311ve.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311uz.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311tu.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311tm.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311td.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311ru.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311rh.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311rg.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311qa.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311q8.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311no.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311nn.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311lv.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311lb.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311ky.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311kn.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311hg.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311gm.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311f3.html",
             ]
pagelist2 = ["http://blog.sina.com.cn/s/blog_c2b7980d010311ek.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311dv.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010311ds.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d01031189.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010310hn.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010310e4.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d010310e3.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103103g.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d0103101n.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d01030zts.html",
             "http://blog.sina.com.cn/s/blog_c2b7980d01030ztr.html",
             ]
headers = {
    'Connection': 'close',
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    'cache-control': "no-cache",
}
url = "http://blog.sina.com.cn/s/blog_c2b7980d01030ztr.html"


# 获取网址
def get_url(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


def get_title(url):
    try:
        html = get_url(url)
        soup = BeautifulSoup(html, "html.parser")
        # 通过分析网页内容，查找img的统一父类及属性
        title = soup.find('div', class_='articalTitle').find_all('h2')  # img为图片的标签
        return title[0].string
    except:
        print("获取标题失败")


def get_imglist(url):
    try:
        html = get_url(url)
        soup = BeautifulSoup(html, "html.parser")
        # 通过分析网页内容，查找img的统一父类及属性
        all_img = soup.find('div', class_='articalContent').find_all('img')  # img为图片的标签
        return all_img
    except:
        print("获取图片列表失败")



# 获取图片地址并保存下载
def get_pic(img,root, filename):
    # count = 0
    src = img['real_src']  # 获取img标签里的src内容
    img_url = src
    # img_origin = "http://s15.sinaimg.cn/orignal/"
    img_origin = "http://album.sina.com.cn/pic/"
    img_name = img_url.split('/')[-1]
    print("img_url:" + img_url)

    path = root + img_name  # 获取img的文件名
    print("path:" + path)
    print("img_origin+name:" + img_origin + img_name)
    try:
        if not os.path.exists(root):  # 判断是否存在文件并下载img
            os.mkdir(root)
        if not os.path.exists(path):
            read = requests.get(img_origin + img_name, headers=headers, allow_redirects=False)
            new_url = read.headers['Location'].replace(".cn", ".in")
            print("new_url", new_url)
            read = requests.get(new_url, headers=headers)
            with open(filename, "wb")as f:
                f.write(read.content)
                f.close()
                print("文件保存成功！")
        else:
            print("文件已存在！")
    except:
        print("文件爬取失败！")


executor = concurrent.futures.ThreadPoolExecutor(max_workers=None)
futures = []


def start_single_page(url):
    title = get_title(url)
    root = title + "/"
    imglist = get_imglist(url)
    count = 0
    for img in imglist:
        count += 1
        executor.submit(get_pic, img, root,root + str(count) + ".jpg")
        # f = executor.submit(get_pic, img, root,root + str(count))
        # futures.append(f)
    # results = [f.result() for f in futures]


# 主函数
if __name__ == '__main__':
    for s in pagelist2:
        print(s)
        start_single_page(s)
    for s in pagelist1:
	    print(s)
	    start_single_page(s)
