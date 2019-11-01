from wordcloud import WordCloud
import PIL.Image as Image
import numpy as np
import jieba
import json


with open('comment.json', 'r', encoding='utf-8') as fp:
    temp_list = json.loads(fp.read())
    text = ''.join(temp_list)
word_list = jieba.cut(text)
jieba_res = ' '.join(word_list)
mask = np.array(Image.open('word.jpg'))
wordcloud = WordCloud(
    mask=mask,
    background_color='white',
    font_path='msyh.ttc',
    max_words=130
).generate(jieba_res)
wordcloud.to_file('wordcloud_new.png')
img_res = wordcloud.to_image()
img_res.show()
