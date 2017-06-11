# crawlDouBanMoviesTOP250
运行环境
```
Python 3.x
```
运行方法
```
python 爬取豆瓣电影TOP250.py
```
需要的库
```
import requests
from bs4 import BeautifulSoup
```
对于爬取豆瓣电影TOP250存储到MySQL.py的说明
第28行更改为你自己的数据库即可,不用手动创建表,但是要手动创建Movies这个数据库
```
db = pymysql.connect(host = "IP",user = "root",password = "password",db = "Moives",charset = "utf8mb4")
```
