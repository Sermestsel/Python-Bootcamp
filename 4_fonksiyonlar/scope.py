"""
Scope: (Lokal ve Global)
    -Bir değişkenin nerede erişilebilir olduğunu ifade eder
    -Bir değişken nerede tanımlıysa orada geçerlidir.

"""

# local (Yerel) değişken: Fonksiyon içinde tanımlanan değişkene denir


def testLocal():
    x = 10
    print(f"Fonksiyon içi: {x}")


testLocal()
# print(x)  # NameError: name 'x' is not defined

# Global (Genel) değişken: Fonksiyon dışında tanımlanan değişken

x = 15


def testGlobal():
    print(f"Fonksiyon içi: {x}")


testGlobal()

# Aynı isimli değişkenler:

x = 11


def testSame():
    x = 5
    print(f"Fonksiyon İçi : {x}")


testSame()
print(f"Fonksiyon dışı: {x}")


# global anahtar kelimesi:

x = 9


def testKey():
    global x
    x = 5  # local -> global


testKey()
print(x)
