"""if yapısı: Bir koşul doğruysa kod bloğunu çalıştırır.
#Örnek:
if kosul:
     yapilacak_islem
"""

# Örnek:

from operator import truediv

sayi = 10
if sayi > 0:  # Eğer sayı sıfırdan büyükse
    print("Sayı pozitiftir.")  # Eğer bu koşul doğru ise print fonksiyonu çağrılır.

# if sayi >0:
# print("burası çalışmaz. Python girintili bir kod dilidir.")

# if else yapısı: else koşul yanlış ise çalışır.

sayi = -1
if sayi > 10:
    print("Sayı Pozitiftir.")
else:
    print("Sayı Negatiftir. ")

# if - elif - else : İlk doğru koşul çalışır, diğerleri kontrol edilmez. Hiçbiri doğru değilse, else çalışır.
# Örnek

ogrenci_notu = 72
if ogrenci_notu > 85:
    print("A")
elif ogrenci_notu > 70:
    print("B")
elif ogrenci_notu > 50:
    print("C")
elif ogrenci_notu > 30:
    print("D")
else:
    print("F")

# Mantıksal Operatörler: Birden fazla koşulun birleşme durumu

yas = 20
ogrenci = True

# Örnek: eğer öğrencinin yaşı 25ten küçükse ve öğrenci ise öğrenci indirimi uygula.

if yas < 25 and ogrenci == True:
    print("Öğrenci İndirimi Uygulandı.")

if yas < 25 or ogrenci == True:
    print("Öğrenci İndirimi Uygulandı.")

# If ve Liste kullanımı

meyveler = ["elma", "armut", "muz"]

if "elma" in meyveler:
    print("Elma Listede var.")
else:
    print("Listede yok.")

# Stok kontrol örneği:

meyveler = ["elma", "armut", "muz"]
urun = input("Bir meyve girin: ")

if urun in meyveler:
    print("Stokta mevcut.")
else:
    print("Stokta bulunamadı.")


