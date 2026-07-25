"""
Break Nedir?
    -Break döngüyü tamamen durdurmak için kullanılır. Koşul sağlandığında döngüden çıkar ve bir daha devam etmez.
"""

for i in range(10):
    if i == 5:
        break
    print(i)


"""
Continue nedir? 
    -O anki turu atlar, döngü devam eder. 
"""

for i in range(10):
    if i == 5:
        continue
    print(i)

"""
Pass Nedir?
    - Henüz kod yazılmamış yerde boş bırakmak için kullanılır.
    - Program hata vermez ama hiçbir işlem yapılmaz.
"""

if True:
    # Burayı sonra doldur
    pass

for i in range(3):
    if i == 1:
        pass
    print(i)


"""
Nested yapılar:
    - Bir yapının başka bir yapı içinde olması. 
    -if içerisinde if, for içerisinde if, if içerisinde while gibi
"""

# For içerisinde if örneği

for i in range(5):
    if i % 2 == 0:
        print(i)

# if içerisinde if örneği

yas = 20
ogrenci_olma_durumu = True

if yas > 18:
    if ogrenci_olma_durumu:
        print("Öğrenci indirimi uygulandı.")

# for içerisinde for örneği

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
