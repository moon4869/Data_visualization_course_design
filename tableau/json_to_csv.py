import json

with open('maoyan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    ctry = data['score']
    with open('score.csv', 'a', encoding='utf-8') as f1:
        for k, v in ctry.items():
            f1.write(k + ',' + str(v) + '\n')
