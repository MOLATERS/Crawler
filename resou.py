import requests

url ="https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&show_cache_when_error=1&extparam=seat%3D1%26dgr%3D0%26c_type%3D30%26lcate%3D1001%26region_relas_conf%3D0%26cate%3D10103%26filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26display_time%3D1688884630%26pre_seqid%3D2052206706&luicode=10000011&lfid=231583"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}

res = requests.get(url,headers=headers)
dict = res.json()

cards = dict.get("data").get("cards")
index = 1
dict = {"0":"Ḧöẗ Ẅöṛḋṡ","1":"文娱","2":"要闻","4":"更多"}
for j in range (0,1):
    print(f"⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚{dict[str(0)]}⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚")
    for i in range (0,10):
        print(f"No.{i+1}  "+cards[j].get("card_group")[i].get("desc"))
    print(f"⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚{dict[str(0)]}⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚⸚")
    for i in range (0,10):
        print(f"No.{i+1}  相关链接："+cards[j].get("card_group")[i].get("scheme"))

