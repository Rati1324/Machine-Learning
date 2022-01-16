from scrapy.http import TextResponse
import requests
import pandas as pd
from pprint import pprint

ram = []
storage = []
price = []
brand = []

url = requests.get("https://alta.ge/computers-and-office/pcs-notebooks-and-accessories/notebooks.html")
response = TextResponse(url.url, body=url.text, encoding='utf-8')
items = response.css("a.product-title::attr(href)").getall()

index = 1
for i in items:
    url = requests.get(i)
    response = TextResponse(url.url, body=url.text, encoding='utf-8')
    item = response.css("div.ty-product-feature").getall()
    for j in item:
        if "RAM:" in j:
            substr = j[j.find('lue">') + 5:]
            print(substr)
            print("-----")
            ram_amount = int(substr[:substr.find("<")]) / 1024
            ram.append(ram_amount)
        elif "HDD" in j:
            substr = j[j.find('lue">') + 5:]
            if "TB" in substr:
                hdd = int(substr[:substr.find("<") - 2])
                hdd /= 1000
            storage.append(hdd)
            break
        elif "SSD:" in j:
            substr = j[j.find('lue">') + 5:]
            ssd = int(substr[:substr.find("<")])
            if "TB" in substr:
                ssd /= 1000
            # print(ssd)
            storage.append(ssd)
            break
        elif "Brand" in j:
            substr = j[j.find('lue">') + 5:]
            brand_name = str(substr[:substr.find("<")])
            brand.append(brand_name)
    item = response.css("span.ty-price-num").get()
    substr = item[item.find('">') + 2:]
    price_amount = int(substr[:substr.find("<")])
    price.append(price_amount)
    index += 1
print(ram)
print(storage)
print(brand)
print(price)

# for page in range(1, 4):
#     url = requests.get(f"https://ultra.ge/%E1%83%9C%E1%83%9D%E1%83%A3%E1%83%97%E1%83%91%E1%83%A3%E1%83%A5%E1%83%94%E1%83%91%E1%83%98?page={page}&bfilter=")
#     response = TextResponse(url.url, body=url.text, encoding='utf-8')
#     items = response.css("div.caption a::attr(href)").getall()
#     for j in items:
#         url = requests.get(j)
#         response = TextResponse(url.url, body=url.text, encoding='utf-8')
#         item = response.css("td").getall()
#         if any(["ოპერატიული მეხსიერება" in i for i in item]):
#             for i in range(len(item)):
#                 if "ოპერატიული მეხსიერება" in item[i]:
#                     size = int(item[i + 1][4:-7])
#                     ram.append(size)
#                 elif "მყარი დისკის ტიპი" in item[i]:
#                     size = item[i - 1][4:-5]
#                     if "TB" in size:
#                         size = int(size[:-2]) * 1000
#                     else:
#                         size = int(size[:-3])
#                     storage.append(size)
#                     break
#             item = response.css("h2").get()
#             index_close = [i for i in range(len(item)) if item.startswith('>', i)][1]
#             index_open = [i for i in range(len(item)) if item.startswith('</', i)][0]
#             amount = float(item[index_close + 1:index_open - 1].replace(',', ''))
#             price.append(amount)


# print(ram, len(ram))
# print(storage, len(storage))
# print(price, len(price))
# data = {"ram": ram, "storage": storage, "price": price}
# df = pd.DataFrame(data)
# df.to_excel("data.xls", index=False)
