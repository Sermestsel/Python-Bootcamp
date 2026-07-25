# =================================================================
#                              SORU 1:
# Kullanıcıdan bir sayı alınacak
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırılacak.
# =================================================================


print("Cevap 1")
sayi = int(input("Bir sayı giriniz: "))
if sayi < 0:
    print("Sayı Negatif")
elif sayi > 0:
    print("Sayı Pozitif")
else:
    print("Sayı 0'dır.")

print("*" * 50)

# =================================================================
#                              SORU 2:
# 1'den 10'a kadar (10 dahil) sayılar yazdırılacak
# Bu sayılar toplanacak.
# =================================================================

print("Cevap 2")
total = 0

for i in range(1, 11):
    print(i)
    total += i
print(total)

print("*" * 50)


# =================================================================
#                              SORU 3:
# Kullanıcıdan q alana kadar sürekli giriş alınacak
# Kullanıcı her giriş yaptığında "Girdiniz: " şeklinde ekrana yazdırılacak
# Kullanıcı q'ya basarsa çıkış yapılacak. =================================================================

print("*" * 50)
print("Cevap 3")
giris = ""
while giris != "q":
    giris = input("Girdi yapılacak metni girin (Çıkmak için q tuşuna basın.) : ")
    if giris != "q":
        print(f"Girdiniz : {giris}")
print("Çıkış yapıldı.")

# =================================================================
#                              SORU 4:
# 1'den 20ye kadar sayılara gidilecek,
# Eğer sayı çiftse "Çift", tekse "Tek" yazılacak.
# Sayı 10'dan büyükse "Büyük", değilse "Küçük / Eşit" yazılacak
# =================================================================

print("*" * 50)

for i in range(1, 21):
    if i % 2 == 0:
        sayi = "Çift"
    else:
        sayi = "Tek"
        if i < 10:
            durum = "Küçük / Eşit"
        else:
            durum = "Büyük."

    print(f"{i} - {sayi} - {durum}")
