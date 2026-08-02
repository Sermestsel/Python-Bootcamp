# Dosyaya Yazma
dosya = open("yeni_dosya.txt", "w", encoding="utf-8")
dosya.write("Merhaba Dünya\n")
dosya.write("Python Öğreniyoruz")
dosya.close()

# Okuma, İşleme, Kaydetme


# Okuma
dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

# İşleme
yeni_icerik = icerik.upper()

# Kaydetme
dosya = open("islenmis_ornek.txt", "w", encoding="utf-8")
dosya.write(yeni_icerik)
dosya.close()
