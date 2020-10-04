# 繰り返し坪数を調べるプログラム
while True:
    tubo = int(input("坪数は? "))
    m2 = tubo * 3.31
    s = "{0}坪は {1}平方メートルです".format(tubo, m2)
    print(s)

while True:
    weight = int(input("体重は？"))
    n2 = weight *3.31
    y = "{0}ツボは{1}平方メートルです".format(weight,n2)
    print(y)