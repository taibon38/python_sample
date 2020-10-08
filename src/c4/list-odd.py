# (1) 二倍して1を引く方法
data = [ (i * 2 - 1) for i in range(1, 6) ]
print(data)

# (2) range()を工夫する方法
data = [ i for i in range(1, 11, 2) ] #1~10を2ステップずつ表現
print(data)

# (3) 内包表記で for と if を組み合わせる方法
data = [ i for i in range(1, 11) if i % 2 == 1 ] 
print(data)


##練習
data = [ (i*2-1) for i in range(10) ] #10個の奇数が出される。
print(data)

data = [(i*2-1) for i in range(1,11)] #1から10までを2倍して1を引いたものが出される
print(data)

data = [i for i in range(1,11) if i % 2 == 1] 
print(data)
