# for 構文をフラグで分岐する場合
# 食材の一覧
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

# マンゴーがないか確認する
# flag_found = False
# for food in foodstuff:
#     if food == "Mango":
#         flag_found = True
#         break

# if flag_found:
#     print("マンゴーが入ってます")
# else:
#     print("ありません。")


flag_found = False
for food in foodstuff:
    if food == "Natto":
        flag_found = True
        break
if flag_found:
    print("納豆が入っています")
else:
    print("安心して食べれますよ")