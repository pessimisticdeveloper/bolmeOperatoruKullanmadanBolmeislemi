#Verilen iki sayıyı bölme operatörü kullanmadan birbirine bölen algoritma yazın. Recursive fonksiyonları kullanın..

def bolme(bolunen,bolen):
    if bolen == 0:
        return 0
    if bolunen - bolen == 0:
        return 1
    return 1 + bolme(bolunen - bolen,bolen)
sonuc = bolme(100,20)

print(sonuc)