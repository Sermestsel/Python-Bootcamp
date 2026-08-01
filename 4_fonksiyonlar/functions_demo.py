"""
Kullanıcıdan vize ve final notu alınacak
Ortalama hesaplaması yapılacak
Harf notu belirlenecek
Sonuç ekrana yazdırılacak
"""

# Not hesaplama sistemi


def ortalama_hesapla(vize: float, final: float) -> float:
    """
    Vize %40, Final %60 olacak
    """
    ortalama = vize * 0.4 + final * 0.6
    return ortalama


def harf_notu_belirle(ortalama: float) -> str:
    """
    Ortalama değerine göre harf notu döndürür.
    """
    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama >= 50:
        return "C"
    else:
        return "F"


def sonucu_yazdir(isim: str, ortalama: float, harf: str):
    """
    Sonucu ekrana yazdır
    """
    print("----------SONUÇ-------------")
    print(f"Öğrenci Adı : {isim}")
    print(f"Ortalama : {ortalama}")
    print(f"Harf : {harf}")


# Program akışı:
isim = input("Öğrenci Adı : ")
vize = float(input("Vize Notu Girin: "))
final = float(input("Final Notunu Girin : "))

ortalama = ortalama_hesapla(vize=vize, final=final)
harf = harf_notu_belirle(ortalama=ortalama)

sonucu_yazdir(isim=isim, ortalama=ortalama, harf=harf)
