isim = input("İsminizi giriniz: ")
sifre = int(input("Şifrenizi giriniz: "))
bakiye = 1000
print("Merhaba,", isim, ". Kayıt başarıyla tamamlandı. Başlangıç bakiyesi: ", bakiye, "TL.")

while True:
    print("\nYapmak istediğiniz işlemi seçiniz:")
    print("1- Para Çek")
    print("2- Para Yatır")
    print("3- Bakiye Sorgula")
    print("4- Çıkış")

    islem = int(input("Seçiminiz: "))

    if islem == 1:
        cekmek = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if cekmek > bakiye:
            print("Yetersiz bakiye .")
        else:
            bakiye -= cekmek
            print("Para çekme başarılı. Kalan bakiye:", bakiye, "TL.")

    elif islem == 2:
        yatirmak = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        if yatirmak <= 0:
            print(", sıfır veya negatif para yatmaz ki.")
        else:
            bakiye += yatirmak
            print("Para yatırma başarılı. Yeni bakiye:", bakiye, "TL.")

    elif islem == 3:
        print("Mevcut bakiyen:", bakiye, "TL.")

    elif islem == 4:
        print("Çıkış yapılıyor, kendine iyi bak .")
        break

    else:
        print("Geçerli bir işlem seçmedin moruk, tekrar dene.")
