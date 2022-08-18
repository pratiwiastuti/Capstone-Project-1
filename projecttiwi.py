print("Nama    : Pratiwi Astuti")
print("Project : Academic Scores - Data Nilai Siswa")
print("***********************************************")
listSiswa = [{'NIS': '1297', 'Nama Lengkap': 'Abdul Yusuf', 'UTS' : 75, 'UAS': 80},
    {
        'NIS': '1310',
        'Nama Lengkap': 'Anita Amalia',
     #   'Nama Belakang': 'Salsabila',
        'UTS' : 75,
        'UAS' : 67
    },
    {
        'NIS': '1425',
        'Nama Lengkap': 'Bunga Ananda',
    #    'Nama Belakang': 'Ananda',
        'UTS' : 75,
        'UAS' : 80
    },
    {
        'NIS': '1733',
        'Nama Lengkap': 'Galih Gunadi',
    #    'Nama Belakang': 'Gunawan',
        'UTS' : 90,
        'UAS' : 90
    },
    {
        'NIS': '3780',
        'Nama Lengkap': 'Yolla Yulian',
    #    'Nama Belakang': 'Yuliana',
        'UTS' : 87,
        'UAS' : 57
    },
]
kkm_nilai = 70
UTS=[]
UAS=[]
cart = []
nomor=[]

# Menampilkan data nilai
def menampilkanDataNilaiSiswa() :
    print('Daftar Nilai Siswa\n')
    print("No \t NIS \t Nama Lengkap \t UTS \t UAS")
    print("="*45)
#    print('Index  \t NIS  \t Nama Lengkap  \t MTK\t| IPA')
    for i in range(len(listSiswa)) :
        print('{}\t {}\t {}  \t {}  \t {}'.format(i,listSiswa[i]['NIS'],listSiswa[i]['Nama Lengkap'],listSiswa[i]['UTS'],listSiswa[i]['UAS']))

# Menambahkan data siswa
def menambahSiswa() :
    namaSiswa = input('Masukkan Nama Lengkap : ')
    nomorInduk = input('Masukkan Nomor Induk : ')
    nilaiUts = int(input('Masukkan Nilai UTS : '))
    nilaiUas = int(input('Masukkan Nilai UAS : '))
    listSiswa.append({
        'NIS': nomorInduk,
        'Nama Lengkap': namaSiswa,
        'UTS': nilaiUts,
        'UAS': nilaiUas
    })
    menampilkanDataNilaiSiswa()

# Cek kelulusan
def cekKelulusan () :
    menampilkanDataNilaiSiswa()
    nilaiUts = int(input('Masukkan Nilai UTS : '))
    nilaiUas = int(input('Masukkan Nilai UAS : '))
    akhir = (nilaiUts*40/100)+(nilaiUas*60/100)
    print("Nilai Akhir : 40% nilai UTS + 60% nilai UAS")
 
    print("Nilai Akhir", ":", akhir)
    if akhir >= kkm_nilai:
        print("Selamat Anda LULUS")
    else :
        print("Anda TIDAK LULUS, harap hubungi wali kelas")

while True :
    pilihanMenu = input('''
        Data Nilai Siswa Kelas IX SMP Sandi

        List Menu :
        1. Menampilkan Nilai Siswa
        2. Menambahkan Data Siswa
        3. Cek Kelulusan
        4. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDataNilaiSiswa()
    elif(pilihanMenu == '2') :
        menambahSiswa()
    elif(pilihanMenu == '3') :
        cekKelulusan()
    elif(pilihanMenu == '4') :
        break