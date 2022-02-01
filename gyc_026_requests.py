"""
目标:Get请求方法演练
案例:http://www.baidu.com
请求:
1．请求方法:GET
响应:
2．响应对象.url # 获取请求url
3．响应对象.status_code # 获取响应状态码
4．响应对象.text # 以文本形式显示响应内容
"""

# Get请求

# 1、导包
import requests

# 2、调用get
url = 'http://www.baidu.com'
r = requests.get(url)

# 3、获取请求url
print('请求地址', r.url)

# 4、获取响应状态码
print('状态码', r.status_code)

# 5、获取响应信息 文本信息
print('文本响应信息', r.text)

print('-----------------------------------------------------------')

"""
目标:Get请求方法演练
案例:http://www.baidu.com?id=1001
案例:http://www.baidu.com?id=1001,1002
案例:http://www.baidu.com?id=1001,1002&kw=背景
请求:
1．请求方法:GET
参数:
1．params：字段或者字符串（推荐使用字典）
响应:
1．响应对象.url # 获取请求url
2．响应对象.status_code # 获取响应状态码
3．响应对象.text # 以文本形式显示响应内容
"""

# Get请求带参数的使用

# 1、导包
import requests

# 2、调用get
# params = {'id':1001} # 案例1
# params = {'id':'1001,1002'} # 案例2
params = {'id': '1001', 'kw': '背景'}  # 案例3
url = 'http://www.baidu.com'
r = requests.get(url, params=params)

# 3、获取请求url
print('请求地址', r.url)

# 4、获取响应状态码
print('状态码', r.status_code)

# 5、获取响应信息 文本信息
print('文本响应信息', r.text)  # 返回类型为字符串

print('-----------------------------------------------------------')
"""
目标:Post请求方法演练

请求:
1．请求方法:Post
参数:
1．json:传入json字符串
2．headers:传入请求信息头内容
响应:
1．响应对象.json()

"""
"""
此接口来自果创云
账号：no115gyc
密码：qwer1234
http://api.yesapi.cn/docs-api-App.User.Register.html
"""
# Post请求

# 1、导包
import requests
import json

# 2、调用Post
url = 'http://hn216.api.yesapi.cn/?s=App.User.Register'  # 请求地址
# headers ={""} # 请求头 此接口没有的请求头，故不传
data = {
    "app_key": "53EF1F4EB9E787644CD99D605AA9DBFC",  # key 在果创云中获取
    "username": "no4115gyc3",
    "password": "5d93ceb70e2bf5daa84ec3d0cd2c731a"
}  # 请求json

# r = requests.post(url,headers=headers,json=data) # 请求头 此接口没有的请求头，故不传，请求头为字典数据格式
r = requests.post(url, json=data)  # 使用json新增用户

# data和json的区别
# data是字典对象
# json是json对象
# 后台格式是有区别的
# 如果要将字段转为json字符串，使用json.dumps(字段对象)
# r = requests.post(url,data=json.dumps(data)) # 使用data新增用户

# 3、获取请求url
print('请求地址', r.url)

# 4、获取响应状态码
print('状态码', r.status_code)

# 5、响应对象
print('响应对象json', r.json())
print('响应对象json，返回为字典：', r.json()['data']['err_msg'])
print('响应对象text', r.text)
print('响应对象headers', r.headers)
# print('响应对象text，返回为字典：',r.text['data']['err_msg'])

# 响应数据text和json()的区别   # text没有小括号
# json():返回类型字典，可以通过键名来获取响应的值
# text:返回的类型为字符串,无法通过键名来获取响应的值
# 提示:共同点长得都像字典

print('-----------------------------------------------------------')

# Put请求 & Delete请求

# 参考Post

# Put请求 & Delete请求，因为有安全问题，现在没有get和post常用

print('-----------------------------------------------------------')

# 响应对象方法（encoding 和 headers）
# 响应对象方法 cookies


# 1、导包
import requests

# 2、调用get
url = 'http://www.baidu.com'
r = requests.get(url)

# 3、获取响应编码
print('响应对象encoding', r.encoding)

# 4、获取响应头
print('响应对象headers', r.headers)

# 5、获取cookies
print('响应对象cookies', r.cookies)
print('响应对象cookies', r.cookies['BDORZ'])

# 5、获取content
print('响应对象content', r.content)

print('-----------------------------------------------------------')

# 响应对象方法 content (图片)

# 1、导包
import requests

# 2、调用get
url_img = 'http://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png'
r = requests.get(url_img)

# 3、获取text
print('响应对象text', r.text)  # 乱码

# 4、获取content
print('响应对象content', r.content)  # 返回图片字节码

# 5、将图片写入当前目录
with open("baidu.png", "wb") as f:
    f.write(r.content)

print('-----------------------------------------------------------')

# Session对象

# 为什么使用session对象
# 说明: session可以自动保存服务器产生的cookies信息，并且自动在下一条请求是附加

# 什么是session
# 说明:一次会话(从客户端和服务器创建请求连接开始，客户端和服务器断开连接结束)

# session获取及应用
# 获取:
# 导包 import requests
# 获取 session 对象 session = requests.session()
# 应用:
#     通过session对象.方法
#     示例:
#         session.get()
#         session.post()
#         session.delete()
#         session.put()

# 1、导包
import requests

# 2、调用session # 使用session方法可以自动保存使用cookies
session = requests.session()

# 3、调用session方法发送请求
requests.session().post('http://www.baidu.com')

print('-----------------------------------------------------------')

"""
requests结合Unittest
https://www.bilibili.com/video/BV1uz411q7Pg?p=19
"""
