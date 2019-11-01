# 转换编码
import json
with open('list1&2.json', 'r', encoding='utf-8') as f:
    while True:
        temp = f.readline()
        if temp and temp != '\n':
            data = json.loads(temp)
            with open("new_list.json", "a", encoding='utf-8') as f1:
                f1.write(json.dumps(data, ensure_ascii=False))
                f1.write('\n')
        if not temp:
            break
