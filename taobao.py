import requests
import json

url = "https://cart.taobao.com/cart.htm"

param = {
    "spm" : "a21bo.jianhua.1997525049.1.5af92a89kXXxbh",
    "from" : "mini",
    "ad_id" : "",
    "am_id" : "",
    "cm_id" : "",
    "pm_id" : "1501036000a02c5c3739"
}

requirment = requests.get(url, params=param)

print(requirment.text)
