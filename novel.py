import requests
from bs4 import BeautifulSoup

base = "http://book.doupoxs.com/doupocangqiong/"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}

for chapter in range (1,6):
    with open(f"./Novel/chapter{chapter}.md","w") as F:
        url = base + str(chapter) +".html"
        novel = requests.get(url,headers=header)
        trans_text = novel.text.encode("ISO-8859-1").decode("utf-8")
        bs = BeautifulSoup(trans_text,"html.parser")
        title = bs.find_all('div',{'class':"entry-tit"})
        context = bs.findAll('div',{'class':"m-post"})
        for tit in title:
            F.write("# "+ tit.get_text())
            print(tit.get_text())
        for tex in context:
            F.write("- " + tex.get_text())
    F.close()
       
        
        
            
    
    