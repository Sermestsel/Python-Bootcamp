# print: ekrana çıktı üretir

print("Merhaba")
"""
girdi: "Merhaba"
işlem: ekrana yazdırma
çıktı: Merhaba
"""

# len: veri yapısı uzunluğu
liste = [1, 2, 3]
print(len(liste))
"""
girdi: liste
işlem: eleman sayısı hesaplama
çıktı: 3
"""

# type: değişkenin veri tipi
x = 3.14
print(type(x))
"""
girdi: x
işlem: veri tipi öğrenme
çıktı: <class 'float'>
"""

# veri tipi dönüşüm fonksiyonları: int(), float(), str()
sayi = "10"
print(int(sayi))
"""
girdi: sayi
işlem: veri tipi dönüştürme
çıktı: Integer, 10
"""
# sum(), max(), min()= toplama, en büyüğü bulma, en küçüğü bulma

sayilar = [1, 2, 3, 5]
print(sum(sayilar))  # 11
print(max(sayilar))  # 5
print(min(sayilar))  # 1

# abs(): mutlak değer

x = -8
print(abs(x))  # 8

# round()
x = 4.10297380
print(round(x, 3))  # 4.103

# sorted()

siralama = [5, 3, 7, 9, 1, 2]
print(sorted(siralama))  # [1, 2, 3, 5, 7, 9]
