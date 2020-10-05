# (動物,最高時速)のリスト（各要素はタプルで作成）
animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ", 80),
]

# 足の速い順に並び替える
faster_list = sorted(
    animal_list,  # 第1引数→リストやタプルなどのデータ型
    key = lambda ani : ani[1], # 第2引数 →無名関数 
    reverse = True) # 第3引数→reverse = True or False を指定。 デフォルトは昇順。Trueにすると降順。

# 結果を表示
for i in faster_list: print(i)

