import requests as rp
from bs4 import BeautifulSoup as soup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
q="face".replace(" ","+")
url="https://www.google.com/search?q="+q+"&rlz=1C1CHBF_enUS880US880&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiuqfy-08foAhXbgnIEHXZzAdcQ_AUoAXoECBgQAw&biw=1280&bih=832&safe=active&ssui=on"
page=rp.get(url,headers=headers)
s = soup(page.content,"html.parser")
imgs=s.find_all("img")
