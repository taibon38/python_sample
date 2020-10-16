meibo = {"tarou": {"age": 30, "live": "tokyo"},
         "hanako": {"age": 25, "live": "kanagawa"},
         "kenta": {"age": 27, "live": "tokyo"},
         "miyo": {"age": 22, "live": "chiba"},
         }

print(meibo) #辞書の要素をすべて取得できる。
# {'tarou': {'age': 30, 'live': 'tokyo'}, 'hanako': {'age': 25, 'live': 'kanagawa'}, 'kenta': {'age': 27, 'live': 'tokyo'}, 'miyo': {'age': 22, 'live': 'chiba'}}

print(meibo.keys()) #キーの一覧を取得できる
# dict_keys(['tarou', 'hanako', 'kenta', 'miyo']) 

print(meibo.values()) #値の一覧を取得できる
# dict_values([{'age': 30, 'live': 'tokyo'}, {'age': 25, 'live': 'kanagawa'}, {'age': 27, 'live': 'tokyo'}, {'age': 22, 'live': 'chiba'}])

print(meibo.items()) #辞書に含まれるすべてのキーと値の組み合わせを取得
# dict_items([('tarou', {'age': 30, 'live': 'tokyo'}), ('hanako', {'age': 25, 'live': 'kanagawa'}), ('kenta', {'age': 27, 'live': 'tokyo'}), ('miyo', {'age': 22, 'live': 'chiba'})])

for key ,value in meibo.items(): #for文と組み合わせることですべての値を順番に取り出すことができる
    print(f"key:{key},values:{value}")

print(meibo["tarou"]) #キーを指定で値を取得
#{'age': 30, 'live': 'tokyo'}

print(meibo["tarou"]["age"]) #tarouの中の辞書データから、ageキーを指定して値を取得
#30

print("―――――――――――――――――――")
#すべてのageだけ取り出したい時の処理

for i in meibo.keys():
    print(meibo[str(i)]["age"])


print("―――――――――――――――――――")
#辞書の中にリストや辞書が混在している場合に、id を取り出したいときの処理

meibo2 = {"tarou": {"age": 30, "live": "tokyo"},
         "hanako": {"age": 25, "live": "kanagawa"},
         "kenta": {"age": 27, "live": "tokyo"},
         "miyo": {"age": 22, "live": "chiba"},
         "rest": [{"id": "abcde", "date": "181119", "fullname": "tanakajirou"},{"name": "tai"}],
         }

print(meibo2['rest'][1]) #rest 内の、キー1 を呼び出し
#{'name': 'tai'}

print(meibo2['rest'][1]['name']) #rest 内の、インデックス1　nameに紐付いた valueを呼び出し
#tai
print(meibo2['rest'][0]["fullname"]) #rest 内の、インデックス0のnameに紐付いた valueを呼び出し