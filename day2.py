print("selamat Datang di Chatbot Perhitungan")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y 

def bagi(x, y):
    return x / y

while True:
    print('Mau hitung soal apa?\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Close')
    operasi = int(input('Silahkan pilih dalam bentuk angka: '))
    if operasi == 1:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print(f'Hasilnya adalah: {tambah(x, y)}\n')
    elif operasi == 2:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print(f'Hasilnya adalah: {kurang(x, y)}\n')
    elif operasi == 3:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print(f'Hasilnya adalah: {kali(x, y)}\n')
    elif operasi == 4:
        x = int(input('Masukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))
        print(f'Hasilnya adalah: {bagi(x, y)}\n')
    elif operasi == 5:
        break
    else:
        print('Operasi tidak ditemukan')
