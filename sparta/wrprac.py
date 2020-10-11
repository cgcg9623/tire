from wordcloud import WordCloud

text = ''
with open("동기방_group.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ','').replace('이모티콘\n','').replace('사진\n', '')

print(text)

wc = WordCloud(font_path="C:/WINDOWS/Fonts/NanumBarunGothic.ttf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
