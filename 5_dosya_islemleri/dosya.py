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


dosya = open("ornek.txt", "r", encoding="utf-8")
for satir in dosya:
    print(satir.strip())
dosya.close()
