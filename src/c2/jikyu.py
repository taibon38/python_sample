# 時給計算プログラム

# 時給の入力 --- (*1)
user = input("時給はいくらですか？")
jikyu = int(user)

# 時間の入力
user = input("何時間働きましたか？")
jikan = int(user)

# 計算 --- (*2)
kyuryou = jikyu * jikan

# 結果を表示 --- (*3)
fmt = """
時給{0}円で、{1}時間働いたので...
給料は、{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)

###### 移動時間計算式
user = input("km/hの速さですか？")
speed = int(user)

user = input("何km移動しましたか？")py
kyori = int(user)

time = speed * kyori

fmt = """
時速{0}kmで、{1}km移動したので、
移動時間は{2}時間です。
"""
kotae = fmt.format(speed,kyori,time)
print(kotae)

