# Yazım Hatası (Syntax Error)

if 5 > 3:  # SyntaxError: expected ':'
    print("ok")  # NameError: name 'ok' is not defined

# Name Error ( Tanımsız Değişken )
# Örnek:
# print(x)  # NameError: name 'x' is not defined

# Type Error ( Tip Uyuşmazlığı )
# Örnek :
# print("10" + 5)  # TypeError: can only concatenate str (not "int") to str

# Value Error ( Değer Uygun Değil )
# Örnek:
# int("Umut")  # ValueError: invalid literal for int() with base 10: 'Umut'

# Zero Division Error (Sıfıra Bölme Hatası)
# Örnek:
# print(10 / 0)  # ZeroDivisionError: division by zero

# Index Hatası
# Örnek
liste = [1, 2, 3, 4]
# print(liste[10])  # IndexError: list index out of range

# Key Error (Sözlükte Anahtar Hatası )
# Örnek:
ogrenci = {"isim": "umut"}
# print(ogrenci["yas"])  # KeyError: 'yas'

# File Not Found
# Örnek:
# with open("umut.txt", "r") as f:
# print(f.read())  # FileNotFoundError: [Errno 2] No such file or directory: 'umut.txt'

# Attribute Hatası (yanlış metod özellik hatası)
# Örnek
sayi = 10
# sayi.append(5)  # AttributeError: 'int' object has no attribute 'append'