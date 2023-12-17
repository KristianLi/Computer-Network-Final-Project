import openai
import os
import json
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")  # 获取当前日期
def read_json_files(folder_path):
    """
    读取指定文件夹中的所有 JSON 文件。

    :param folder_path: 包含 JSON 文件的文件夹路径。
    :return: 一个字典，键是文件名，值是 JSON 文件的内容。
    """
    json_data = {}

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # 读取 JSON 文件
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    json_data[filename] = json.load(file)
                except json.JSONDecodeError:
                    print(f"错误：文件 '{filename}' 不是有效的 JSON。")

    return json_data

# 示例：读取 'my_folder' 中的 JSON 文件
folder_path = f'../Data/{current_date}/'  # 替换为你的文件夹路径
json_files = read_json_files(folder_path)

# 打印结果
# for file_name, content in json_files.items():
#     print(f"文件：{file_name}\n内容：{content}\n")

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    """
    使用 OpenAI ChatGPT 模型进行对话。

    :param prompt: 发送给模型的提示。
    :param model: 使用的 ChatGPT 模型版本。
    :return: 模型的响应或错误信息。
    """
    # 在这里设置你的 API 密钥
    openai.api_key = "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"

    try:
        # 使用 OpenAI ChatGPT API 发送提示
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt+str(json_files)}]
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        return f"OpenAI 错误: {e}"
    except Exception as e:
        return f"其他错误: {e}"

def save_response_to_json(response, file_name=f"../Data/{current_date}/analysis.json"):
    """
    将给定的响应字符串保存到一个 JSON 文件中。

    :param response: 要保存的响应字符串。
    :param file_name: 要创建的 JSON 文件的名称。
    """
    # 创建要保存的数据结构
    data = {"response": response}

    # 将数据写入 JSON 文件
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

prompt = "以下是爬取到到某些地区到辐射值，请分析一下数据,研究不同地区的辐射情况，分析地理分布上的差异，评估环境和健康风险等问题，我要结论"
response = chat_with_gpt(prompt)
print(response)
save_response_to_json(response)
