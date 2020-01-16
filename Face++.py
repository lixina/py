import time
import urllib.request
import urllib.error
http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = ''
secret = ''
filepath = r'' #本地图片路径 \

boundary = '--------------%s' % hex(int(time.time() * 1000)) #格式化输出当前毫秒数
data = [] #列表类型
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr = open(filepath, 'rb') #读取filepath下的二进制文件
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append(
    "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
data.append('--%s--\r\n' % boundary)

for i, d in enumerate(data): #循环得到list的元素编号及元素
    if isinstance(d, str): #判断元素是否是str类型
        data[i] = d.encode('utf-8')

http_body = b''.join(data) # b''空字符串
req = urllib.request.Request(url=http_url, data=http_body) # build http request
req.add_header('Content-Type','multypart/form-data; boundary=%s' % boundary) #header

try:
    resp = urllib.request.urlopen(req,timeout=5) #post data to server
    qrcont = resp.read() #get response
    print(qrcont.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.read().decode('utf-8'))




