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

# x を2倍する無名関数
x2 = lambda x : x * 2
print(x2(10))

# lambda練習（三角形の面積） lambda 引数：処理
tri = lambda a,b:a*b/2
print(int(tri(3,4)))

# map() ※リストに対する処理
nums = [1,3,5,7,9]
x2 = lambda x : x * 2  #値を2倍にする無名関数を定義
result = list(map(x2,nums)) # map(function,iterable,...) 第1引数→関数オブジェクト 第2引数→リストやタプルなど複数の値を持てるデータ型。第1引数の関数を第2引数に全て適応。
print(result)

# map() 短い版（lamda式は代入しなくてもできる）
result2 = list(map(lambda x : x * 3 ,nums))
result3 = list(map(lambda x : x * 4 ,nums))
print(result2)
print(result3)

# filiter() filiter(function,iterable,...) 第1引数→関数オブジェクト 第2引数→リストやタプルなど複数の値を持てるデータ型。第1引数の関数を第2引数に全て適応。
nums = [1,3,5,7,9,11,14,26,67,77,88,99,101]
result4 = list(filter(lambda x : (x % 2) == 1 , nums))
print(result4)

result5 = list(filter(lambda x : (x > 88) , nums))
print(result5)

# sorted()
## (動物,最高時速)のリスト（各要素はタプルで作成）
animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ", 80),
]

##足の速い順に並び替える
faster_list = sorted(
    animal_list,  # 第1引数→リストやタプルなどのデータ型
    key = lambda ani : ani[1], # 第2引数 →無名関数 ani[1]は、タプル無いの2つめの引数を指定している。（つまり「58」、「110」など)
    reverse = True) # 第3引数→reverse = True or False を指定。 デフォルトは昇順。Trueにすると降順。

## 結果を表示
for i in faster_list: print(i)

# sorted() 辞書型の場合
# 辞書型で動物:最高時速を表したもの
hero_dict = {
    "b.ハルク": 58 ,
    "a.アイアンマン": 110  ,
    "d.キャプテン": 60 ,
    "c.ティ・チャラ": 80 
}

# 時速で並び替えて表示
li = sorted(
    hero_dict.items(), # 辞書型データに対し、items()メソッドを実行すると、タプルのリストに変換してくれる。
    key = lambda x: x[0],
    reverse = False)
for name,speed in li:
    print(name,speed)


# イテレータの確認
i = iter(range(1,4))
print(i)
