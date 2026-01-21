import os
import time
os.system("cls")

choice = input("Bomba ishga tushsinmi? (ha/yo'q): ")
if choice == 'ha':
    for i in range(10, 0, -1):
        print(f"{i} soniya qoldi")
        time.sleep(1)
    print("Buuum!...")
else:
    print("Taymer ishga tushirilmadi!")