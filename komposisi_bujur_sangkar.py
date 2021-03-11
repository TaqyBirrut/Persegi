def cekBujurSangkar(panjang,lebar):
    #Cek bujur sangkar atau tidak
    if panjang == lebar:
        return("Bujur sangkar")
    else:
        return("Tidak bujur sangkar")

def luas(panjang,lebar):
    #Mencari luas
    luas = panjang*lebar
    return luas

def cekLuasGenapGanjil(panjang,lebar):
    luas = panjang*lebar
    if luas %2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def keliling(panjang,lebar):
    #Mencari keliling
    keliling = panjang*2 + lebar*2
    return keliling

def cekKelilingGenapGanjil(panjang,lebar):
    keliling = panjang*2 + lebar*2
    if keliling %2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def cekPanjangGenapGanjil (panjang):
    #Cek panjang genap ganjil
    if panjang %2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def cekLebarGenapGanjil(lebar):
    #Cek lebar genap ganjil
    if lebar %2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def main():
    #Kamus
    panjang = int(input("Panjang = "))
    lebar = int(input("Lebar = "))
    print(50*"=")

    #Output
    segi = (cekBujurSangkar(panjang,lebar))
    Mluas = (luas(panjang,lebar))
    Aluas = (cekLuasGenapGanjil(panjang,lebar))
    Mkeliling = (keliling(panjang,lebar))
    Akeliling = (cekKelilingGenapGanjil(panjang,lebar))
    cekJenisPanjang = (cekPanjangGenapGanjil(panjang))
    cekJenisLebar = (cekLebarGenapGanjil(lebar))
    print("Segi =",segi)
    print("Luas =",Mluas)
    print("Luas = ",Aluas)
    print("Keliling =",Mkeliling)
    print("Keliling =",Akeliling)
    print("Panjang =",cekJenisPanjang)
    print("Lebar =",cekJenisLebar)
main()


