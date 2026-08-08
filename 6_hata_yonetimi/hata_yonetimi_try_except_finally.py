# Try - Except - Else - Finally

"""
Try - Except
    - program hata verdiğinde çakılmasın durumu.
    - hata olursa yakalayıp kontrollü şekilde yönetmesi.
"""

# try:
#     sayi = int(input("Sayı Giriniz: "))
#     print(10 / sayi)

# except:
#     print("Bir hata oluştu.")
# print("Program başarılı bir şekilde çalışmaya devam ediyor.")


# Belirli bir hata yakalama yöntemi:

from sys import exception

try:
    sayi = int(input("Sayı Giriniz: "))
    print(10 / sayi)
except ValueError:
    print("Lütfen bir sayı giriniz.")
except ZeroDivisionError:
    print("Sıfıra Bölme yapılamaz.")

# else: hata yoksa çalışır.

try:
    sayi = int(input("Bir Sayı Girin:"))
    sonuc = 10 / sayi
except (ValueError, ZeroDivisionError):
    print("Hatalı Giriş.")
else:  # Hata yoksa çalışan taraf
    print(f"Sonuç : {sonuc}")

# Finally: Her durumda çalışır
try:
    dosya = open("veri.txt", "r", encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya Bulunamadı.")
finally:  # Her Durumda Çalışır.
    print("Her İhtimalde çalışır Finally.")

# Raise : Kendi hatamızı özellikle oluşturmak
yas = int(input("Yaş : "))
if yas < 0:
    raise ValueError("Yaş negatif olamaz.")  # ValueError: Yaş negatif olamaz.

# Genel hata ayıklama mantığı

try:
    sayi = int(input("Bir Sayı Girin:"))
    print(10 / sayi)
except Exception as e:
    print(f"Hata : {str(e)} ")
