year=int(input("Укажите год: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Это високосный год")
        else:
            print("Это не високосный год")
    else:
        print("Это високосный год")
else:
    print("Это не високосный год")
