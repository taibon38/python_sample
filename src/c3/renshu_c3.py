# coding:UTF-8

# 辞書型データの作成
ages = {'suzuki':30,'sato':28,'tanaka':58}
print(ages)

# 辞書型データの参照と設定
##参照
b = ages['suzuki']
print(b)
print(ages['tanaka'])

##設定
ages['takahashi'] = 40
ages['suzuki'] = 29
print(ages)


# 文字列の演算
s1 = "abc"
s2 = "def"
s = s1 + s2
print(s)

# 複数生成
y = "@"
x = y * 3
print(x)

# 文字抽出
a = "0123456789"
b = a[2]
print(b)

# [1:4]の範囲をスライス
c = a[1:4]
print(c)

# stepの活用
d = a[0:9:2]
print(d)

# 文字列の分割（空白)
s = "This is a pen"
kugiri = s.split()
"-".join(kugiri)
print(kugiri)

# 文字列の分割（指定)
s = "2020/10/04"
ymd = s.split("/")
print(ymd)

# 文字列の連結
s = "2020/10/04"
ymd = s.split("/")
ymd2 = "-".join(ymd)
print(ymd2)

# 文字列の置換
s = "This is a pen"
change = s.replace('pen','banana')
search = s.find('is')
print(change)
print(search)



