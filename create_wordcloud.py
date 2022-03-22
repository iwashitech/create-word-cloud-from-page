# -*- coding: utf-8 -*-
"""
"""

import os
import MeCab
from wordcloud import WordCloud

user_name = os.environ['USERPROFILE'].replace('\\', '/')

def mecab_analysis(text):
    t = MeCab.Tagger('-Ochasen')
    node = t.parseToNode(text) 
    output = []
    while(node):
        if node.surface != "":
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

# page_text.txtのテキストをコピペする
text = "テキスト"
#wakati = MeCab.Tagger("-Owakati")
#words = wakati.parse(text)

words = " ".join(mecab_analysis(text))

stop_words = [u'感じ', u'思い', u'思っ', u'行っ', u'とても', u'たくさん', u'行く', u'行き', u'いき', u'ため', u'もう', u'あっ', u'いい', u'てる', u'よく', u'いっ', u'くれ', u'今回', u'おり', u'でき', u'こちら', u'やっ', u'おき', u'かけ', u'頂き', u'下さる', u'ちゃっ', u'しまっ', u'下さい', u'くださっ', u'こんなに', u'下さっ', u'どう', u'あと', u'ちょっと', u'まし', u'から', u'あり', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', u'くれる', u'やる', u'くださる', u'なっ', u'しまう', u'られ', u'なり', u'さま', u'しまい', u'そう', u'せる', u'した', u'思う', u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て', u'に', u'を', u'は', u'の', u'が', u'と', u'た', u'し', u'で', u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'ます', u'です', u'ませ', u'ください', u'もの']

wc = WordCloud(width=1200, height=800, background_color='white', colormap='autumn', font_path='HGRGM.TTC', stopwords=set(stop_words))
wc.generate(words)
wc.to_file(user_name + '/Desktop/wordcloud.png')
