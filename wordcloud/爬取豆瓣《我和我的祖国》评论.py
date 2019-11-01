import requests
from faker import Faker
import re
import time
import json


# res = []
comment = []
f = Faker(locale='zh_CN')
base_url = 'https://movie.douban.com/subject/32659890/comments?start={}&limit=20&sort=new_score&status=P&comments_only=1'
for i in range(11):
    offset = i * 20
    url = base_url.format(offset)
    headers = {
        'User-Agent': f.chrome()
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        temp_str = response.json()
        data = temp_str['html']
    pattern = re.compile(
        r'<div class="comment-item".*?class="votes">(.*?)</span>.*?class="allstar(.*?) rating".*?class="comment-time " title="(.*?)".*?class="short">(.*?)</span>.*?</div>', re.S)
    temp_re = re.findall(pattern, data)
    for j in temp_re:
        comment.append(j[3].replace('\n', ''))
    print('已获取{}条评论'.format(len(comment)))
    # res += temp_re
    time.sleep(10)
with open('comment.json', 'a', encoding='utf-8') as fp:
    fp.write(json.dumps(comment, ensure_ascii=False))
