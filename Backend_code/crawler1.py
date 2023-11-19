import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hko.gov.hk/tc/radiation/monitoring/index.html"

# 发送HTTP请求并获取网页内容
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 找到辐射值和地名所在的标签
dose_values = soup.find_all("span", class_="c-station-dose-value")
station_names = soup.find_all("a", class_="c-station-dose-value l-color-safe")

# 创建空的字典来存储地名和辐射值
radiation_data = {}

# 遍历找到的标签，获取地名和对应的辐射值
for index, name in enumerate(station_names):
    station = name.text.strip()
    dose = dose_values[index].text.strip()
    radiation_data[station] = dose

# 将数据存入JSON文件
with open("radiation_data2.json", "w", encoding="utf-8") as file:
    json.dump(radiation_data, file, ensure_ascii=False, indent=4)

print("数据已成功存入 'radiation_data2.json' 文件中。")
