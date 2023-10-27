nama="sentosa"
mapel="matematika"
nilai=90

if(nilai >= 80 and nilai <= 100):
    grade="a"
elif(nilai >= 70 and nilai < 80):
    grade ="b"
elif(nilai >= 60 and nilai < 70):
    grade ="c"
elif(nilai >= 30 and nilai < 60):
    grade = "d"

print("nama siswa \t:" ,nama,
"\nmata_pelajaran \t:" ,mapel,
"\nnilai \t\t:",nilai,
"\nketerangan \t:",grade)