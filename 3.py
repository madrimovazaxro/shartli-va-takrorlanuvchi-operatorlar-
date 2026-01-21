import os
os.system("cls")

summa = int(input("Summani kiriting: "))
if 100000 <= summa <= 500000:
    chegirma = 15     
elif 501000 <= summa <= 1000000:
    chegirma = 25
elif summa > 1000000:
    chegirma = 40

total =summa -  summa * chegirma//100
print(f"Sizga {chegirma}% chegirma berildi. Siz to'laydigan {total} so'm!")