a_file = open("test2.txt", mode="w", encoding="utf-8")
try:
    a_file.write("""
    私は失敗したことがない。
    ただ、一万通りの方法を
    見つけただけだもの。
    みつを
    """)
finally:
    a_file.close()
