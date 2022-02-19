def create_phone_number(n):
    phone_number = '('
    for i, num in enumerate(n): #melakukan pengulangan dengan enumerate agar diambil sesuai dengan posisi indeks
        if i < 3: # pada saat angka mencapai indeks < 2 cth 111 maka
            phone_number += str(num) #angka akan ditambah dengan awalan (
            if i == 2: #pada saat iterasinya sudah mencapai indeks kedua
                phone_number += ') ' #maka angka ditutup dengan ) dan spasi
        elif i <= 13: #menentukan angka selanjutnya setelah indeks ke dua
            phone_number += str(num) #memasukkan angka pada indeks sisanya
            if i == 5: # 3 angka selanjutnya terletak pada indeks 3,4,5
                phone_number += '-' #saat mencapai i = 5 3 angka tadi akan dipisah dengan -
    return phone_number
