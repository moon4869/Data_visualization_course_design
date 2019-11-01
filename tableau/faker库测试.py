from faker import Faker
import requests


f = Faker(locale='zh_CN')
url = 'https://piaofang.maoyan.com/second-box?beginDate=20190930'
headers = {
    'User-Agent': f.user_agent()
}
response = requests.get(url, headers=headers)
print(response.status_code)
