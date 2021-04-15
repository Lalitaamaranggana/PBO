class Karyawan:
    jumlah_karyawan = 0
 
    def __init__(self, nama, gaji, kelamin):
        self.nama = nama
        self.gaji = gaji
        self.kelamin = kelamin
        Karyawan.jumlah_karyawan += 1
 
    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
 
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print("Kelamin :", self.kelamin)
        print("________________")
 
karyawan1 = Karyawan("Sarah", 1000000, "laki-laki")
karyawan2 = Karyawan("Dodo", 2000000, "waria")
karyawan3 = Karyawan("pak dengklek", 10000, "perempuan")
 
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)
 
 
