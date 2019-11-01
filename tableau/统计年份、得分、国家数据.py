# 统计年份、得分、国家数据
import json
import re
score = {}
year = {}
country = {}
count = 0
with open('maoyan.txt', 'r', encoding='utf-8') as f:
    while f:
        temp = f.readline()
        data = json.loads(temp)
        temp_year = data['time'][:4]
        temp_score = data['score']
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        temp_re = re.findall(pattern, data['time'])
        temp_country = ''
        if temp_re:
            temp_country = ''.join(temp_re)
        if year.get(temp_year):
            year[temp_year] += 1
        else:
            year[temp_year] = 1
        if score.get(temp_score):
            score[temp_score] += 1
        else:
            score[temp_score] = 1
        if country.get(temp_country):
            country[temp_country] += 1
        else:
            country[temp_country] = 1
        count += 1
        if count == 100:
            break
with open('maoyan.json', 'a', encoding="utf-8") as f:
    res = {}
    res['score'] = score
    res['year'] = year
    res['country'] = country
    f.write(json.dumps(res))
print('-' * 50)
