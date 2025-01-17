# 料金を計算
import math

# 計算を行うクラスを定義 --------- (*1)
class CalcFee:
    def __init__(self):
        ''' 初期化処理 '''
        self.shipping_fee = 1000 # 送料
        self.tax_rate = 0.08     # 税率
        self.value = 0           # 合計
        
    def addItem(self, price):
        ''' 商品の値段を加算する '''
        self.value += price 
        
    def calc(self):
        ''' 最終的な料金を計算する '''
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v = math.ceil(total + tax)
        return v

# 実際の計算を行う ------------ (*2)
fee1 = CalcFee() #CalcFeeクラスから、fee1インスタンスを生成。
fee1.addItem(500) #priceプロパティに500という値を追加。
print(fee1.calc(), "円") #fee1インスタンスにおいて、calc関数を実行(アイテム合計500円+送料1000円)×1.08% 

fee2 = CalcFee()
fee2.shipping_fee = 1500 #送料を1500円に更新
fee2.addItem(800) #800円の商品を追加
fee2.addItem(500) #500円の商品を追加
print(fee2.calc(), "円")

fee3 = CalcFee()
fee3.shipping_fee = 2000
fee3.tax_rate = 0.1
fee3.addItem(1000)
fee3.addItem(500)
fee3.addItem(100)
print(fee3.calc(),"円") #関数を実行。() で実行。
