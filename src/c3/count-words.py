# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る --- (*1)
text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")  #print(text)すると、全部カンマなどがなくなってる。
words = text.split() #.split()を用いることで、特定の区切り文字を指定して文字列を区切ってリスト型を得れる。区切り文字を省略すると空白文字を元に文字列を分割。

# 単語を数える --- (*2)
counter = {}
for w in words: #wordsはリストになってるからここで範囲を指定。
    ws = w.lower() # 小文字に変換
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

# 結果を表示 --- (*3)
for k,v in sorted(counter.items()):
    if v >= 3:
        print(k, v)
