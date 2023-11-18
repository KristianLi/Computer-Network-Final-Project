import requests
from bs4 import BeautifulSoup
url1 = "https://www.hko.gov.hk/sc/radiation/monitoring/index.html"
url2 = "https://data.rmtc.org.cn/gis/listtype0M.html"
url3 = "https://maris.iaea.org/explore/type/1"
url4 = "https://mds.nmdis.org.cn/pages/dataView.html?type=2&id=a5da2a0528904471b3"
output_file = '../target_html/test2.html'

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the URL: {url}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching the URL: {url}. Exception: {e}")
        return None

def save_to_file(html_content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content saved to {filename} successfully!")
    except IOError as e:
        print(f"Error saving HTML content to {filename}. Exception: {e}")

if __name__ == "__main__":
    # 替换成你想要爬取的网站URL

    # 获取网站的HTML内容
    html_content = get_html(url2)

    if html_content:
        # 解析HTML内容（可选）
        soup = BeautifulSoup(html_content, 'html.parser')
        # 将HTML内容写入本地文件
        save_to_file(html_content, output_file)
