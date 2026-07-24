#Veri Tipi Kontrolü
x=10
print(type(x)) #<class 'int'>
x="10"
print(type(x)) #<class 'str'>

#Yanlış tipte işlem örneği
# print("255" + 5) #TypeError: can only concatenate str (not "int") to str

#Tip Dönüşümleri (casting)

x="25" #str
print(type(int(x))) #int'e çevrildi.
print(type(float(x))) #Float'a çevrildi.

x=25 #int
print(type(str(x))) #String'e çevrildi.

sayi=int(input("Bir Sayı Girin : "))
print(sayi)
print(type(sayi))

# print(int("abc"))  ValueError: invalid literal for int() with base 10: 'abc'
