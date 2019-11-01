import json
count = 0
box_offc = {}
res = open('boxoffice.csv', 'a', encoding='utf-8')
for i in range(32):
    filename = str(i) + '.json'
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        # print(data)
        querydate = data['data']['queryDate']
        movielist = data['data']['list']
    for movie in movielist:
        if count == 10:
            break
        name = movie['movieName']
        value = float(movie['boxInfo'])
        # if value[-1] == '亿':
        #     value = float(value[:-1]) * 10000
        # if value[-1] == "万":
        #     value = float(value[:-1]) * 1
        if box_offc.get(name):
            box_offc[name] += value
        else:
            box_offc[name] = value
        # temp_list.append(name)
        # temp_list.append(str(box_offc[name]))
        # temp_list.append(querydate)
        # temp_res = ','.join(temp_list) + '\n'
        # print(temp_res)
        # res.write(temp_res)
        count += 1
        # temp_list.clear()
    temp_list = []
    for k, v in box_offc.items():
        temp_list.append(k)
        temp_list.append(str(v))
        temp_list.append(querydate)
        temp_res = ','.join(temp_list) + '\n'
        print(temp_res)
        res.write(temp_res)
        temp_list.clear()
    count = 0
res.close()
# print(box_offc)
# with open('color.json', 'a', encoding='utf-8') as f1:
#     f1.write(json.dumps(box_offc, ensure_ascii=False))
