import requests
from lxml import etree
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
res = requests.get("http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001",headers=headers)
content = res.content.decode()

html = etree.HTML(content)
title = html.xpath('//body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li/div[2]/h4/a/text()')
price = html.xpath('//body/div[4]/div/div[2]/div[1]/div/div[1]/ul/li/div[2]/ul/li/strong[last()]/b/text()')

print ("博客來網路書店排名書籍推薦:")
for i,j in zip(title,price):
  print(i,j)
