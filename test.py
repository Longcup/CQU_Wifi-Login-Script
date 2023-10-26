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
        "user_account": "20212801",
        "user_password": "021208",
        "wlan_user_ip": "172.22.131.149",
        "wlan_user_ipv6": "",
        "wlan_user_mac":"c03c59454e4e",
        "wlan_ac_ip": "",
        "wlan_ac_name":"",
        "jsVersion": "4.2.2",
        "terminal_type": "1",
        "lang": "zh_cn",
        "v": "4167"
        #"lang": "zh"
}
if __name__ == "__main__":
    data_r = {}
    data_r = {'result': 1, 'msg': '获取用户在线信息成功！', 'list': [{'online_session': 43360, 'online_time': '2023-10-26 19:07:47', 'online_ip': '172.22.131.149', 'online_ipv6': '', 'online_mac': 'c03c59454e4e', 'time_long': '524', 'uplink_bytes': '0', 'downlink_bytes': '799', 'dhcp_host': '', 'device_alias': '', 'nas_ip': '67570186', 'user_account': '20212801', 'exit_id': '0', 'is_radius_auth': '0', 'is_perceive': '0', 'phone_flag': '0', 'is_bind_mac': '0', 'is_owner_ip': '1'}], 'total': 1}

    # session = requests.Session()
    # response = requests.get("http://login.cqu.edu.cn:801/eportal/portal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=%2C0%2C20212801&user_password=021208&wlan_user_ip=172.24.10.8&wlan_user_ipv6=&wlan_user_mac=38f3ab903304&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2.2&terminal_type=1&lang=zh-cn&v=4643&lang=zh")
    response = requests.get("http://login.cqu.edu.cn:801/eportal/portal/", params=data_s)
    print(response.text)

    response = requests.get(
        'http://login.cqu.edu.cn:801/eportal/portal/online_list')
    print(json.loads(response.text[12:-2]))

    # url = response.url
    #
    # with open('request_host_url.txt', 'w') as f:
    #     f.write(url)

