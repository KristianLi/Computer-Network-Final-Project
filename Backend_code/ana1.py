import os
import numpy
from scipy.stats import pearsonr
import re, datetime
import json
#pip install scipy
#y为近几日的辐射值,返回明天的y以及r值和p值，r的绝对值大于0.5即可表明相关，p小于0.05即可表示有相关性
def predict():
    def least_squares_fit(y):
        x=list(range(len(y)))
        a, b = numpy.polyfit(x, y, 1)
        r, p = pearsonr(y,a + b * numpy.array(x))
        return a*len(y)+b,r,p

    data_path = '../Data'
    previous_data = {}

    for dir in os.listdir(data_path):
        file = os.path.join(data_path, dir, 'radiation_data2.json')
        with open(file, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                if previous_data.get(item['Area']) is None:
                    previous_data[item['Area']] = []
                else:
                    previous_data[item['Area']].append(int(item['Radiation_Data'].split(' ')[0]))

    saves = []
    for Area, Radiation_Datas in previous_data.items():
        m, r, p = least_squares_fit(Radiation_Datas)
        saves.append({
            'Area': Area,
            'Radiation_Data': '%d nGy/h' % int(m)
        })


    tomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    target_file = os.path.join(data_path, tomorrow_date, 'radiation_data2.json')
    folder_path = os.path.join(data_path, tomorrow_date)
    os.path.exists(folder_path) or os.mkdir(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # 如果文件夹不存在，则创建文件夹
    with open(target_file, 'w+', encoding='utf-8') as f:
        json.dump(saves, f,indent=4, ensure_ascii=False)
predict()