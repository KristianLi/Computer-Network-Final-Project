import json
import datetime

# 获取今天的日期并格式化为 'YYYY-MM-DD' 格式
today_date = datetime.datetime.now().strftime("%Y-%m-%d")

# 构建原始文件的路径和名称
input_filename = f"../Data/{today_date}/radiation_data2.json"

def format_area_name(area):
    """根据不同类型的地区名添加相应的后缀。"""
    if area in ["北京", "天津", "上海", "重庆"]:
        return area + "市"
    elif area in ["内蒙"]:
        return area + "古自治区"
    elif area in ["西藏"]:
        return area + "自治区"
    elif area in ["广西"]:
        return area+ "壮族自治区"
    elif area in ["宁夏"]:
        return area + "回族自治区"
    elif area in ["新疆"]:
        return area + "维吾尔自治区"
    elif area in ["香港", "澳门"]:
        return area + "特别行政区"
    else:
        return area + "省"

def process_area(data):
    """处理 'Area' 字段，完整地表示地区名，并移除 'Time' 字段。"""
    processed = []
    for entry in data:
        # 移除括号及其内部的内容
        raw_area = entry['Area'].split(" (")[0]
        # 格式化地区名称
        formatted_area = format_area_name(raw_area)

        # 创建新的条目，不包括 'Time' 字段
        new_entry = {
            'name': formatted_area,
            'value': entry['Radiation_Data']
        }
        processed.append(new_entry)
    return processed

def read_json(filename):
    """从文件中读取JSON数据。"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_file(data, filename):
    """将处理后的数据保存到一个新的JSON文件。"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 读取原始数据
try:
    radiation_data = read_json(input_filename)

    # 对数据进行处理
    processed_data = process_area(radiation_data)

    # 定义新文件的名称
    output_filename = f"../Data/{today_date}/re_data.json"

    # 保存处理后的数据到文件
    save_to_file(processed_data, output_filename)

    print(f"Processed data has been saved to {output_filename}")
except FileNotFoundError:
    print(f"The file {input_filename} was not found.")
