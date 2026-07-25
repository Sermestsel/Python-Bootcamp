#Benzersiz (unique) elemanlardan oluşan bir veri yapısıdır. Aynı elemandan birden fazla kez olamaz.

#Set
sayilar={1,2,3,4}
print(sayilar)

#Set tekrar eden eleman

sets={1,2,2,3,3,3}
print(sets) #{1, 2, 3}

#Set Özellikleri: Setler sırasızdır. Indexi yoktur. 
#Örnek : print(sayilar[2])

#Listeyi Sete Çevirme Örneği: 

liste=[1,2,2,3,4,4]
benzersiz= set(liste)
print(benzersiz) #{1, 2, 3, 4}

#Set eleman ekleme

sayilar.add(5)
print(sayilar) #{1, 2, 3, 4, 5}

#Set eleman silme
sayilar.remove(2)
print(sayilar) #{1, 3, 4, 5}

#Set İşlemleri

a= {1,2,3}
b={3,4,5}

print(a.union(b)) #Birleşim #{1, 2, 3, 4, 5} 
print(a.intersection(b)) #Kesişim #{3}
print(a.difference(b)) #Fark #{1, 2}

