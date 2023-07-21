from bs4 import BeautifulSoup
import urllib.request, urllib.error


# URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向服务器发送消息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def get_data(team_code):
    base_url = "https://nba.hupu.com/players/"
    teams_list = ['grizzlies', 'mavericks', 'spurs', 'rockets', 'pelicans', 'warriors', 'suns', 'clippers', 'lakers',
                 'jazz', 'nuggets', 'timberwolves', 'blazers', 'thunder', 'nets', '76ers', 'celtics', 'raptors',
                 'knicks',
                 'heat', 'wizards', 'hornets', 'hawks', 'magic', 'bulls', 'bucks', 'cavaliers', 'pacers', 'pistons']
    url = base_url + teams_list[team_code]
    return askURL(url)


if __name__ == "__main__":
    html = get_data(5)
    soup = BeautifulSoup(html, "html.parser")
    with open("hupu.txt", "a") as f:
        for item in soup.find_all("table", class_="players_table"):
            for tr in item.find_all("tr"):
                tds = tr.find_all("td")
                if not tds:
                    # Skip header row
                    continue
                names_a , name = [] , []
                names_a = tds[1].find("a")
                print(names_a)
                
                # try:
                #     # name = tds[0].find("a").text.strip()
                #     detail_url = tds[0].find("a")["href"]
                #     img_src = tds[1].find("img")["src"]
                #     num = tds[2].text.strip()
                #     position = tds[3].text.strip()
                #     height, weight = [s.strip() for s in tds[4].text.split("/") if s.strip()]
                #     birth = tds[5].text.strip()
                #     salary = tds[6].find("b").text.strip()
                # except:
                #     print("出错")
                # f.write(f"{detail_url}\n{img_src}\n{num}\n{position}\n{height}\n{weight}\n{birth}\n{salary}\n")
                # print(f"{detail_url}\n{img_src}\n{num}\n{position}\n{height}\n{weight}\n{birth}\n{salary}\n")
