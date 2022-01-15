from scrapy.http import TextResponse
import requests
from pprint import pprint

url = requests.get("https://ultra.ge/%E1%83%9C%E1%83%9D%E1%83%A3%E1%83%97%E1%83%91%E1%83%A3%E1%83%A5%E1%83%94%E1%83%91%E1%83%98")

response = TextResponse(url.url, body=url.text, encoding='utf-8')
items = response.css("div.caption a::attr(href)").getall()

ram = []
for i in items[:1]:
    url = requests.get(i)
    response = TextResponse(url.url, body=url.text, encoding='utf-8')
    item = response.css("td").getall()
for i in range(len(item)):
    if "ოპერატიული მეხსიერება" in item[i]:
        print(item[i + 1])