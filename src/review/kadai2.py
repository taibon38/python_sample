# Q1. 1〜30の整数のうち、偶数だけを要素として持つリスト([2, 4, 6, ... 30])を出力するプログラムを書いてください。 
# ただし、print([2, 4, 6, ... 30]と全ての数字を書く方法は使わないでください。実装方法は複数あります。

list_even = list(range(2,31,2))
print(list_even)

# Q2. アジアの国リスト、ヨーロッパの国リスト、各国の首都がわかる辞書があります。これらの情報から、アジアの首都リストとヨーロッパの首都リストを作成して出力するプログラムを書いてください。
# (['東京', 'バンコク', 'ニューデリー']と['ローマ', 'アムステルダム', 'ベルリン']の2つのリストを作成、出力してください。要素の順番は気にしなくてOKです。)

asian_countries = ["日本", "タイ", "インド"]
european_countries = ["イタリア", "オランダ", "ドイツ"]

capitals = {
    "インド": "ニューデリー",
    "イタリア": "ローマ",
    "日本": "東京",
    "オランダ": "アムステルダム",
    "ドイツ": "ベルリン",
    "タイ": "バンコク",
}

asian_capitals = [] #アジア首都の空リストを作成
a = asian_capitals

european_capitals = [] #ヨーロッパ首都の空リストを作成
e = european_capitals

for i in range(len(asian_countries)): #アジアの国名リストの長さを取得し範囲を設定
    a.append(capitals[asian_countries[i]]) #capitals辞書の中でアジア国名をキーとする値をリストaに追加
print(a)

for i in range(len(european_countries)): #ヨーロッパの国名リストの長さを取得し範囲を設定
    e.append(capitals[european_countries[i]]) #capitals辞書の中でアジア国名をキーとする値をリストaに追加
print(e)


# Q3. numbersリストから、数字の重複をなくした上で降順に並び替えたリストを作成し出力してください。([9, 8, 7, 4, 2]が出力結果となるプログラムを書いてください。)
numbers = [4, 2, 8, 2, 2, 7, 9, 4, 4, 9, 9]
unique = list(set(numbers)) #重複のないリストを作成
list.sort(unique,reverse=True) #降順を指定
print(unique)

# Q4. (名前、教科、得点)情報を保持するscoresリストがあります。名前ごとの総得点を集計して辞書として出力してください。
# 期待する出力結果: {'山田': 155, '高橋': 110, '佐藤': 180}

scores = [
    ("山田", "国語", 90),
    ("高橋", "国語", 50),
    ("佐藤", "国語", 100),
    ("山田", "数学", 65),
    ("高橋", "数学", 60),
    ("佐藤", "数学", 80),
] #リストの要素がタプルなため、タプル名[インデックス]で値を取得できる。この場合はi=インデックス番号かつタプル名になる。　print(i[0],i[2])で発行可能

total = {} #代入する空の辞書を作成
for i in scores: #scoresリストから、名前と得点を抽出
    if i[0] == "山田":
        total_score = i[2] + i[2]#同じ名前の得点を合算
        total["山田"] = total_score #total辞書に、キー:値として、 名前:総得点として追加。辞書オブジェクト[キー]=値


    elif i[0] == "高橋":
        total_score = i[2] + i[2]#同じ名前の得点を合算
        total["高橋"] = total_score #total辞書に、キー:値として、 名前:総得点として追加。辞書オブジェクト[キー]=値

    elif i[0] == "佐藤":
        total_score = i[2] + i[2]#同じ名前の得点を合算
        total["佐藤"] = total_score #total辞書に、キー:値として、 名前:総得点として追加。辞書オブジェクト[キー]=値    

print(total) #辞書リストをprint


# Q5. 名前リストがあります。それぞれの名前が"何人目か"がわかるようにして、順番に名前を出力してください。また、4人目以降の名前は出力しないでください。
# 期待する出力結果↓
# 1人目: 山田
# 2人目: 佐藤
# 3人目: 加藤

