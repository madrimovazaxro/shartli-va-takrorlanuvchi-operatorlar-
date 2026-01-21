import os
os.system("cls")

ball = float(input("Ball: "))
if ball >= 60:
    print("Tabriklaymiz! Siz imtihondan o’tgansiz")
elif ball > 100 or ball < 0:
    print("Xato ball!")
elif ball < 60:
    print("Afsus, siz imtihondan yiqilgansiz")
    