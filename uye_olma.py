while True:
    para = int(input("Ne kadar yatıracağınızı giriniz. "))
    if para <=5000:
        print("Standart üyesiniz.")
    elif  5000<para and 7000>para:
        print("Altın üyesiniz.")
    elif  7000<=para and 10000>=para:
        print("Platin üyesiniz.")
    elif  10001<para:
        print("Çekebilceğiniz en yüksek miktar 10000TL'dir.")
    else:
        print("Geçersiz komut girdiniz.")