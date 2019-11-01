import requests
import time
from faker import Faker


f = Faker(locale='zh_CN')
base_url = 'https://piaofang.maoyan.com/second-box?beginDate=20191031'
# base_url = 'https://piaofang.maoyan.com/second-box?beginDate=201910'
headers = {
    'User-Agent': f.chrome()
}
# for i in range(1, 30):
#     url = base_url + str(i)
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         filename = str(i) + '.json'
#         with open(filename, 'w', encoding='utf-8') as f:
#             f.write(response.text)
#             print('成功写入第' + str(i) + '条')
#             time.sleep(2)
response = requests.get(base_url, headers=headers)
with open('31.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
