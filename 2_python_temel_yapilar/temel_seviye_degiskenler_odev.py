# ===============================================================
#                              Soru 1:
# Bir Değişken tanımlanacak: ad="Kaan", yas = 25, ortalam =3.45
# Bu değişkenlerin tiplerini type() ile yazdır.
# ===============================================================

ad = "Kaan"
yas = 25
ortalama = 3.45

print("Cevap 1:")
print(type(ad))
print(type(yas))
print(type(ortalama))

# ===============================================================
#                              Soru 2:
# Kullanıcıdan yaş bilgisi alınacak,
# Bu yaşın tipini ekrana bastırılacak ve 5 yıl ekleyip sonucu yazdırılacak
# ===============================================================
print("*" * 50)
print("Cevap 2:")
yas = input("Yaşınızı Girin: ")
print(type(yas))

yas_format_int = int(yas)
bes_yil = yas_format_int + 5
print(bes_yil)


# ===============================================================
#                              Soru 3:
# Bir ürün fiyatı (float) alınacak, %18 KDV hesaplancak.
# Toplam fiyatı 2 basamak olacak şekilde yazdırılacak.
# ===============================================================
print("*" * 50)
print("Cevap 3: ")
fiyat = float(input("Ürün fiyatını giriniz (Örn: 99.90): "))
kdv = fiyat * 0.18
toplam = fiyat + kdv
print("KDV Tutarı :", round(kdv, 2))
print("Toplam Tutar:", round(toplam, 2))

# ===============================================================
#                              Soru 4:
# Bir liste oluşturulacak: sayilar=[10,20,30,40,50]
# İlk eleman, son eleman yazdırılacak,
# 2. indexten sona kadar olan parça yazdırılacak
# Listeye 60 eklenecek
# Listedeki 20 değeri silinecek
# ===============================================================
print("*" * 50)
print("Cevap 4: ")
sayilar = [10, 20, 30, 40, 50]
print("İlk Index :", sayilar[0])
print("Son Index :", sayilar[4])
print("2. Indexten Sonrası: ", sayilar[2:])
sayilar.append(60)
print("60 eklenince: ", sayilar)
sayilar.remove(20)
print("20 çıkarılınca: ", sayilar)
# ===============================================================
#                              Soru 5:
# Bir tuple oluşturulacak: koordinat=(12,34)
# Değerler unpacking ile x ve y değişkenlerine alınacak ve yazdırılacak,
# Tuple'ın değiştirilemediğini göstermek için (yorum satırlı) örnek verilecek
# ===============================================================
print("*" * 50)
print("Cevap 5: ")
koordinat = (12, 34)
x, y = koordinat
print("Koordinatlar :", x, ",", y)
# koordinat[0]=23
# print(koordinat)

# ===============================================================
#                              Soru 6:
# Bir sözlük oluşturulacak: ogrenci={"isim":"Ayse","yas":22,"bolum":"Yazılım"}
# Öğrenci ismi yazdırılacak,
# not anahtarı eklenecek, 90 olacak
# yas değeri 23 olarak güncellenecek
# tüm anahtarlar ve tüm değerler yazdırılacak
# ===============================================================
print("*" * 50)
print("Cevap 6: ")
ogrenci = {"isim": "Ayse", "yas": 22, "bolum": "Yazılım"}
print(ogrenci["isim"])

ogrenci["not"] = 90
print(ogrenci)

ogrenci["yas"] = 23
print(ogrenci)
print("Anahtar:", list(ogrenci.keys()))
print("Değer:", list(ogrenci.values()))

# ===============================================================
#                              Soru 7:
# Bir set oluşturulacak: liste = ["Ali", "Ayse","Ali","Mehmet","Ayse"]
# Liste sete çevrilecek, benzersiz isimler yazdırılacak
# benzersiz isim sayısı yazdırılacak
# ===============================================================

print("*" * 50)
print("Cevap 7: ")

liste = ["Ali", "Ayse", "Ali", "Mehmet", "Ayse"]
benzersiz_isimler = set(liste)
print("İsimler : ", benzersiz_isimler)
print("Benzersiz İsim Sayısı:", len(benzersiz_isimler))

