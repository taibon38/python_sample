# クラスを設計したところ
class Human:
    ''' 人間を表すクラス '''
    
    def search(self, place):
        '''周りを見る処理'''
        pass
      
    def take(self, food):
        '''物を掴む処理'''
        self.food = food
        
    def open_mouth(self):
        '''口を開ける処理'''
        pass
        
    def eat(self):
        '''食物を食べる処理'''
        print(self.food+"を食べました")

hito = Human() #インスタンス = クラス名()
hito.take("Banana")
hito.eat()