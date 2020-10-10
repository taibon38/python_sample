# # 文字列のエスケープ \を使う
# print('I can\'t play the guitar.')
# print("I like \"Orange\".")

# # 数値を文字列に変換する
# kion = 30
# print("今日の気温は",str(kion),"度です")

# # formatの活用
# per_inch = 2.54
# inch = 24 
# cm =  inch * per_inch
# print("{0}インチは{1}センチ".format(inch,cm))

# # inputの活用 時給計算プログラム
# user = input("時給はいくらですか？")
# time = input("何時間働きましたか？")

# salary = int(user) * int(time)
# print(salary,"円です！どうぞ。")

# # if の活用  if: else:は同じインデント。
# # 偶数と奇数の判別
# user = int(input("好きな数字を入れてください"))
# if user % 2 == 0:
#     print("それは偶数ですね。")
# else:
#     print("それは奇数ですね。")

# while（条件付きの繰り返し構文）繰り返し坪数を調べるプログラム
# while True:
#     user = input("坪数は？")
#     if user == "" or user == "q" :break #繰り返しを抜け出す処理
#     tubo = int(user)
#     m2 = tubo*3.31
#     s = "{0}坪は、{1}㎡です".format(tubo,m2)
#     print(s)

# for (範囲付きの繰り返し構文) 1から10まで足し算するプログラム

r = 0
for i in range(1,11):
    r = int(r + i)
    print("{0}を足すと{1}".format(i,r))
    if r >= 40 :break
print("1から10を足すと",r)

