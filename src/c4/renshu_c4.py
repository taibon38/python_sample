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
  
# ------datetime------
import datetime
d = datetime.date.today()
print(d)

t = datetime.datetime.now()
t.strftime("%Y/%m/%d %H:%M:%S")
print(t)

##特定の日付を指定する方法
s = datetime.date(2020,10,8)
print(s)
## 変数に日付を代入
## 1週間後を計算
s_1week_after = s+datetime.timedelta(weeks=2)
print(s_1week_after)

## 3日前を計算
s_3day_before = s-datetime.timedelta(days=3)
print(s_3day_before)

## 日付の差を計算
a = datetime.date(2020,10,8)
b = datetime.date(1992,10,8)
c = a-b 
print(c)

s_sabun = s_1week_after - s_3day_before 
print(s_sabun)

# 正規表現
import re #正規表現のモジュールを取り込む
pat = r"\d+"  #raw stringの記述 \d は、任意の数値を取る。
str = "This pen is yen300." #文字列
a = re.search(pat,str) #正規表現検索
print(a)

import re
pattern = r"\w+"  #raw stringの記述 \w は、任意の英数字を取る。
str = "This pen is 100yen." #文字列
b = re.search(pattern,str) #正規表現検索
print(b)

c = re.search(r"^abc$","abc") #^は先頭。　$は末尾。
print(c)

d = re.search(r"^abc$","abcd") #マッチしない例。Noneと結果が返ってくる。
print(d)
