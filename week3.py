class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun})"

class Majalah(Buku):
    def __init__(self, judul, penulis, tahun, edisi):
        super().__init__(judul, penulis, tahun)
        self.edisi = edisi

    def info(self):
        return f"{self.judul} - Edisi {self.edisi} ({self.tahun})"

try:
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    tahun = int(input("Tahun: "))
    tipe = input("Buku atau Majalah? ")

    if tipe.lower() == "majalah":
        edisi = input("Edisi: ")
        item = Majalah(judul, penulis, tahun, edisi)
    else:
        item = Buku(judul, penulis, tahun)

    print("=== Informasi ===")
    print(item.info())

    with open("koleksi.txt", "a") as file:
        file.write(item.info() + "\n")

except ValueError:
    print("Tahun harus berupa angka.")
