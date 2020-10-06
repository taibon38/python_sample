# (1) テキストファイルを開く
a_file = open("mt7_7.txt", encoding="utf-8")
b_file = open("mt7_7_sjis.txt", encoding="sjis")

# (2) テキストを読む
s = a_file.read()
y = b_file.read()

# (3) ファイルを閉じる
a_file.close()
b_file.close()

# 結果を表示する
print(s)
print(y)

