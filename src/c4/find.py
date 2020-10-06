# テキストからキーワードを探す
key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
    # 一行ずつファイルを読む
    for i, line in enumerate(tf):
        # 文字列 key が行に含まれるか？
        if line.find(key) >= 0:
            print(i+1, ":", line)

# 練習
key2 = "ironman"
with open("mt7_7.txt",encoding="utf-8") as tt:
    for i2,line2 in enumerate(tt):
        if line2.find(key2) >=0:
            print(i2+1 , ":",line2) #行番号を出すためにインデックスに+1している。デフォは0スタート

# enumerateの結果確認
with open("mt7_7.txt",encoding="utf-8") as tt:
    for i2,line2 in enumerate(tt):
        print(i2 , ":",line2)