#coding=UTF-8

'''
***********
接口自动化框架设计
此模块放所有接口的入参信息
***********
'''


#1.接口的url地址
login_host ="http://192.168.1.32:8003"
login_url = "/login"
#接口的入参信息

#2.进入祈福页面接口
#接口的url地址
bless_host ="http://192.168.1.40:8002"
bless_url = "/api/temple/bless/index"


#3.添加恭请的佛像接口
addSelectBuddha_host = "http://192.168.1.40:8002"
addSelectBuddha_url = "/api/temple/bless/addSelectBuddha"

#4.以恭请的佛像列表-分页接口
hasSelectBuddhaListPage_host = "http://192.168.1.40:8002"
hasSelectBuddhaListPage_url = "/api/temple/bless/hasSelectBuddhaListPage"














