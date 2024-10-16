# INPUT PENGGUNA
print ("PENILAIAN KELULUSAN MAHASISWA")
nama = input("Masukan Nama : ")
nim = int(input("masukan nim : "))
alamat = input("Masukan Alamat : ")
nilai_kehadiran = float (input("Masukan Nilai kehadiran :"))
nilai_tugas = float(input("Masukan Nilai Tugas :"))
nilai_uts = float(input("Masukan Nilai UTS :"))
nilai_uas = float(input("Masukan Nilai UAS :"))
#MENGHITUNG BOBOT NILAI

bobot_kehadiran = 10
bobot_tugas = 20
bobot_uts = 30
bobot_uas = 40
# MENGHITUNG TOTAL BOBOT 

total_bobot = bobot_tugas + bobot_kehadiran + bobot_uts + bobot_uas 


# MENGITUNG NILAI AKHIR

nilai_akhir = (nilai_tugas * bobot_tugas / total_bobot) + (nilai_kehadiran * bobot_kehadiran / total_bobot) + (nilai_uts * bobot_uts / total_bobot) + (nilai_uas * bobot_uas / total_bobot)

print(f'hasil akhir : {nilai_akhir}')


#output status mahasiswa

if  nilai_akhir >= 80:
    hasil = "status : lulus"
else :
    hasil = "status : tidak lulus"
    
print ("_" * 50)
print ("-" * 50)
print (f'Nama Mahasiswa : {nama}')
print (f'NIM            : {nim}')
print (f'Alamat         : {alamat}')
print (f'Nilai akhir    : {nilai_akhir}')
print (f'{hasil}')