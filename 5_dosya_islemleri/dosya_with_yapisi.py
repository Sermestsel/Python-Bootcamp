# With yapısı: Dosya kapanır, hata olsa bile kapanır, daha temiz bir kod yazılmış olur
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("With Yapısı")
    print(icerik)
    # otomatik bir şekilde kapanır

# With ile yazma
with open("with_dosya_yazma.txt", "w", encoding="utf-8") as dosya:
    dosya.write("With ile yazma işlemi gerçekleştirildi.")
