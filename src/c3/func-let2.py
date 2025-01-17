# 関数を定義
def mul_func(a, b): return a * b
def add_func(a, b): return a + b

# 引数に関数を要求する関数を定義 --- (*1)
def calc_5_3(func):
    return func(5, 3) # --- (*1a)

# 引数に関数を指定する --- (*2)
result = calc_5_3(mul_func)
print(result) # 表示結果→ 15

# 引数に他の関数を指定する --- (*3)
result = calc_5_3(add_func)
print(result) # 表示結果→ 8

def calc_10_3(func2):
    return func2(10,3)
result2 = calc_10_3(mul_func)
print(result2)

result2 = calc_10_3(add_func)
print(result2)