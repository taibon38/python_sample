# ここに「商品」を表すItemクラスを定義してください。
# Itemクラスは、商品名(name)と値段(price)属性を持つ設定をしてください。

class Item:
    def __init__(self,i_name,price): #初期化処理
        self.i_name = i_name
        self.price = price


    def name_price(self):
        print("選択された商品："+self.i_name+":"+str(self.price)+"円")

# ここに「人」を表すPersonクラスを定義してください。
# Personクラスは、名前(name)、残高(balance)、保有商品(items)を属性として持つ設定をしてください。
# 保有商品を表すitems属性は、「どの商品を何個購入したか」を管理できるようにしてください。辞書型を使って、キーを商品名、バリューを個数にすると良いと思います。ex.) {"Item1(チョコ)": 3, "Item2(アメ)": 1}

class Person:
    def __init__(self,p_name,balance,items): #初期化処理
        self.p_name = p_name
        self.balance = balance
        self.items = {}

# Itemクラスからインスタンスを3つ作って、それぞれ変数(item1〜3)に代入してください。
# 属性(商品名、値段)に設定する値はなんでも構いません。
item1 = Item("りんご",100)
item2 = Item("みかん",50)
item3 = Item("メロン",300)

# 作成したItemインスタンスは、itemsリストで管理します。
items = [item1, item2, item3]

# Personクラスからインスタンスを2つ作って、それぞれ変数(person1, 2)に代入してください。
# person1は500円の残高、person2は700円の残高を持つ設定にしてください。保有商品は1つもない設定にしてください。
person1 = Person("佐藤",500,"")
person2 = Person("高橋",700,"")

# ここからは、説明文で要求されていることが実現できるように実装してください。
# 関数を作ったり、クラス内にインスタンスメソッドを作ったりして実装してみてください。


# 1. 「ユーザー名と残高の表示」
# ↓コンソールに、以下の様に名前と残高を出力してください。まずは、person1の名前と残高を出力してください。出力したら、「2.購入商品の質問」をしてください。
# 〇〇さん。あなたの残高は、500円です。

def shopping(self):

    while True:
        print(f"{self.p_name}さん。あなたの残高は{str(self.balance)}円です")
        
# 2.「購入商品の質問」
# 以下の様に、質問文と選択肢(商品番号、商品名、値段)をコンソールに出力し、ユーザーから入力を受け取れるようにしてください。商品番号は1から連番で割り振られるようにしてください。
# ↓ 質問文と選択肢をコンソールに出力
# どの商品を買いますか？番号で選択してください。購入処理を終了する場合は0を押してください。
# 1. チョコ 100
# 2. アメ 80
# 3. ガム 130

        item_select_question = "どの商品を買いますか？番号で選択してください。購入処理を終了する場合は0を押してください。\n"

        for i, item in enumerate(items, 1):
            # ↓文字列の前にfを置くf-stringという書き方をしています
            item_select_question += f"{i}. {item.i_name} {item.price}\n"
            #print(item_select_question) で、インデックス番号とname、priceが取得されることがわかる
        user = int(input(item_select_question))

# 3.「ユーザーの回答によって処理を切り分ける」1

# 「購入商品の質問」でユーザーが入力した値に応じて、以下の処理をしてください。
# ユーザーが0を入力した場合 → 「購入処理を終了しました。」と出力する。「4.購入個数の確認」以降の処理はせずに⭐️に移る。
# ユーザーが1〜3を入力した場合 → 「4.購入個数の確認」に移る。
# ユーザーが4〜を入力した場合 → 「正しい値を入力してください。」と出力して、もう一度「1.ユーザー名と残高の表示」に戻る。

        if user == 0 :
            print("購入処理を終了しました")
            break

        elif user >= 4 :
            print("正しい値を入力してください")
            # person1.name_balance()  
            # user = int(input(item_select_question))
            continue 

        else :
            print("正しく入力できました")


# 4.「購入個数の確認」
# 以下のように、「3.購入商品の質問」でユーザーが選んだ商品名&値段と「何個買いますか?」を出力した上で、ユーザーから入力を受け取れるようにしてください。
# コンソールに出力
# 選択された商品: アメ: 80円。何個買いますか？
        if user == 1 :
            item1.name_price() 
            price = item1.price
            count = int(input("何個買いますか？"))

        elif user == 2 :
            item2.name_price()
            price = item2.price
            count = int(input("何個買いますか？"))

        elif user == 3 :
            item3.name_price()
            price = item3.price
            count = int(input("何個買いますか？"))
            

# 5.「決済処理」
# ここまでで、ユーザーが選択した商品と個数から、トータルの金額が求められます。(アメ80円を2個買ったら、トータル金額は160円。)
# トータルの金額 > ユーザー残高の場合 → 「残高不足です。もう一度選択してください。」と出力して、「1.ユーザー名と残高の表示」に戻ってください。
# トータルの金額 <= ユーザー残高の場合 → 購入金額の分だけ、ユーザーの残高を減らしてください。ユーザーの「保有商品」に購入された商品と個数を追加してください。その上で、もう一度「ユーザー名と残高の表示」に戻ってください。
# 「購入商品の質問」はユーザーが0を入力するまでずっと繰り返されます。

        total = price *count  
        # 合計確認用 → print("合計"+str(total)+"円です")
        if input() == 0 :
            break
        elif total > self.balance:
            print("残高不足です。もう一度選択してください。") 
            continue

        else :  #total <= person1.balance
            self.balance = self.balance - total
            count += count
            self.items.setdefault(item.i_name,count)#上書きせずに、第一引数(キー)と第二引数(バリュー)を、self.itemsの辞書型に追加。
            print(f"残額は{str(self.balance)}円です")

shopping(person1)            

# ⭐️ person1について、1〜5までの処理が終わったら(ユーザーが0を入力したら)、person2についても同じ処理をしてください。person2でも処理が終わったら、「6.ステータスの表示」に移ってください。

shopping(person2)        

# 6.「ステータスの表示」
# ここまでの購入処理によって、ユーザーの「残高」と「保有商品」が更新されているはずです。
# person1とperson2の最終的なステータスを出力してください。
# ex.)
# --------ステータス---------
# 名前: 山田, 残高: 120円, 保有商品: チョコ: 3個,アメ: 1個
# 名前: 高橋, 残高: 700円, 保有商品: なし

print("--------ステータス---------")
print(f"名前：{person1.p_name}, 残高:{str(person1.balance)}円, 保有商品:{person1.items}")
print(f"名前：{person2.p_name}, 残高:{str(person2.balance)}円, 保有商品:{person2.items}")
