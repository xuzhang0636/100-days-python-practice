"""
用户身份验证

Version: 0.1
Author: Robert Xu
"""

username = input('请输入用户名：')
password = input('请输入口令：')

if username == 'admin' and password == '123456':
    print('success')
else:
    print('failed')
