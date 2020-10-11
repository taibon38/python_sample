class Person: #Personという型を作成
    def __init__(self,name,age):
        # print("test") #__init__が実行される時に出てくる。型の数分。
        self.name = name #nameという属性を持つ（生成されたインスタンスに名前をつけれる。人型のため、名前や年齢をつけたい）
        self.age = age

    def self_introduce(self): #Person型に紐付いた関数＝メソッド
        print("私の名前は"+self.name+"です")
        print("私の年齢は"+str(self.age)+"歳です")
        # print("私の年齢は"+str(weight)+"kgです")　引数も取れる。体重とかはインスタンスにあったほうがわかりやすいので、あくまでもここは引数が取れるという例

person1 = Person("Sato",28)   #Personという型を利用しインスタンスをつくる。selfは値を指定しなくてよい。　selfは、person1というインスタンスを示している。
print(type(person1)) #person1の型を調べる → Person型と表示。<class '__main__.Person'>)
print(person1.name,person1.age) #値を参照

person2 = Person("Sato2",30)  
print(type(person2)) 
print(person1.name,person1.age) #値を参照

person1.self_introduce(50)
person2.self_introduce(80)
