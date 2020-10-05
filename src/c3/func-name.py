# 関数の定義
def calcTime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

# 通常の呼び出し --- (*1)
print( calcTime(500, 100) )
# 名前付き引数の呼び出し --- (*2)
print( calcTime(dist=500, speed=100) )

def inzei(teika,sales,per):
    value = per /100
    m = int(teika * sales * value)
    return m

print(inzei(1000,100,10))
print(inzei(teika=1000,sales=100,per=10))