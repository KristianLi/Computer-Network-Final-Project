import os
import json
from datetime import datetime, timedelta

def get_date_range(start_date, end_date):
    """
    生成从 start_date 到 end_date 的日期列表。
    """
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def read_radiation_data(start_date, end_date, base_folder_path):
    """
    读取并整合指定日期范围内的辐射数据，按地区组织信息。
    """
    all_data = {}
    for single_date in get_date_range(start_date, end_date):
        folder = single_date.strftime("%Y-%m-%d")
        file_path = os.path.join(base_folder_path, folder, 'radiation_data2.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    # 加载当天的数据
                    daily_data = json.load(file)
                    for entry in daily_data:
                        area = entry["Area"]
                        # 如果地区不在字典中，则添加它
                        if area not in all_data:
                            all_data[area] = []
                        # 添加辐射数据和时间
                        all_data[area].append({
                            "Radiation_Data": entry["Radiation_Data"],
                            "Time": entry["Time"]
                        })
                except json.JSONDecodeError:
                    print(f"错误：文件 '{file_path}' 不是有效的 JSON。")
        else:
            print(f"文件未找到: {file_path}")

    return all_data

def save_combined_data(data, output_file):
    """
    将整合后的数据保存到一个 JSON 文件中。
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # 确保输出目录存在
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 设置日期范围和文件夹路径
current_date = datetime.now()
half_month_ago = current_date - timedelta(days=3)
base_folder_path = '../Data'  # 根据实际情况调整路径

# 读取并整合数据
combined_data = read_radiation_data(half_month_ago, current_date, base_folder_path)

# 设置输出文件路径并保存整合数据
output_folder = os.path.join('../Data', current_date.strftime('%Y-%m-%d'))
output_file = os.path.join(output_folder, 'whole.json')  # 保存结果的文件名
save_combined_data(combined_data, output_file)
print(f"整合后的数据已保存到 {output_file}")
