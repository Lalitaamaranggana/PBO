class siswa:
    #class variabel
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, nama, kelas, lahir, asal, umur):
        self.nama = nama
        self.kelas = kelas
        self.lahir = lahir
        self.asal = asal
        self.umur = umur
        siswa.jumlah_siswa =+ 1
    #methode
    def viewSiswa(self):
        print("---------------------")
        print("Data Siswa")
        print("Nama  : ", self.nama)
        print("Kelas : ", self.kelas)
    
    def viewBiodata(self):
        print("Biodata")
        print("Nama : ", self.nama)
        print("Asal : ", self.asal)
        print("TTL  : ", self.lahir)
        print("Umur : ", self.umur)
 
#instansiasi objek
siswa1 = siswa("Finda", "XII MIPA 1", "1 September 2002", "Bandung", 19)
siswa2 = siswa("Umi", "XII MIPA 2", "14 Februari 2002 ", "Surabaya", 19)
siswa3 = siswa("Jaydan", "XII MIPA 5", "22 April 2003", "Bali", 18)
#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewBiodata()
print("Jumlah siswa : ", siswa.jumlah_siswa)
#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewBiodata()
print("Jumlah siswa : ", siswa.jumlah_siswa)
#pemanggil objek siswa 3
siswa3.viewSiswa()
siswa3.viewBiodata()
print("Jumlah Siswa : ", siswwa.jumlah_siswa)
