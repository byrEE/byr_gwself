#!/usr/bin/env python3
# coding=utf-8

__author__='byrEE'

from urllib import request,parse 
from bs4 import BeautifulSoup
import getpass
import sys
import re

def flow_cal(flow):
    flow0=flow%1024
    flow1=flow-flow0
    flow0*=1000
    flow0=flow0-flow0%1024
    return flow1/1024+flow0/1024000

def fee_cal(fee):
    fee1=fee-fee%100
    return fee1/10000

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
            print('*********************')
            print('your info is:')
            query_info()
            print('*********************')

        else:
            print('学号或密码不对，请重新输入： ')
            login()

def query_info():
    pat_js=re.compile(r".*time='(\d+)\s+';flow='(\d+)\s+'.*fee='(\d+)\s+'.*")
    req=request.Request('http://10.3.8.211')
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0')
    with request.urlopen(req) as gw:
        data_gw=gw.read().decode('gb2312')
        sp=BeautifulSoup(data_gw,'lxml')
        tmp=sp.script.string
        #print(tmp)
        tff=re.findall(pat_js,tmp)
        #print(tff)
        print('****************')
        print('Used Time: %s  Min'%tff[0][0])
        print('Used Traffic: %s Mbyte'%flow_cal(int(tff[0][1])))
        print('Balance: %s'%fee_cal(int(tff[0][2])))
        print('****************')

def logout():
    req_q=request.urlopen('http://10.3.8.211/F.htm')
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
