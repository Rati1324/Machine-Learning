from scrapy.http import TextResponse
import requests
import pandas as pd
from pprint import pprint

url = requests.get("https://ultra.ge/%E1%83%9C%E1%83%9D%E1%83%A3%E1%83%97%E1%83%91%E1%83%A3%E1%83%A5%E1%83%94%E1%83%91%E1%83%98?page=1&bfilter=")
response = TextResponse(url.url, body=url.text, encoding='utf-8')
items = response.css("div.caption a::attr(href)").getall()

ram = []
storage = []
price = []
for i in items[:9]:
    url = requests.get(i)
    response = TextResponse(url.url, body=url.text, encoding='utf-8')
    item = response.css("td").getall()

    if item[0] == "ტიპი":
        for i in range(len(item)):
            if "ოპერატიული მეხსიერება" in item[i]:
                size = int(item[i + 1][4:-7])
                ram.append(size)
            elif "მყარი დისკის ტიპი" in item[i]:
                size = item[i - 1][4:-5]
                if "TB" in size:
                    size = int(size[:-2]) * 1000
                else:
                    size = int(size[:-3])
                storage.append(size)
                break

    item = response.css("h2").get()
    index_close = [i for i in range(len(item)) if item.startswith('>', i)][1]
    index_open = [i for i in range(len(item)) if item.startswith('</', i)][0]
    amount = float(item[index_close + 1:index_open - 1].replace(',', ''))
    price.append(amount)

print(ram, len(ram))
print(storage, len(storage))
print(price, len(price))
# data = {"ram": ram, "storage": storage, "price": price}
# df = pd.DataFrame(data)
# df.to_excel("data.xls", index=False)
