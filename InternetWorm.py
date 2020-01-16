import urllib.request
import re

def getcontent(url,page):
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    # 构建段子内容提取的正则表达式
    contentpat = '<div class="content">(.*?)</div>' # .不进行多行匹配
    # 寻找出所有内容
    contentlist = re.compile(contentpat,re.S).findall(data) # re.S忽略多行的影响 进行多行匹配
    # 通过for循环遍历段子内容并将内容分贝赋给对应的变量
    for content in contentlist:
        content = content.replace("\n", "")
        print(content)
        print("-----------------------")
        # open("", content)
# 分别获取各页面的段子
for i in range(1, 30):
    url = "http://qiushibaike.com/8hr/page/"+str(i)
    getcontent(url, i)

