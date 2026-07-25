"""
while kosul:
    yapilacak_islem
"""

# Örnek
i = 0
while i < 5:
    print(i)
    i = i + 1

# Sayaç Mantığı:
sayac = 1
while sayac <= 3:
    print("Merhaba")
    sayac += 1

# While + if kullanımı

i = 0
while i < 10:
    if i % 2 == 0:
        print(f"Çift: {i}")

    i += 1

# kullanıcı kontrollü while döngüsü
giris = ""
while giris != "q":
    giris = input("Çıkış için q'ya basın: ")
    print(f"Kullanıcı mesajı: {giris}")
