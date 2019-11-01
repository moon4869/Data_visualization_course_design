# 获取电影地址列表
# 获取电影类型、国家数据
import requests
import re
import json
from requests.exceptions import RequestException
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?<p.*?href="(.*?)".*?</dd>', re.S)
    items = re.findall(pattern, html)
    return items


def parse_page(html):
    pattern = re.compile(r'<li.*?"ellipsis">(.*?)</li>', re.S)
    items = re.findall(pattern, html)
    return items


def write_to_file(content):
    with open('maoyansrc.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(src_list, offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)
    src_list += items


if __name__ == "__main__":
    # src_list = []
    list1 = []
    list2 = []
    # for i in range(10):
    #     main(src_list, offset=i * 10)
    #     time.sleep(2)
    # with open('src_list.json', 'a', encoding="utf-8") as f:
    #     f.write(json.dumps(src_list))
    with open('src_list.json', 'r', encoding='utf-8') as f:
        temp = f.read()
        src_list = json.loads(temp)
    url = "https://maoyan.com"
    for i in src_list:
        html = get_one_page(url + str(i))
        items = parse_page(html)
        list1.append(items[0].strip())
        p = re.compile(r'(.*?)\n')
        list2.append(re.match(p, items[1].strip()).group(0)[:-1])
        time.sleep(2)
        print(items)
    with open('list1&2.json', 'a', encoding="utf-8") as f:
        f.write(json.dumps(list1))
        f.write('\n')
        f.write(json.dumps(list2))
    print('完成！')
