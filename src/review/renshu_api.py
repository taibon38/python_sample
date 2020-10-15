#ぐるなびアクセスキー：58606bab6f638851759987006856adcc
#参考にしたページ：https://qiita.com/ume1126/items/14e9c1b0662acc289b19
#レストラン検索API：https://api.gnavi.co.jp/api/manual/restsearch/

import requests
import pprint
import json

#レストラン検索APIのURL
url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

#パラメータの設定
params={}
params["keyid"] = "58606bab6f638851759987006856adcc" #取得したアクセスキー
params["freeword"] = "戸田"

#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json() # 読まなきゃいけない！じゃないと<Response [200]>とでるだけ。 [200]というのは、成功という意味。
# print(result_api) # 整形せずにそのまま表示
# pprint.pprint(result_api) # 整形して表示

print(result_api['rest'][0]['address'])  #Q.なぜ1件のみ？？
# 無事に住所が表示されました
print(result_api['rest'][0]['name_kana'])
# カナも表示されました
print(result_api['rest'][0]['code']['areaname'])
# 地域名
print(result_api['rest'][0]['code']['category_name_l'][:2])
#URL
print(result_api['rest'][0]['url'])

hit = len(result_api['rest'])
print(f"{hit}件ヒット！")  #Q.なぜ10件のみ？？

# ループで、ヒットした10件分の店名を表示させる
for i in range(hit): #range()の使い方。開始から終了までの連続した数値を要素として持つrange型オブジェクトを作成する　https://note.nkmk.me/python-range-usage/
    print(result_api['rest'][i]['name'])
    print(result_api['rest'][i]['url'])
