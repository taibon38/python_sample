
# ここに「商品」を表すItemクラスを定義してください。
# Itemクラスは、商品名(name)と値段(price)属性を持つ設定をしてください。

class Item :
    def __init__(self,name,price): #初期化処理
        self.name = name
        self.price = price 

    def print_name_price(self):
        print(f"選択された商品：{self.name}。{self.price}円")

# ここに「人」を表すPersonクラスを定義してください。
# Personクラスは、名前(name)、残高(balance)、保有商品(items)を属性として持つ設定をしてください。
# 保有商品を表すitems属性は、「どの商品を何個購入したか」を管理できるようにしてください。辞書型を使って、キーを商品名、バリューを個数にすると良いと思います。ex.) {"Item1(チョコ)": 3, "Item2(アメ)": 1}

class Person:
    def __init__(self,name,balance): #関数の中で使うものだけ引数にいれる。インスタンスごとに値が変わらないものは消しちゃってOK。
        self.name = name
        self.balance = balance
        self.items = {}

# Itemクラスからインスタンスを3つ作って、それぞれ変数(item1〜3)に代入してください。
# 属性(商品名、値段)に設定する値はなんでも構いません。
item1 = Item("クッキー",100)
item2 = Item("せんべい",50)
item3 = Item("まんじゅう",200)

# 作成したItemインスタンスは、itemsリストで管理します。
items = [item1, item2, item3]

# Personクラスからインスタンスを2つ作って、それぞれ変数(person1, 2)に代入してください。
# person1は500円の残高、person2は700円の残高を持つ設定にしてください。保有商品は1つもない設定にしてください。
person1 = Person("sato",500)
person2 = Person("tanaka",700)

# ここからは、説明文で要求されていることが実現できるように実装してください。
# 関数を作ったり、クラス内にインスタンスメソッドを作ったりして実装してみてください。


# 1. 「ユーザー名と残高の表示」
# ↓コンソールに、以下の様に名前と残高を出力してください。まずは、person1の名前と残高を出力してください。出力したら、「2.購入商品の質問」をしてください。
# 〇〇さん。あなたの残高は、500円です。

def shopping(person):

    item_select_question = "どの商品を買いますか？番号で選択してください。購入処理を終了する場合は0を押してください。\n"

    for i,item in enumerate(items,1) :#enumerate（イテラブル,開始位置） →インデックス番号,要素の順に取得できる ※enumerateは、列挙するという意味
        item_select_question += f"{i}.{item.name} {item.price}\n" #item変数に、item1,item2,item3 を順番に代入していく。＋しているのは、それをつなげるから。+しないと、最後に代入されたitem3の値が出る。

    while True:
        print(f"{person.name}さん。あなたの残高は、{person.balance}円です。") #person引数を取る。

# 2.「購入商品の質問」
# 以下の様に、質問文と選択肢(商品番号、商品名、値段)をコンソールに出力し、ユーザーから入力を受け取れるようにしてください。商品番号は1から連番で割り振られるようにしてください。
# ↓ 質問文と選択肢をコンソールに出力
# どの商品を買いますか？番号で選択してください。購入処理を終了する場合は0を押してください。
# 1. チョコ 100
# 2. アメ 80
# 3. ガム 130

        item_number = int(input(item_select_question))

# 3.「ユーザーの回答によって処理を切り分ける」
# 「購入商品の質問」でユーザーが入力した値に応じて、以下の処理をしてください。
# ユーザーが0を入力した場合 → 「購入処理を終了しました。」と出力する。「4.購入個数の確認」以降の処理はせずに⭐️に移る。
# ユーザーが1〜3を入力した場合 → 「4.購入個数の確認」に移る。
# ユーザーが4〜を入力した場合 → 「正しい値を入力してください。」と出力して、もう一度「1.ユーザー名と残高の表示」に戻る。

        if item_number == "":
            continue
        elif item_number == 0:
            print("購入処理を終了しました")
            break
        elif item_number > len(items):
            print("正しい値を入力してください")
            continue
        else:
            print("正しく入力できました")

# 4.「購入個数の確認」
# 以下のように、「3.購入商品の質問」でユーザーが選んだ商品名&値段と「何個買いますか?」を出力した上で、ユーザーから入力を受け取れるようにしてください。
# コンソールに出力
# 選択された商品: アメ: 80円。何個買いますか？
        item = items[item_number-1]
        item.print_name_price()
        item_count = int(input("何個買いますか？"))
        price = item.price #itemsリストから抽出した番号の価格（ex:2を入力したら、50が表示される）

# 5.「決済処理」
# ここまでで、ユーザーが選択した商品と個数から、トータルの金額が求められます。(アメ80円を2個買ったら、トータル金額は160円。)
# トータルの金額 > ユーザー残高の場合 → 「残高不足です。もう一度選択してください。」と出力して、「1.ユーザー名と残高の表示」に戻ってください。
# トータルの金額 <= ユーザー残高の場合 → 購入金額の分だけ、ユーザーの残高を減らしてください。ユーザーの「保有商品」に購入された商品と個数を追加してください。その上で、もう一度「ユーザー名と残高の表示」に戻ってください。
# 「購入商品の質問」はユーザーが0を入力するまでずっと繰り返されます。

#残高チェックの処理
        total = item_count * price
        # print(f"合計{total}円です")
        if total > person.balance :
            print("残高不足です。もう一度選択してください。")
            continue
        else :
            person.balance -= total
            print(f"残高は{person.balance}円です")


#個数カウントの処理
        if item.name in person.items: #personの辞書リストに、item.nameが存在している場合の処理
            person.items[item.name] += item_count #辞書[キー] =値 で追加
            print(f"{item.name}を{item_count}個買いました。{item.name}は合計で{person.items[item.name]}個です。")

        elif item_count == 0:
            continue
        else:
            person.items[item.name] = item_count
            print(f"{item.name}を{item_count}個買いました。")


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

def status(person):
    print(f"名前:{person.name},残高:{person.balance}円,保有商品:",end='')
    if not person.items : #保有商品を表示させるコード
        print("なし")
    else:
        for name,count in person.items.items(): #person.itemsのキーと値を一つずつ代入
            result = f"{name}:{count}個"
            print(result,end='')
    
    
print("--------ステータス---------")

status(person1)
print("\n")
status(person2)