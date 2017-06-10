import requests
import pymysql
from bs4 import BeautifulSoup


for k in range(11):	
	url = 'https://movie.douban.com/top250?start='+str(25*k)+'&filter='
	html = requests.get(url)
	soup = BeautifulSoup(html.content,"html.parser")
	# html = requests.get('https://movie.douban.com/top250',timeout = 30)
	# soup = BeautifulSoup(html.content,"html.parser")
	items = soup.find("ol","grid_view").find_all("li")
	lists = []
	for i in items:
		movie = {}
		movie["rank"]= i.find("em").text
		movie["link"]= i.find("div","pic").find("a").text
		movie["poster"]= i.find("div","pic").find("a").find('img').get("src")
		movie["name"] = i.find("span","title").text
		movie["score"]= i.find("span","rating_num").text
		movie["quote"]= i.find("span","inq").text if(i.find("span", "inq")) else ""
		lists.append(movie)
		
	for j in range(len(lists)):
		tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
		print(tplt.format(lists[j]['rank'],lists[j]['name'],lists[j]['score'],lists[j]['quote'],chr(12288)))
