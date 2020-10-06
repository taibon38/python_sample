with open("mt7_7.txt", encoding="utf-8") as tf: #with open(ファイル名) as 変数名
    for line in tf:
        print(line)

tt = open("mt7_7.txt",encoding="sjis")

t = tt.read()
print(t)