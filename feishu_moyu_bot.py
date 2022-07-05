#    ____       _                      __    __       
#   /___ \_   _(_)_ __   ___ ___ _   _/ / /\ \ \_   _ 
#  //  / / | | | | '_ \ / __/ _ \ | | \ \/  \/ / | | |
# / \_/ /| |_| | | | | | (_|  __/ |_| |\  /\  /| |_| |
# \___,_\ \__,_|_|_| |_|\___\___|\__, | \/  \/  \__,_|
#                                |___/                
# !/use/bin/env/python
# encoding:utf-8
# author: QuinceyWu
import requests
import json


def get_data():
    data = {
        "msg_type": "text",
        "content": {
            "text": "{get_moyu_text}"
        }
    }
    return json.dumps(data, ensure_ascii=True).encode("utf-8")


def req(data):
    # webhook
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/{webhook_key}"
    header = {
        "Content-type": "application/json",
        "charset": "utf-8"
    }
    requests.post(url, data=data, headers=header)


if __name__ == '__main__':
    req(get_data())