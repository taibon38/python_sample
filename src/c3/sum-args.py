def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v

# 合計を表示
print(sumArgs(1, 2,3))
print(sumArgs(1, 2, 3, 4, 5))
print(sumArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def sumRensyu(*nums):
    a = 0 
    for n in nums:
        a = a + n
    return a
print(sumRensyu(1,3,4))
print(sumRensyu(6,6,6))