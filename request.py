import requests

url = "https://fanyi.baidu.com/sug"

s = input("what do you want to seach?\n")

dat = {
    "kw": s
}

res = requests.post(url,data=dat)
ans = res.json()
list = ans["data"]
num = 1
for item in list:
    print(f"No.{num} WORDS\t")
    print(item["k"] +"---->"+ item["v"]+'\t')
    num+=1
