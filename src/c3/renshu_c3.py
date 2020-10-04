# coding:UTF-8

# 辞書型データの作成
ages = {'suzuki':30,'sato':28,'tanaka':58}
print(ages)

# 辞書型データの参照と設定
##参照
b = ages['suzuki']
print(b)
print(ages['tanaka'])

##設定
ages['takahashi'] = 40
print(ages)