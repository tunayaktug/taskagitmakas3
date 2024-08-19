import random

def tas_kagit_makas_Tunay_Aktug():
    # Oyunun tanıtımı
    print("tas, kagit, makas oyunuma hos geldiniz.")
    print("oyun kurallari:")
    print("* tas, makas karsisinda sayi alir.")
    print("* makas, kagit karsisinda sayi alir.")
    print("* kagit, tas karsisinda sayi alir.")
    print("* iki tur kazanan oyunu kazanir.")

    # Oyunun seçenekleri
    secenekler = ['tas', 'kagit', 'makas']
    
    def bilgisayarin_secimi():
        return random.choice(secenekler)
    
    def sonucu_belirle(oyuncu, bilgisayar):
        if oyuncu == bilgisayar:
            return 'Beraberlik'
        elif (oyuncu == 'tas' and bilgisayar == 'makas') or \
             (oyuncu == 'makas' and bilgisayar == 'kagit') or \
             (oyuncu == 'kagit' and bilgisayar == 'tas'):
            return 'oyuncu kazandi'
        else:
            return 'bilgisayar kazandi'

    # Oyunun başlatma kısmı
    basla_komutu = input("oyunu baslatmak icin 'basla' yazin: ").lower()
    if basla_komutu != 'basla':
        print("yanlis komut. oyun baslatilamadi. cikis yapiliyor...")
        return

    # Oyunun ana döngüsü
    while True:
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            oyuncu_secimi = input("tas, kagit, makas seceneklerinden birini secin: ").lower()

            if oyuncu_secimi not in secenekler:
                print("gecersiz seçenek, lütfen tekrar deneyin.")
                continue

            bilgisayar_sec = bilgisayarin_secimi()
            print(f"bilgisayarin secimi: {bilgisayar_sec}")

            sonuc = sonucu_belirle(oyuncu_secimi, bilgisayar_sec)
            print(f"sonuc: {sonuc}")

            if sonuc == 'oyuncu kazandi':
                oyuncu_galibiyetleri += 1
            elif sonuc == 'bilgisayar kazandi':
                bilgisayar_galibiyetleri += 1

            print(f"skor: Oyuncu {oyuncu_galibiyetleri} - {bilgisayar_galibiyetleri} Bilgisayar")

        if oyuncu_galibiyetleri == 2:
            print("tebrikler! oyunu oyuncu kazandi.")
        else:
            print("üzgünüm! oyunu bilgisayar kazandi.")

        devam_et = input("baska bir oyun oynamak ister misiniz? (evet/hayir): ").lower()
        if devam_et != 'evet':
            print("oyun bitti. cikis yapiliyor...")
            break

        # Bilgisayarın devam etmek isteyip istemediğini rastgele belirleme
        if random.random() < 0.5:
            print("bilgisayar oyunu birakmak istiyor. maalesef cikis yapiliyor...")
            break
        else:
            print("bilgisayar da başka bir oyun oynamak istiyor. devam edelim")

# Fonksiyonun çalıştırılması
tas_kagit_makas_Tunay_Aktug()
