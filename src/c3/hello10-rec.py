# 再帰関数を定義
def say_hello(i):
    if i <= 0: return
    print("ハロー", i)
    say_hello(i-1)
# 実行
say_hello(10)

def say_ohayo(i):
    if i <= 0 :return
    print("おはよう",i)
    say_ohayo(i-2)
say_ohayo(20)