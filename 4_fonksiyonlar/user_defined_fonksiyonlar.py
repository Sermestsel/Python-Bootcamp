"""Fonksiyon tanımlama: def

def fonksiyon_adi():
    kod_bloğu
"""

# Selamlama Fonksiyonu Tanımlama


def selam_ver():
    print("Merhaba")


# Selamlama Fonksiyonunu Kullanma ("Çağırma")
selam_ver()


# parametre kullanımı
def selam_ver(isim):
    print(f"Merhaba, ben {isim} akıllı asistanıyım")


selam_ver("SermYo")


# Birden Fazla Parametre Kullanımı
def selam_ver(isim, selamlama_cumlesi):
    print(isim + " " + selamlama_cumlesi)


selam_ver("SermYo", "Hoş Geldiniz.")


# Return kullanımı
def topla(a, b):
    sonuc = a + b
    print(f"Sonuç : {sonuc}")
    return sonuc


toplama_islemi_sonucu = topla(3, 8)
print(f"Toplama İşlemi Sonucu : {toplama_islemi_sonucu}")


# Birden fazla değer döndürme
def hesapla(a, b):
    toplam = a + b
    carpim = a * b
    return toplam, carpim


hesapla_toplam, hesapla_carpim = hesapla(3, 9)
print(f"Toplam: {hesapla_toplam}")
print(f"Çarpımı: {hesapla_carpim}")


# Varsayılan Parametre
def selam(isim, mesaj="Merhaba"):
    print(f"{isim} {mesaj}")


selam("SermYo")
selam("Umuth")
selam("Rith")
selam("Umut", "Nasılsın?")


def selam(isim, yas, meslek, c, lr, epoch):
    """
    Description: Bu fonksiyon selamlama yapar.
    İnput:
        isim(str): Kullanıcı Adı
        yas (int): Kullanıcı Yaşı
        meslek(str): Kullanıcı Mesleği
        c,
        lr,
        epoch
    Output: None
    """

    print(isim, yas, meslek, c, lr, epoch)


# Keyword Argüman
selam("Umut", 32, "Bilg Progr.", "0.01", "0.001", "1000")
selam(isim="Umut", yas=32, meslek="Bilg Progr.", c="0.01", lr="0.001", epoch="1000")


# Type Hint (Modern Python)
def topla(a: int, b: int) -> int:
    return a + b


print(topla(3, 5))


# Fonksiyon içinde fonksiyon kullanımı:
def kare(x):
    kare = x**2  # x*x
    return kare


def yazdir(x):
    print(kare(x))


yazdir(5)
