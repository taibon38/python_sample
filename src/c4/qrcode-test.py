# パッケージをインポート
import qrcode
# QRコードを生成
img = qrcode.make("http://kujirahand.com/")
# ファイルに保存
img.save("qrcode-test.png")

import qrcode
img = qrcode.make("https://twitter.com/papapp0731")
img.save("qrcode-test-twitter.png")