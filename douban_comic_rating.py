import requests

url = "https://movie.douban.com/j/chart/top_list"

data  = {
    "type": 24,
    "interval_id": "100:90",
    "start": 0,
    "limit": 20
}

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=header,params=data)
content = response.json()
print(content)

# for movie in content:
    # print(movie["rating"][0],movie["cover_url"])    

with open("douban_comic_rating.json","w",encoding="utf-8") as f:
    f.write(str(response.text))
    f.close()
    
with open("douban_comic_rating.md","w",encoding="utf-8") as f:
    for movie in content:
        f.write(f"{movie['rating'][0]}\n {movie['cover_url']}\n")
    f.close()