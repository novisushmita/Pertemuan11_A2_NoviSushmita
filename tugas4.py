def jumlah(daftar_angka, pemisah):
    total = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            total += angka
    return total

# penggunaan 1
daftar1 = [20, 25, 30, 35, 40]
pemisah1 = 10

hasil1 = jumlah(daftar1,pemisah1)
print("Hasil 1 : ",hasil1)

# penggunaan 2
daftar2 = [13, 15, 42, 45, 60, 65, 83, 85]
pemisah2 = 5

hasil2 = jumlah(daftar2,pemisah2)
print("Hasil 2 : ",hasil2)