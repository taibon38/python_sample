# ------モジュール------
# import syaku as sya
# print(sya.syaku_to_cm(10))

# from syaku import syaku_to_cm as s2cm
# print(s2cm(20))

# ------じゃんけん------
# import random
# hand = ["グー","チョキ","パー","ゲーム終了"]

# print("===じゃんけんスタート！===")
# while True:
#     com = random.randint(0,2)
#     for i,desc in enumerate(hand):
#         print(i,":",desc)
#     you = int(input("出す手を数値で入力"))
#     if you == 3:break
#     if you < 0 or you > 2 :
#         print("0~3で入力してね")
#         continue
#     print("---")
#     print("自分",hand[you])
#     print("自分",hand[com])
#     input("---")

#     j = (you - com + 3) % 3
#     if j == 0:
#         print("あいこ")
#     elif j == 1:
#         print("負け(T_T)")
#     else :
#         print("勝ち＼(^o^)／")
#     input("---")

# ------enmurateの内容チェック------
# hand = ["グー","チョキ","パー","ゲーム終了"]

# for x, y in enumerate(hand):
#   print("{0}:{1}".format(x, y))
  