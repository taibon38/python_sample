# # 印税を計算する関数 --- (*1)
# def calc_royalty(price, sales, per):
#     rate = per / 100
#     ro = int(price * sales * rate)
#     return ro

# # ユーザーから情報を入力してもらう --- (*2)
# i = input("定価は？")
# price = int(i)

# i = input("発行部数は？")
# sales = int(i)

# i = input("印税率(パーセント)は？")
# per = float(i)

# # 結果を表示する --- (*3)
# v = calc_royalty(price, sales, per)
# print("印税は、", v, "円です")

def inzei(price,sales,per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro 

i = input("定価は？")
price = int(i)

i = input("部数は？")
sales = int(i)

i= input("印税率は？")
per = float(i)

kekka = inzei(price,sales,per)
print("印税は",kekka,"円です")


