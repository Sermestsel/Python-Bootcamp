"""
Dosya İşlemleri:
    -Dosyadan veri okuma
    -okunan veri işlenmesi
    -dosyaya veri yazma ve kaydetme
    -with yapısı

Proje

Neden Dosya İşlemleri?
    - Yapay Zeka veriden öğrenir, veri python ortamına yüklenir ve işlenir. Bu nedenle dosyalama önemlidir.

    Dosya Nedir? Tipleri: Verinin kalıcı olarak saklandığı yapıdır.
        -kullanıcı listeleri
        -not kayıtları
        -log dosyaları
        -csv veri dosyaları
"""

# Dosya Açma ve Okuma

dosya = open("ornek.txt", "r", encoding="utf-8")
# ornek.txt : dosya,
# "r" read modu
# encoding="utf-8" #Türkçe karakterlerin okunmasına olanak tanır
icerik = dosya.read()  # tüm dosyayı okur
print(icerik)
dosya.close()

# Satır Satır Okuma
dosya = open("ornek.txt", "r", encoding="utf-8")
for satir in dosya:
    print(satir.strip())
dosya.close()

# Dosya İçeriğinin İşlenmesi
# Okunan veri üzerinde işlem yapma

dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()
print("**" * 20)
print(icerik)
# İçeriği büyük harfe dönüştürme
yeni_icerik = icerik.upper()
print(f"yeni içerik: \n{yeni_icerik}")

# Satır sayısını bulmak:
dosya = open("ornek.txt", "r", encoding="utf-8")
satirlar = dosya.readlines()
dosya.close()
print(f"Toplam Satır : {len(satirlar)}")
