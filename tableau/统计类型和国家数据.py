import json
types = []
ctrys = []
type_c = {}
ctry_c = {}
with open('new_list.json', 'r', encoding='utf-8') as f:
    s1 = f.readline()
    types += eval(s1)
    s2 = f.readline()
    ctrys += eval(s2)
for i in types:
    if ',' in i:
        data = i.split(',')
        for j in data:
            if type_c.get(j):
                type_c[j] += 1
            else:
                type_c[j] = 1
    else:
        if type_c.get(i):
            type_c[i] += 1
        else:
            type_c[i] = 1

for i in ctrys:
    if ',' in i:
        data = i.split(',')
        for j in data:
            if ctry_c.get(j):
                ctry_c[j] += 1
            else:
                ctry_c[j] = 1
    else:
        if ctry_c.get(i):
            ctry_c[i] += 1
        else:
            ctry_c[i] = 1

with open('type_ctry.json', 'a', encoding="utf-8") as f:
    res = {}
    res['type'] = type_c
    res['ctry'] = ctry_c
    f.write(json.dumps(res, ensure_ascii=False))
print('-' * 50 + '成功' + '-' * 50)
