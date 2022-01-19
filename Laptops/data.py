from scrapy.http import TextResponse
import requests
import pandas as pd
from pprint import pprint

ram = []
storage = []
price = []
cores = []
thread = []
cpu_speed = []
max_cpu_speed = []

def scrap(string):
    substr = string[string.find('lue">') + 5:]
    if "TB" in substr:
        substr = int(substr[:substr.find("<") - 2]) * 1000
    elif "MHz" in substr:
        substr = int(substr[:substr.find("<") - 4])
    else:
        substr = int(substr[:substr.find("<")])
    return substr

for page in range(1, 7):
    url = requests.get(f"https://alta.ge/notebooks-page-{page}.html")
    response = TextResponse(url.url, body=url.text, encoding='utf-8')
    items = response.css("a.product-title::attr(href)").getall()

    for i in items:
        url = requests.get(i)
        response = TextResponse(url.url, body=url.text, encoding='utf-8')
        item = response.css("div.ty-product-feature").getall()
        
        if not len(response.css("span.ty-no-price").getall()) and all([ any(["Max Processor Speed:" in k for k in item]), any([">Processor Speed:" in k for k in item]) ]):
            for j in item:
                if "RAM:" in j:
                    ram_amount = scrap(j) / 1024
                    ram.append(ram_amount)
                elif "HDD:" in j or "SSD:" in j:
                    substr = scrap(j)
                    storage.append(substr)
                    break
                elif "Number Of Cores:" in j:
                    cores.append(scrap(j))
                elif "Processor Thread:" in j:
                    thread.append(scrap(j))
                elif "Max Processor Speed:" in j:
                    max_cpu_speed.append(scrap(j))
                elif "Processor Speed:" in j:
                    cpu_speed.append(scrap(j))
            item = response.css("span.ty-price-num").get()
            substr = item[item.find('">') + 2:]
            price_amount = int(substr[:substr.find("<")])
            price.append(price_amount)

print(len(ram))
print(len(storage))
print(len(price))
print(len(cores))
print(len(thread))
print(len(max_cpu_speed))
print(len(cpu_speed))

data = {"ram": ram, "storage": storage, "price": price, "cores": cores, "thread": thread, "max_cpu_speed": max_cpu_speed, "cpu_speed": cpu_speed}
df = pd.DataFrame(data)
df.to_excel("data.xls", index=False)