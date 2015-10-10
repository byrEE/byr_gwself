#!/usr/bin/env python3
# coding=utf-8

__author__='byrEE'

from urllib import request,parse 
from bs4 import BeautifulSoup
import getpass
import sys
def login():
    DDDDD=input('学号：')
    upass=getpass.getpass('密码：')
    login_data=parse.urlencode([('DDDDD',DDDDD),('upass',upass),('0MKKey','')])
    req=request.Request('http://10.3.8.211/')
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0')
    with request.urlopen(req,login_data.encode('utf-8')) as f:
        data=f.read().decode('gbk')
        soup=BeautifulSoup(data,'lxml')
        info=str(soup.title.string)
        test_str='登录成功窗'
        if info==test_str:
            print('login successful')
        else:
            print('学号或密码不对，请重新输入： ')
            login()

def logout():
    req=request.urlopen('http://10.3.8.211/F.htm')
    print('logout successfully')

def parse_id():
    id=input('''请选择登陆还是注销：
        1 ——> 登陆
        2 ——> 注销
        3 ——> 退出\n ''')
    if id==str(1):
        login()
    elif id==str(2):
        logout()
    elif id==str(3):
        sys.exit()
    else:
        print('非法id')

if __name__=='__main__':
    parse_id()
