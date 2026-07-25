#Verileri Anahtar-Değer (Key-Value) mantığıyla saklar.
#Liste indeks, Sözlük(Dictionary) Anahtar ile çalışır.


ogrenci={ #isim = Anahtar, ali = value
    
    "isim":"ali",
    "yas":25,
    "bolum":"bilgisayar"
}

print(ogrenci)

#Dictionary'e erişim
print(ogrenci["isim"])
print(ogrenci["yas"])

#dictionary yeni değer ekleme
ogrenci["not"]=85
print(ogrenci) #{'isim': 'ali', 'yas': 25, 'bolum': 'bilgisayar', 'not': 85}

#dictionary değer güncelleme
ogrenci["yas"]=26
print(ogrenci)

#dictionary eleman silme
del ogrenci["bolum"]
print(ogrenci)

#Anahtar ve değer al
print(ogrenci.keys()) #anahtar
print(ogrenci.values()) # değer
print(ogrenci.items()) #anahtar - değer
"""
dict_keys(['isim', 'yas', 'not'])
dict_values(['ali', 26, 85])
dict_items([('isim', 'ali'), ('yas', 26), ('not', 85)])
"""

