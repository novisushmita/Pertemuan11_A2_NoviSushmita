def penjumlahan(nilai1, nilai2):  # operasi penjumlahan
    penjumlahan = print("Hasil : ",nilai1+nilai2)
    return penjumlahan

def pengurangan(nilai1, nilai2):  # operasi pengurangan
    pengurangan = print("Hasil : ",nilai1-nilai2)
    return pengurangan

def perkalian(nilai1, nilai2):  # operasi perkalian
    perkalian = print("Hasil : ",nilai1*nilai2)
    return perkalian

def pembagian(nilai1, nilai2):  # operasi pembagian
    pembagian = print("Hasil : ",nilai1/nilai2)
    return pembagian

def show_menu():  # fungsi untuk menampilkan menu
    print("\n")
    print("----------- KALKULATOR ----------")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Exit")
    menu = int(input("PILIH OPERASI> "))
    if menu != 5:
        nilai1 = float(input("Masukkan angka pertama: "))
        nilai2 = float(input("Masukkan angka kedua: "))
    print("\n")
    if menu == 1:
        penjumlahan(nilai1, nilai2)
    elif menu == 2:
        pengurangan(nilai1, nilai2)
    elif menu == 3:
        perkalian(nilai1, nilai2)
    elif menu == 4:
        pembagian(nilai1, nilai2)
    elif menu == 5:
        exit()
    else:
        print("Operasi tersebut tidak ada!")

if __name__ == "__main__":
    while True:
        show_menu()