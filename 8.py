import os
os.system("cls")

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

for i in range(B, C+1):
    print(f"{A} ning {i} darajasi {A**i}")