#integer
yas=32
ogrenci_sayisi=55000
sicaklik=-15

print(yas)
print (35)

#hesaplama

a=10
b=5

toplam=a+b
print(toplam)

carpma=a*b
print(carpma)

cikarma=a-b
print(cikarma)

bolme=a/b
print(bolme)

#Demo

urun_sayisi=8
birim_fiyati=10
toplam=urun_sayisi*birim_fiyati
print(toplam)

#Zam Uygulaması
birim_fiyat=10
yuzde=int(input("Zam oranını giriniz: "))
zamli_fiyat=birim_fiyat+birim_fiyat*yuzde/100
print(zamli_fiyat)

#Float: kesirli sayılar nokta ile ayrılır.

pi=3.14
sicaklik=35.5
urun_fiyati=99.99

print(sicaklik)

#matematiksel işlemler

a=3.5
b=2.0

print(a+b) #toplama
print(a/b) #bölme

#ondalık hassasiyeti
print(0.1+0.2)

#yuvarlama (round)
sonuc=0.1+0.2
print(sonuc)

sonuc_yuvarlanmis=round(sonuc,2)
print(sonuc_yuvarlanmis)

#Proje: Gelen fiyat üzerinden KDV (%20)hesaplama

fiyat=float(input("Fiyatı giriniz: "))
print (fiyat)
kdvli_fiyat=fiyat+20*fiyat/100
print(kdvli_fiyat)

