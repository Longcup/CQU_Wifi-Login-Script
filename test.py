import logging
import requests
import base64
import re
import sys
import time
import socket
import json

data_s = {
    "c": "Portal",
    "a": "login",
    "callback": "dr1004",
    "login_method": "1",
    "user_account": "",
    "user_password": "",
    "wlan_user_ip": "",
    "wlan_user_ipv6": "",
    "wlan_user_mac": "",
    "wlan_ac_ip": "",
    "wlan_ac_name": "",
    "jsVersion": "4.2.2",
    "terminal_type": "1",
    "lang": "zh_cn",
    "v": "4167"
    # "lang": "zh"
}
data_r = {}


def get_inf() :
    # 连上校园网后运行
    response = requests.get(
        'http://login.cqu.edu.cn:801/eportal/portal/online_list')
    print(json.loads(response.text[12:-2]))
    with open('request_info.txt', 'w') as f:
        f.write(response.text[12:-2])



def login():
    with open("request_info.txt", "r") as f:
        data_r = json.loads(f.read())
    print(data_r)

    data_s["wlan_user_ip"] = data_r["list"][0]["online_ip"]
    data_s["wlan_user_mac"] = data_r["list"][0]["online_mac"]

    data_s["user_account"] = input("输入账号:")
    data_s["user_password"] = input("输入密码:")
    response = requests.get("http://login.cqu.edu.cn:801/eportal/portal/", params=data_s)
    print(response.text)


def is_net_ok() -> bool:
    try:
        status = requests.get("https://www.baidu.com").status_code
        if status == 200:
            print("对对对")
            return True
        else:
            return False
    except Exception:
        return False


if __name__ == "__main__":
    if is_net_ok():# 有网 获取ip和macid
        data_r = get_inf()
    else:# 没网 执行登录请求
        login()

    # session = requests.Session()
    # response = requests.get("http://login.cqu.edu.cn:801/eportal/portal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=%2C0%2C20212801&user_password=021208&wlan_user_ip=172.24.10.8&wlan_user_ipv6=&wlan_user_mac=38f3ab903304&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2.2&terminal_type=1&lang=zh-cn&v=4643&lang=zh")

