# coding:UTF-8
# 入力を得てインチをセンチメートルに変換
# 変換の元になる値
per_inch = 2.54
# ユーザーから入力を得る
user = input("何インチですか? ")
# 浮動小数点型に変換する
inch = float(user)
# 計算
cm = inch * per_inch
# 結果を表示
desc = "{0}インチ = {1}センチ".format(inch, cm)
print(desc)

per_cm = 0.01
user2 = input("何センチですか？")
cm = float(user2)
m = cm * per_cm
size = "{0}センチ = {1}メートル".format(cm,m)
print(size)