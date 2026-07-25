"""
For döngüsü kullanımı:

for degisken(x,y,z vb.) in koleksiyon:
    -yapilacak_islem

degisken : her turda değişen geçici isim
koleksiyon : liste,tuple gibi veri yapıları
"""

# Liste ile for döngüsü
sayilar = [10, 20, 30]

# #mantıksız girdi
# sayi1 = sayilar[0] + 5  # 10 +5
# sayi2 = sayilar[1] + 5  # 20 +5
# sayi2 = sayilar[2] + 5  # 30 + 5

for sayi in sayilar:
    print(sayi + 5)


# Range ile for döngüsü

for i in range(5):  # [0,1,2,3,4]
    print(i)

for i in range(1, 7):
    print(i)

# For ile toplama işlemi

sayilar = [10, 20, 30]

toplam = 0
for sayis in sayilar:
    print(sayis)
    toplam = toplam + sayis
print(toplam)

# For + if kullanımı:

sayilar = [1, 2, 3, 4, 5, 6]
for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"Çift : {sayi}")

# string üzerinden for

kelime = "ucanble"

for harf in kelime:
    print(harf)