names = ["山田", "佐藤", "加藤", "高橋", "武田"]

for i in range(len(names)) : #namesの長さを取得し範囲を設定
    if i < 3:
        n = names[i]
        print(str(i+1)+"人目："+str(n)) #iのデフォルトが0のため、+1して1人目からスタート
    else:
        break  #4人目以降はループしない設定

# Q6. 現在の日付の1週間前と1ヶ月前の日付を"YYYY-MM-DD"の形式で出力してください。今日が2020年8月1日の場合、"2020-07-25"と"2020-07-01"を出力してください。
# ヒント: 月の計算にはpython-dateutilモジュールが使えます。
# pip3 install python-py でモジュールをインストール

import datetime
from dateutil.relativedelta import relativedelta

one_week_ago = datetime.date.today() - relativedelta(weeks=1) #1週間前を算出
one_month_ago = datetime.date.today()- relativedelta(months=1) #1ヶ月前を算出
print(one_week_ago)
print(one_month_ago)

# Q7. 以下に定義したStudentクラスは、各生徒の名前と教科ごと(国語、算数、英語)の点数を管理するためのクラスです。
# このクラスの中に、各生徒の平均点を出力するインスタンスメソッドを定義してください。

import math

class Student:
    def __init__(self, name, japanese, math, english):
        self.name = name
        self.japanese = japanese
        self.math = math
        self.english = english
    
    # ここにインスタンスメソッドを定義してください。
    def ave(self):
        result = (self.japanese + self.math + self.english) / 3
        return math.ceil(result)

student1 = Student("山田", 80, 100, 90)
student2 = Student("高橋", 90, 40, 90)
# ここでインスタンスメソッドを呼び出すと"山田さん", "高橋さん"それぞれの平均点が出力されるようにしてください。

print(f"{student1.name}さんの平均点は{str(student1.ave())}点です")
print(f"{student2.name}さんの平均点は{str(student2.ave())}点です")

# Q8. 変数postal_codeで指定された郵便番号に対応する住所を出力するプログラムを書いてください。
# 住所の取得には、郵便番号検索API(http://zipcloud.ibsnet.co.jp/doc/api)を使ってください。
# ヒント: APIを利用するにはrequestsモジュールを使います。

postal_code = "0790177" # この郵便番号に対応する住所「北海道美唄市上美唄町協和」が出力結果となります。

import json
import sys
import requests

RECEST_URL = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={0}".format(postal_code)
address = "" 
response = requests.get(RECEST_URL)
json_result = response.text #json文字列から辞書型へ変換
json_to_dic_result = json.loads(response.text)
# print(json_to_dic_result)

if json_to_dic_result["message"] == None:
    result_dic = json_to_dic_result["results"][0]
else:
    print("お探しの住所は見つかりませんでした(´・∀・｀)")
    sys.exit()

for i in range(1, 4):
    address += result_dic["address" + str(i)]

print(address)

# # 以下はinputして呼び出す版
#  #ハイフンありなしどちらでも入力可能
# postal_code = input("郵便番号を入力してください(7桁)") #呼びだすAPI元のURL
# RECEST_URL = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={0}".format(postal_code)
#  #住所
# address = "" #住所のカナ
# kana = ""

# response = requests.get(RECEST_URL)
# json_result = response.text #json文字列から辞書型へ変換
# json_to_dic_result = json.loads(response.text)
#  #該当する情報の判定 
# if json_to_dic_result["message"] == None:
#     result_dic = json_to_dic_result["results"][0]
# else:
#     print("お探しの住所は見つかりませんでした(´・∀・｀)")
#     sys.exit()

# for i in range(1, 4):
#     address += result_dic["address" + str(i)]
#     kana += result_dic["kana" + str(i)]

# context = {"郵便番号:": postal_code, "カナ:": kana, "住所:": address}

# print("|-- {0:^10} --|".format("検索結果"))
# for k, v in context.items():
#     print(k, v)