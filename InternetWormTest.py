import urllib.request as ur
import urllib.error as ue

file = ur.urlopen("http://www.baidu.com")
data = file.read()
print(len(data))
fh = open(r"F:\rl\python_worm\baidu.html", "wb")  # 打开本地文件
fh.write(data)  # 写入本地文件
fh.close()

ur.urlretrieve("http://news.sohu.com", r"F:\rl\python_worm\sohu.html")  # 一键爬取

# 异常处理机制
try:
    ur.urlopen("http://blog.csdn.net")
except ue.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "code"):
        print(e.reason)
    ur.urlopen("http://www.baidu.com")