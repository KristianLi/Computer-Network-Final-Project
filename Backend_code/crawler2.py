import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

url = 'https://data.rmtc.org.cn/gis/listtype0M.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    data_list = []
    locations = soup.find_all('li', class_='datali')

    current_date = datetime.now().strftime("%Y-%m-%d")  # 获取当前日期

    for location in locations:
        place = location.find('div', class_='divname').text.strip()
        radiation_value = location.find('span', class_='label').text.strip()

        data = {
            'Area': place,
            'Radiation_Data': radiation_value,
            'Time': current_date  # 将当前日期添加到数据中
        }
        data_list.append(data)

    folder_path = f'../Data/{current_date}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # 如果文件夹不存在，则创建文件夹

    file_path = f'{folder_path}/radiation_data2.json'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            existing_data.extend(data_list)

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            print(f"数据已追加到 {file_path} 文件")
    else:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)
            print(f"数据已保存到 {file_path} 文件")
else:
    print(f"无法访问该网站。状态码: {response.status_code}")
