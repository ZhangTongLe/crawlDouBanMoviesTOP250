import requests
import pymysql
from bs4 import BeautifulSoup

lists = []
for k in range(11):	
	url = 'https://movie.douban.com/top250?start='+str(25*k)+'&filter='
	html = requests.get(url)
	soup = BeautifulSoup(html.content,"html.parser")
	# html = requests.get('https://movie.douban.com/top250',timeout = 30)
	# soup = BeautifulSoup(html.content,"html.parser")
	items = soup.find("ol","grid_view").find_all("li")
	for i in items:
		movie = {}
		movie["rank"]= i.find("em").text
		movie["link"]= i.find("div","pic").find("a").text
		movie["poster"]= i.find("div","pic").find("a").find('img').get("src")
		movie["name"] = i.find("span","title").text
		movie["score"]= i.find("span","rating_num").text
		movie["quote"]= i.find("span","inq").text if(i.find("span", "inq")) else ""
		lists.append(movie)
		
	# for j in range(len(lists)):
	# 	tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
		# tplt = "{:2}\t{:4}\t{:6}\t{:8}"
		# print(tplt.format(lists[j]['rank'],lists[j]['name'],lists[j]['score'],lists[j]['quote'],chr(12288)))

db = pymysql.connect(host = "IP",user = "root",password = "password",db = "Moives",charset = "utf8mb4")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS movies")
createTab = """CREATE TABLE movies(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	rank VARCHAR(4) NOT NULL,
	score VARCHAR(4) NOT NULL,
	quote VARCHAR(50) 
)"""
cursor.execute(createTab)
for l in range(len(lists)):
	sql = "INSERT INTO `movies`(`name`,`rank`,`score`,`quote`) VALUES(%s,%s,%s,%s)" #注意这个是tab键上面的,不是单引号
	# sql = "INSERT INTO 'movies'('name','rank','score','quote') VALUES(%s,%s,%s,%s)"
	try:
		cursor.execute(sql,(lists[l]['name'],lists[l]['rank'],lists[l]['score'],lists[l]['quote']))
		# cursor.execute(sql,(lists[l]["name"], lists[l]["rank"], lists[l]["score"], lists[l]["quote"]))
		db.commit()
		print("Success")
		# print(i["name"]+" is success")
	except Exception as e:
		db.rollback()
		print(e)

db.close()
