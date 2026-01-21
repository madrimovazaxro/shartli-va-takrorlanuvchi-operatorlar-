import os
os.system("cls")

while(True):
    son = int(input("Son: "))
    match son:
        case 12: fasl, oy, oy_nomi = "qish", 1, "Dekabr"
        case 1: fasl, oy, oy_nomi = "qish", 2, "Yanvar"
        case 2: fasl, oy, oy_nomi = "qish", 3, "Fevral"
        case 3: fasl, oy, oy_nomi = "bahor", 1, "Mart"
        case 4: fasl, oy, oy_nomi = "bahor", 2, "Aprel"
        case 5: fasl, oy, oy_nomi = "bahor", 3, "May"
        case 6: fasl, oy, oy_nomi = "yoz", 1, "Iyun"
        case 7: fasl, oy, oy_nomi = "yoz", 2, "Iyul"
        case 8: fasl, oy, oy_nomi = "yoz", 3, "Avgust"
        case 9: fasl, oy, oy_nomi = "kuz", 1, "Sentyabr"
        case 10: fasl, oy, oy_nomi = "kuz", 2, "Oktyabr"
        case 11: fasl, oy, oy_nomi = "kuz", 3, "Noyabr"
        case _: 
            print("Noto'g'ri raqam kiritildi!")
            exit()
    print(f"Yilning {son}-oyi {fasl} faslining {oy}-oy {oy_nomi}")  
