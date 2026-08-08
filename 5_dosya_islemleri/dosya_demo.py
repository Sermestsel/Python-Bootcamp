"""
Soru 1
"notlar.txt" adında bir dosya oluşturulacak
içine 5 öğrencinin notu yazılacak. Her satır ayrı olacak
"""

with open("ogrenci_notu.txt", "w", encoding="utf-8") as dosya:
    dosya.write("10\n" + "20\n" + "30\n" + "40\n" + "50\n")

"""
Soru 2
Dosya okunacak
-Notların Ortalaması Hesaplanacak
-En Yüksek Not,
-En Düşük Not bulunacak.
"""
notlar = []

with open("ogrenci_notu.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        notlar.append(int(satir.strip()))

ortalama = sum(notlar) / len(notlar)
maks = max(notlar)
mins = min(notlar)

print("Notlar:", notlar)
print("Ortalama : ", ortalama)
print("Maksimum : ", maks)
print("Minimum : ", mins)

"""
Soru 3
Eğer ortalama 50'den büyükse "Sınıfı Geçti", değilse "Kaldı" "sonuc.txt" dosyasına kaydet.
"""

if ortalama < 50:
    sonuc = "Sınıfta Kaldı"
else:
    sonuc = "Sınıfı Geçti"

with open("sonuc.txt", "w", encoding="utf-8") as durum:
    durum.write(f"Ortalama : {ortalama}\n")
    durum.write(f"Sonuç : {sonuc}")

print("Dosyaya Kayıt Edildi.")
