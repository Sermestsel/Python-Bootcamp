#Birden fazla veriyi saklayan bir veri yapısıdır, listeden farkı ise tuple değiştirilemez.

#tuple

koordinatlar=(10,20)

renkler=("Kırmızı","Mavi","Yeşil")

#Liste ve Tuple farklı

liste=[1,2,3]
liste[0]=99 #çalışır
print(liste) # [99, 2, 3]

tup=(1,2,30)
# tup[0]=99
# print(tup) #TypeError: 'tuple' object does not support item assignment

#Tuple İndeksleme

t=(10,20,30)
print(t[1])
print(t[-1])

#Slicing

t=(10,20,30,40)
print(t[1:3])

#Tek Elemanlı Tuple

x=(5)
print(type(x)) #<class 'int'> döndürür. 

x=(5,) #Bu tek elemanlı tupledir.
print(type(x)) #<class 'tuple'> döndürür.

#tuple unpacking
koordinat=(10,20)
x,y=koordinat
print(x,y)

#Tuple metotları

t=(20,20,30,40)
print(t.count(20)) # 2
print(t.index(30)) # 2

