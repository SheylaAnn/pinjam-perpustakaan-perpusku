# CABSTONE 1 - PEMINJAMAN DAN PENGEMBALIAN BUKU

# ====== IMPORT FUNCTION AREA ======
from tabulate import tabulate
import textwrap
import datetime

# ========== LIST DATA =============
current_user = None # status user diawal dibuat none karna setelah def_login akan diganti dengan username yg diinput

data_login = {
    'admin': {'password': '1', 'role': 'admin'}, # akun admin tidak bisa dibuat manual
    'usertest': {'password': 'user123', 'role': 'user'}, # default user
    'sheyla': {'password': 'sheyla123', 'role': 'user'}, 
}

daftar_buku = { # pakai dictionary agar akses lebih cepat menggunakan key
    'ID001':{
        'ISBN':'978-602-03247-8-4', 
        'Judul': 'Hujan',
        'Penulis': 'Tere Liye',
        'Tahun': 2016,
        'Genre': 'Drama',
        'Bahasa': 'Indonesia',
        'Penerbit': 'Gramedia Pustaka Utama',
        'Stock': 5,
        },
    'ID002':{
        'ISBN':'978-623-95545-1-4', 
        'Judul': 'Pergi',
        'Penulis': 'Tere Liye',
        'Tahun': 2018,
        'Genre': 'Pertualangan',
        'Bahasa': 'Indonesia',
        'Penerbit': 'Sabak Grip',
        'Stock': 3,
        },
    'ID003':{
        'ISBN':'978-0-7475-3269-9', 
        'Judul': "Harry Potter and the Sorcerer's Stone",
        'Penulis': 'J. K. Rowling',
        'Tahun': 1997,
        'Genre': 'Fantasi',
        'Bahasa': 'Inggris',
        'Penerbit': 'Bloomsbury',
        'Stock': 2,
        },
    'ID004':{
        'ISBN':'978-0-4390-6486-6', 
        'Judul': 'Harry Potter and the Chamber of Secrets',
        'Penulis': 'J. K. Rowling',
        'Tahun': 1998,
        'Genre': 'Fantasi',
        'Bahasa': 'Inggris',
        'Penerbit': 'Bloomsbury',
        'Stock': 4,
        },
    'ID005':{
        'ISBN':'979-3062-79-7', 
        'Judul': 'Laskar Pelangi',
        'Penulis': 'Andrea Hirata',
        'Tahun': 2005,
        'Genre': 'Fiksi',
        'Bahasa': 'Indonesia',
        'Penerbit': 'Bentang Pustaka',
        'Stock': 7,
        },
}

daftar_pinjaman = {
    'ID001':[
        {'Username': 'sheyla',
         'Status': 'Dikembalikan', 
         'Tanggal Peminjaman': '2025-06-09',
         'Tanggal Pengembalian': '2025-06-16'
        },
        {'Username': 'sheyla', 
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-10',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
    ],
    'ID002': [
        {'Username': 'sheyla', 
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        }
    ],
    'ID003': [
        {'Username': 'admin', 
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-09',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'usertest',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
    ],
    'ID004': [
        {'Username': 'admin',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'usertest',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'sheyla',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
    ],
    'ID005': [
        {'Username': 'admin',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'usertest',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-11',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'sheyla',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-12',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'admin',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-13',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
        {'Username': 'admin',
         'Status': 'Dipinjam', 
         'Tanggal Peminjaman': '2025-06-16',
         'Tanggal Pengembalian': 'Belum dikembalikan'
        },
    ],
}

keranjang_peminjaman = []   # per user

isi_recycle_bin = [
{
        'Old ID': 'ID007',
        'Judul': 'Laut Bercerita',
        'Data': {
            'ISBN': '978-979-794-526-1',
            'Penulis': 'Leila S. Chudori',
            'Tahun': 2017,
            'Genre': 'Fiksi',
            'Bahasa': 'Indonesia',
            'Penerbit': 'Kepustakaan Populer Gramedia',
            'Stock': 4,
        }
    },
    {
        'Old ID': 'ID008',
        'Judul': 'Filosofi Teras',
        'Data': {
            'ISBN': '978-602-481-598-1',
            'Penulis': 'Henry Manampiring',
            'Tahun': 2018,
            'Genre': 'Nonfiksi',
            'Bahasa': 'Indonesia',
            'Penerbit': 'Kompas',
            'Stock': 1,
        }
    },
]

# ========== DEF FUNCTION ==========
# Shortcut pribadi
def gagal():
    print('Input tidak valid!\n')

def potong_text(text, width=25):
    # Agar teks di tabel tidak terlalu lebar tampilannya
    return '\n'.join(textwrap.wrap(text, width=width))

def hitung_dipinjam(id_buku):
    return sum(
        1 for riwayat in daftar_pinjaman.get(id_buku, [])
        if riwayat['Status'] == 'Dipinjam'
    )

def hitung_tersedia(id_buku):
    return daftar_buku[id_buku]['Stock'] - hitung_dipinjam(id_buku)

def generate_new_id():
    angka_tertinggi = 0
    for id_buku in daftar_buku.keys():
        try:
            angka = int(id_buku[2:])
            if angka > angka_tertinggi:
                angka_tertinggi = angka
        except:
            continue
    return f"ID{angka_tertinggi + 1:03d}"

# 1.1 Login
def login_akun():
    print('\n============= LOGIN AKUN PERPUSKU =============')
    global current_user # pakai variabel global untuk seluruh proses selanjutnya setelah login
    username = input('Username: ')
    password = input('Password: ')

    # Jika username & password cocok pada dict data login = akses berhasil
    if username in data_login and data_login[username]['password'] == password:
        print(f'\nSELAMAT DATANG DI PERPUSKU, {username.upper()}!')
        current_user = username # current_user di-overwrite
        return data_login[username]['role'] # diberikan role untuk jenis menu
    else:
        print('Username atau password salah!\n')
        return

# 1.2 Daftar Akun
def daftar_akun():
    print('\n============== DAFTAR AKUN BARU ===============')
    while (True):
        username = input('Buat username: ')
        if username in data_login:
            print('Username sudah terpakai.\n')

        # Jika belum ada maka bisa input password
        else:
            while(True):
                password = input('Buat password (minimal 6 karakter): ')
                # Kasih syarat pembuatan password
                if len(password) < 6:
                    print('Password harus berisi minimal 6 karakter!\n')
                else:
                    break
            
            while(True):
                konfirmasi_akun = input('\nApakah Anda yakin ingin membuat akun? (y/n): ').lower()
                if konfirmasi_akun == 'y':
                    data_login[username] = {    # Menambahkan data ke Dictionary
                        'password': password,
                        'role': 'user'         # Daftar akun hanya untuk user.
                    }
                    print('Akun berhasil dibuat!\n')
                    print('======================================\n')
                    print('Silakan login kembali\n')
                    return # Balik ke menu login
                elif konfirmasi_akun == 'n':
                    print('Pembuatan akun dibatalkan.\n')
                    return
                else:
                    gagal()

# 2.1 Masuk Menu Utama (Admin = Akses jumlah stock buku, log peminjaman per buku, tambah dan hapus data buku (belum bisa pengeditan))
def menu_admin():
    while(True):
        print(
        '\n================= MENU UTAMA ==================\n'
        '1. Daftar Buku\n'
        '2. Cari Buku\n'
        '3. Daftar Peminjaman\n'
        '4. Kelola Buku\n'
        '5. Recycle Bin\n'
        '6. Keluar\n'
        '==============================================='
        )
        pilih_menu_admin = input('Masukkan pilihan Anda (1-6): ')

        if pilih_menu_admin == '1':
            tabel_buku()
        elif pilih_menu_admin == '2':
            cari_buku()
        elif pilih_menu_admin == '3':
            lihat_daftar_peminjaman()
        elif pilih_menu_admin == '4':
            kelola_buku()
        elif pilih_menu_admin == '5':
            recycle_bin()
        elif pilih_menu_admin == '6':
            break
        else:
            gagal()

# 2.1 Masuk Menu Utama (User = Akses pinjam dan kembalikan buku, log peminjaman diri sendiri)
def menu_user():
    while(True):
        print(
        '\n================= MENU UTAMA ==================\n'
        '1. Daftar Buku\n'
        '2. Cari Buku\n'
        '3. Meminjam Buku\n'
        '4. Mengembalikan Buku\n'
        '5. Riwayat Peminjaman Buku\n'
        '6. Keluar\n'
        '==============================================='
        )

        pilih_menu_user = input('Masukkan pilihan Anda (1-6): ')
        if pilih_menu_user == '1':
            tabel_buku()
        elif pilih_menu_user == '2':
            cari_buku()
        elif pilih_menu_user == '3':
            intro_pinjam_buku()
        elif pilih_menu_user == '4':
            intro_kembali_buku()
        elif pilih_menu_user == '5':
            riwayat_pinjam_user()
        elif pilih_menu_user == '6':
            break
        else:
            gagal()

# 3. Lihat Daftar Buku
def tabel_buku():
    print('\n============= DAFTAR BUKU PERPUSKU ============')
    # daftar_buku berupa dict, ID buku tidak memiliki value tunggal jadi ga bisa jadi kolom
    # buat list baru buat tabulate
    list_tabel_buku = []   
    
    if not daftar_buku:
        print("Belum ada buku yang tersedia di perpustakaan.")
        input('Tekan enter untuk kembali\n')
        return
    # menghitung jumlah dipinjam dan tersedia
    
    for id_buku, value in daftar_buku.items():
        jumlah_dipinjam = hitung_dipinjam(id_buku)
        jumlah_tersedia = hitung_tersedia(id_buku)

        # data loop berdasarkan id ditulis ulang sebagai dict untuk dimasukkan ke list
        data_buku = {
            'ID': id_buku,   # Agar ID001 dapat masuk ke tabulate maka ditambah keyword dalam list baru
            'ISBN': potong_text(value['ISBN'], 18),
            'Judul': potong_text(value['Judul'], 10),
            'Penulis': potong_text(value['Penulis'], 12),
            'Tahun': str(value['Tahun']), # Jadi str biar tampilan di tabulate rapih
            'Genre': potong_text(value['Genre'], 12),
            'Bahasa': potong_text(value['Bahasa'], 12),
            'Penerbit': potong_text(value['Penerbit'], 15),
            'Tersedia': jumlah_tersedia,    # Bukan stock yang ditampilkan melainkan yang tersedia saat itu
        }

        # Khusus admin bisa melihat jumlah dipinjam dan seluruh stock
        if data_login[current_user]['role'] == 'admin':
            data_buku['Dipinjam'] = jumlah_dipinjam # Masukkan key baru ke list data_buku
            data_buku['Stock'] = value['Stock']

        # dict data buku dimasukkan ke list_tabel_buku
        list_tabel_buku.append(data_buku)
    print(tabulate(list_tabel_buku, headers='keys', tablefmt='fancy_grid'))
    input('Tekan enter untuk kembali\n')
    return

# 4. Mencari Informasi Buku Dengan Cepat
def cari_buku():
    while(True):
        print('\n================== CARI BUKU ==================')
        # Pencarian bisa dari any keyword
        buku_cari = input("\nMasukkan kata kunci pencarian (ID, Judul, Penulis, Genre, Bahasa, Tahun) atau ketik 'selesai' untuk kembali:  ").lower()

        if buku_cari.lower() == 'selesai':
            break

        # Hasil pencarian bisa lebih dari 1, maka tampung di list
        hasil_pencarian = []
        for id_buku, value in daftar_buku.items():
            semua_data = f"{id_buku} {value['Judul']} {value['Penulis']} {value['Genre']} {value['Bahasa']} {value['Tahun']}".lower()
            # digabung biar filternya tinggal disebut variabel aja (f-string)

            if buku_cari in semua_data:
                tersedia = hitung_tersedia(id_buku) # daftar buku tidak ada info tersedia, jadi harus ditambahkan manual
                jumlah_dipinjam = hitung_dipinjam(id_buku)

            # Masukkan ke dalam list hasil_pencarian
                data_buku = [
                    id_buku,
                    potong_text(value['ISBN'], 18),
                    potong_text(value['Judul'], 10),
                    potong_text(value['Penulis'], 12),
                    str(value['Tahun']), 
                    potong_text(value['Genre'], 12),
                    potong_text(value['Bahasa'], 12),
                    potong_text(value['Penerbit'], 15),
                    tersedia
                ]

                # Akses ekslusif untuk admin
                if data_login[current_user]['role'] == 'admin':
                    data_buku.append(jumlah_dipinjam)
                    data_buku.append(value['Stock'])
                
                hasil_pencarian.append(data_buku)

        if hasil_pencarian:
            # Karna da 2 role jadi buat dulu headersnya biar tabulate headers ga panjang
            headers_user = ['ID', 'ISBN', 'Judul', 'Penulis', 'Tahun', 'Genre', 'Bahasa', 'Penerbit', 'Tersedia']

            # Kalo admin ditambah 2 kolom lagi
            if data_login[current_user]['role'] == 'admin':
                headers_user += ['Dipinjam', 'Stock']

            print('\nHasil Pencarian Anda:')
            print(tabulate(
                hasil_pencarian,
                headers=headers_user,
                tablefmt='fancy_grid'
            ))
        
        else:
            print('Hasil pencarian tidak ditemukan.')
        input('Tekan enter untuk kembali\n')

# 5. Lihat Log Peminjaman Per Buku (Admin)
def lihat_daftar_peminjaman():
    # untuk melihat log peminjaman tiap buku
    print('\n======= DAFTAR PEMINJAMAN BUKU PERPUSKU =======')

    # Kalau daftar peminjaman kosong masih kosong
    if not daftar_pinjaman:
        print('Belum ada data peminjaman.\n')
        input('Tekan enter untuk kembali\n')
        return

    # Kalau daftar peminjaman ada isinya
    data_peminjaman = []
    # dibuat list karna mau dibuat tabulate, agar ID buku bisa jadi kolom

    # loop tiap ID di dict daftar_peminjaman
    for id_buku, value in daftar_pinjaman.items():
        judul = daftar_buku.get(id_buku, {}).get('Judul', 'Judul Tidak Diketahui')
        
        # loop lagi perdasarkan daftar
        for lihat_daftar in value:
            data_peminjaman.append([
                id_buku,
                judul,
                lihat_daftar.get('Username', ''),
                lihat_daftar.get('Status', ''),
                lihat_daftar.get('Tanggal Peminjaman', ''),
                lihat_daftar.get('Tanggal Pengembalian', '')
            ])
    print(tabulate(data_peminjaman, headers=['ID', 'Judul', 'Username', 'Status', 'Tanggal Peminjaman', 'Tanggal Pengembalian'], tablefmt='fancy_grid'))
    input('Tekan enter untuk kembali\n')

# 6.1 Menu Kelola Buku (Admin)
def kelola_buku():  # Update dan Delete
    while(True):
        # Admin bisa pilih menu untuk kelola buku
        print(
        '\n=============== KELOLA PERPUSKU ===============\n'
        '1. Tambahkan Buku\n'
        '2. Hapus Buku\n'
        '3. Keluar\n'
        '==============================================='
        )
        pilih_menu_kelola = input('Masukkan pilihan Anda (1/2/3): ')

        if pilih_menu_kelola == '1':
            tambah_buku()
        elif pilih_menu_kelola == '2':
            hapus_buku()
        elif pilih_menu_kelola == '3':
            break
        else:
            gagal()

# 6.2 Kelola Buku: Tambah (Admin)
def tambah_buku():
    print('\n================= TAMBAH BUKU =================')
    while(True): 
        print("Masukkan judul buku atau ketik 'selesai' untuk kembali ke menu kelola")

        # Admin input judul buku yang baru
        buku_baru = input('Judul buku yang ingin ditambahkan: ') # bisa ga selalu .title()
        if buku_baru.lower() == 'selesai':
                break
            
        # dicek terlebih dahulu apakah ada judul yang sama
        same = False
        for id_buku, value in daftar_buku.items(): # id_buku untuk melihat judul ke semua id
            if buku_baru.lower() == str(value['Judul']).lower(): # ditetapkan str apabila judul buku ternyata int
                same = True
            
                while(True):
                # Kalau sudah ada bisa pilih mau nambah stock dari buku yang sudah ada
                    konfirmasi_stock = input('Buku sudah ada. Ingin tambahkan stock buku? (y/n): ').lower()
                
                # Jika mau menambahkan stock, bisa input jumlah stock yang ditambahkan
                    if konfirmasi_stock == 'y':
                        tambah_stock_buku = int(input('Banyak stock buku yang ditambahkan: '))
                        daftar_buku[id_buku]['Stock'] += tambah_stock_buku
                        print('Stock buku telah ditambahkan!')
                        print('Berikut daftar buku terbaru:')
                        tabel_buku()
                        break

                # Jika tidak mau, kembali ke menu kelola
                    elif konfirmasi_stock == 'n':
                        print('Penambahan stock buku dibatalkan\n')
                        break

                    else:
                        gagal()
                    # selain y/n = invalid

        # Jika tidak ada judul buku yang sama, maka masukkan data-data untuk judul buku yang baru diinput
        if not same:
            new_id = generate_new_id()
            isbn = input("ISBN: ")
            penulis = input("Penulis: ") # Penulis bisa aja namanya ga selalu .title()
            tahun = int(input("Tahun Terbit (Angka): "))
            genre = input("Genre: ").title()
            bahasa = input("Bahasa: ").title()
            penerbit = input("Penerbit: ") # bisa juga namanya ga selalu .title()
            stok = int(input("Jumlah stok (Angka): "))

            # Tambahkan data ke dict daftar_buku
            daftar_buku[new_id] = {
                'ISBN': isbn,
                'Judul': buku_baru,
                'Penulis': penulis,
                'Tahun': tahun,
                'Genre': genre,
                'Bahasa': bahasa,
                'Penerbit': penerbit,
                'Stock': stok,
                'Dipinjam': 0
            }
            print(f"Buku berhasil ditambahkan ke perpustakaan.")
            print('Berikut daftar buku terbaru:')
            tabel_buku()

# 6.3 Kelola Buku: Hapus (Admin)
def hapus_buku():
    print('\n================= HAPUS BUKU ==================')
    while(True):
        # Admin memasukkan judul buku yang mau dihapus
        print("Masukkan judul buku atau ketik 'selesai' untuk kembali ke menu kelola")

        buku_hapus = input('Judul buku yang ingin dihapus: ')
        if buku_hapus.lower() == 'selesai':
            break

        same = False
        # looping vsemua value daftar_buku
        for id_buku, info in daftar_buku.items():
            # jika judul yang diinput sama dengan judul di daftar buku
            if buku_hapus.lower() == str(info['Judul']).lower():
                same = True
                print(
                '\n======================================================\n'
                f'Pilih data buku {buku_hapus} yang ingin dihapus:\n'
                '1. Stock Buku\n'
                '2. Seluruh data\n'
                '3. Keluar\n'
                '======================================================'
                )
                pilih_hapus = input('Masukkan pilihan (1/2/3): ')        
                
                
                # Jika mau hapus stock saja
                if pilih_hapus == '1':
                    stock_tersedia = daftar_buku[id_buku]['Stock']

                    stock_total = daftar_buku[id_buku]['Stock']
                    jumlah_dipinjam = hitung_dipinjam(id_buku)
                    maks_bisa_dihapus = stock_total - jumlah_dipinjam
                        
                    if maks_bisa_dihapus <= 0:
                        print(f"Semua stok sedang dipinjam. Tidak bisa dihapus.\n")
                        break

                    while(True):
                        # Jumlah stock yang mau dihapus
                        hapus_stock_buku = int(input(f'Banyak stock buku yang dihapus (maks {maks_bisa_dihapus}): '))
                        # stock yang mau dihapus tidak mungkin melebihi stock buku
                        if hapus_stock_buku > maks_bisa_dihapus:
                            print('Jumlah yang dimasukkan melebihi stok.\n')
                        # stock yang mau dihapus tidak mungkin juga negatif atau 0
                        elif hapus_stock_buku <= 0:
                            print('Jumlah stock yang dihapus harus lebih dari 0!\n')
                        else:
                            break # selain itu maka lanjutkan ke konfirmasi

                    while(True):
                        kon_hapus_stock = input(f'Apa Anda yakin untuk menghapus stock buku {buku_hapus}? (y/n):  ')
                        if kon_hapus_stock.lower() == 'y':
                            # Jika iya, maka stock berkurang sejumlah penghapusan stock yang diinput
                            daftar_buku[id_buku]['Stock'] -= hapus_stock_buku
                            print('Stock buku telah dikurangi!')
                            print('Berikut daftar buku terbaru:')
                            tabel_buku()
                            break
                        elif kon_hapus_stock == 'n':
                            print('Pengurangan stock buku dibatalkan\n')
                            break
                        else:
                            gagal()

                    # Jika mau menghapus semua data buku
                elif pilih_hapus == '2':
                    while(True):
                        # langsung konfirmasi saja
                        kon_hapus_data = input(f'Apa Anda yakin untuk menghapus stock buku {buku_hapus}? (y/n):  ')
                        if kon_hapus_data.lower() == 'y':
                            # data masuk ke recycle_bin, agar data yang dihapus masih bisa di restore
                            data_dihapus = {
                                'Old ID': id_buku,
                                'Judul': daftar_buku[id_buku]['Judul'],
                                'Data': daftar_buku[id_buku].copy()  # copy biar ga ikut berubah
                            }
                                
                            isi_recycle_bin.append(data_dihapus)

                            del daftar_buku[id_buku]
                            print(f"Buku '{info['Judul']}' berhasil dihapus.")
                            print('Berikut daftar buku terbaru:')
                            tabel_buku()
                            break
                        elif kon_hapus_data.lower() == 'n':
                            print('Menghapus data buku dibatalkan\n')
                            break
                        else:
                            gagal()
                    break
                    
                # selain input 1 & 2
                elif pilih_hapus == '3':
                    break
                else:
                    gagal()
                    pilih_hapus = input('Masukkan pilihan (1/2): ')
        
        if not same:
            print('Buku tidak ditemukan dalam daftar.\n')

# 7.1 Menu Peminjaman Buku (User)
def intro_pinjam_buku():
    print('\n=============== PEMINJAMAN BUKU ===============')
    while(True):
        # Menawarkan user untuk melihat daftar buku yang tersedia, karna sistem returnnya pakai ID buku
        lihat_tabel = input('Ingin melihat daftar buku terlebih dahulu? (y/n/selesai): ')
        # untuk kembali ke menu utama
        if lihat_tabel == 'selesai':
            break

        # Jika iya maka tabel ditampilan, setelahnya masukkan ID buku (Jika data banyak kurang efektif)
        elif lihat_tabel == 'y':
            tabel_buku()
            id_buku_pinjam = input("Masukkan ID buku yang ingin dipinjam atau ketik 'selesai' untuk kembali ke menu: ").upper()
            
            if id_buku_pinjam.lower() == 'selesai':
                # Kembali ke menu utama
                break
            else:
                pinjam_buku(id_buku_pinjam) # masuk ke def pinjam buku (biar ga pengulangan)

        elif lihat_tabel == 'n':
            id_buku_pinjam = input("Masukkan ID buku yang ingin dipinjam atau ketik 'selesai' untuk kembali ke menu: ").upper()
                
            if id_buku_pinjam.lower() == 'selesai':
                # Kembali ke menu utama
                break
            else:
                pinjam_buku(id_buku_pinjam)
        
        else:
            gagal()

# 7.2 Peminjaman Buku (User)
def pinjam_buku(id_buku_pinjam):
    global keranjang_peminjaman
    
    # cek id buku yang ingin dipinjam ada di dalam dict daftar_buku apa tidak
    # Jika tidak ada maka ID buku tidak ditemukan
    # Jika ada proses ke cek stock
    if id_buku_pinjam not in daftar_buku:
        print('ID buku tidak ditemukan.\n')
        return
    
    buku_pinjam = daftar_buku[id_buku_pinjam]

    # Jika tersedia 0
    if hitung_tersedia(id_buku_pinjam) <= 0:
        print(f"Stok yang tersedia untuk buku '{buku_pinjam['Judul']}' sedang kosong.\n")
        return
        
    # Jika tersedia lebih dari 0

    keranjang_peminjaman.append(id_buku_pinjam)
    print(f"Buku {buku_pinjam['Judul']} ditambahkan ke keranjang peminjaman")
                
    # Konfirmasi peminjaman
    # User dikasih lihat rincian yang ingin dipinjam (ID & Judul)
    if keranjang_peminjaman:
        print('\n========= Konfirmasi Peminjaman =========')
        for id_buku in keranjang_peminjaman:
            print(f"{id_buku}: {daftar_buku[id_buku]['Judul']}")
            
            while (True):
                # user konfirmasi
                konfirmasi_pinjam = input('Proses peminjaman? (y/n): ')

                if konfirmasi_pinjam == 'y':
                    waktu_sekarang = datetime.datetime.now().strftime('%Y-%m-%d')

                    for id_buku_pinjam in keranjang_peminjaman:
                        # karna buku dipinjam maka logikanya tidak ada daftar pinjaman
                        # masukan data peminjam ke daftar pinjaman
                        if id_buku_pinjam not in daftar_pinjaman:
                            daftar_pinjaman[id_buku_pinjam] = []
                        
                        daftar_pinjaman[id_buku_pinjam].append({
                            'Username': current_user,
                            'Status': 'Dipinjam',
                            'Tanggal Peminjaman': waktu_sekarang,
                            'Tanggal Pengembalian': 'Belum dikembalikan'
                        })

                    # Setelah berhasil dipinjam, keranjang_peminjaman dikosongkan
                    print('Peminjaman berhasil!\n')
                    keranjang_peminjaman = []
                    return

                elif konfirmasi_pinjam == 'n':
                    print('Peminjaman dibatalkan\n')
                    keranjang_peminjaman = []
                    return

                else:
                    gagal()

# 8.1 Menu Pengembalian Buku (User)
def intro_kembali_buku():
    print('\n============== PENGEMBALIAN BUKU ==============')
    while(True):
        lihat_tabel = input('Ingin melihat daftar peminjaman Anda? (y/n/selesai): ')
        if lihat_tabel == 'selesai':
            break

        elif lihat_tabel == 'y':
            riwayat_pinjam_user()
            id_buku_kembali = input("Masukkan ID buku yang ingin dikembalikan atau ketik 'selesai' untuk kembali ke menu: ").upper()
            
            if id_buku_kembali.lower() == 'selesai':
                break # Kembali ke menu utama
            else:
                kembali_buku(id_buku_kembali)

        elif lihat_tabel == 'n':
            id_buku_kembali = input("Masukkan ID buku yang ingin dikembalikan atau ketik 'selesai' untuk kembali ke menu: ").upper()
                
            if id_buku_kembali.lower() == 'selesai':
                break # Kembali ke menu utama
            else:
                kembali_buku(id_buku_kembali)
        
        else:
            gagal()

# 8.1 Pengembalian Buku (User)
def kembali_buku(id_buku_kembali):
    global daftar_pinjaman
    # di cek dari daftar pinjaman
    # daftar pinjaman tercatat log peminjaman per buku bukan per user
    # filter terlebih dahulu yang milik user

    pinjaman_user = [
        riwayat # jelaskan dahulu apa yang mau dicari
        for riwayat in daftar_pinjaman.get(id_buku_kembali, [])
        if riwayat['Username'] == current_user and riwayat['Status'] == 'Dipinjam'
    ]

    if not pinjaman_user:
        print('ID buku tidak valid atau tidak sedang Anda pinjam\n')
        return

    # cek berapa banyak yang dipinjam
    total_dipinjam = sum(riwayat.get('jumlah', 1) for riwayat in pinjaman_user)
    print(f"Kamu meminjam total {total_dipinjam} eksemplar buku '{daftar_buku[id_buku_kembali]['Judul']}'.")

    while(True):
        # masih dalam str, kalo langsung int() bisa error ketika user tidak sengaja memasukkan str()
        jumlah_kembali_str = input('Masukkan jumlah buku yang ingin dikembalikan: ')
        if not jumlah_kembali_str.isdigit():
            print('Input harus berupa angka.\n')
            continue

        # Jika sudah benar dalam angka, ganti tipe data jumlah input user ke int()
        # cek jumlah pengembalian lebih dari total diminjam atau tidak
        jumlah_kembali = int(jumlah_kembali_str)
        if jumlah_kembali <= 0:
            print('Jumlah tidak boleh nol atau negatif.\n')
        elif jumlah_kembali > total_dipinjam:
            print('Jumlah pengembalian melebihi jumlah yang Anda pinjam.\n')
        else:
            break
    
    # jika sudah sesuai lakukan konfirmasi
    while(True):
        konfirmasi = input(f"Yakin ingin mengembalikan {jumlah_kembali} buku ini? (y/n): ").lower()
        if konfirmasi == 'n':
            print("Pengembalian dibatalkan.\n")
            return
        elif konfirmasi != 'y':
            gagal()
            continue
        else:
            break

    # jika dikembalikan bertahap, maka jumlah yang dipinjam berkurang dan masih tersisa

    tanggal_kembali = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for riwayat in range(jumlah_kembali):
        pinjaman_user[riwayat]['Status'] = 'Dikembalikan'
        pinjaman_user[riwayat]['Tanggal Pengembalian'] = tanggal_kembali
    
    # Tidak ada counter karna def hitung_dipinjam pakai looping status
    print("Pengembalian berhasil.\n")

# 9. Riwayat User
def riwayat_pinjam_user():
    riwayat_user = []
    for id_buku, info_riwayat in daftar_pinjaman.items():
        for riwayat in info_riwayat:
            if riwayat['Username'] == current_user and id_buku in daftar_buku:
                judul = daftar_buku[id_buku]['Judul']
                riwayat_user.append({
                    'ID Buku': id_buku,
                    'Judul': judul,
                    'Status': riwayat['Status'],
                    'Tanggal Peminjaman': riwayat['Tanggal Peminjaman'],
                    'Tanggal Pengembalian': riwayat['Tanggal Pengembalian']
                })
    print('\n=========== Riwayat Peminjaman Anda ===========')
    
    if riwayat_user:
        print(tabulate(riwayat_user, headers='keys', tablefmt='fancy_grid'))
    else:
        print('Belum ada riwayat peminjaman.')
    input('Tekan enter untuk kembali\n')

# 10. Recycle_bin (Admin) # Restore Data 
def recycle_bin():
    global isi_recycle_bin
    while(True):
        print('=========== Recycle Bin ===========')
        if not isi_recycle_bin:
            print('Recycle Bin kosong.')
            return
        
        data_yg_direstore = []
        for idx, item in enumerate(isi_recycle_bin, start=1):
            data_yg_direstore.append([
                idx,
                item['Old ID'],
                item['Judul'],
                item['Data']['Penulis'],
                item['Data']['Tahun']
            ])

        print(tabulate(data_yg_direstore, headers=['No', 'Old ID', 'Judul', 'Penulis', 'Tahun'], tablefmt='fancy_grid'))
        
        print(
            '\nPilih Menu Recycle Bin'
            '\n1. Pulihkan Buku'
            '\n2. Hapus Permanen'
            '\n3. Kembali\n'
            )
        pilihan_menu_hapus = input('Pilih menu (1/2/3): ')

        if pilihan_menu_hapus == '1':
            nomor_restore = input('Masukkan nomor buku yang ingin dipulihkan: ')
            found = None
            if nomor_restore.isdigit():
                nomor_restore = int(nomor_restore)
                if 1 <= nomor_restore <= len(isi_recycle_bin):
                    found = isi_recycle_bin[nomor_restore - 1]

                    konfirmasi = input(f"Yakin ingin memulihkan buku '{found['Judul']}'? (y/n): ").lower()
                    if konfirmasi == 'y':
                        # Pastikan ID tidak konflik
                        old_id = found['Old ID']
                        if old_id not in daftar_buku:
                            new_id = old_id
                        else:
                            new_id = generate_new_id()

                        data_restore = found['Data'].copy()
                        data_restore['Judul'] = found['Judul']  # tambahkan judul yang sempat dipisah

                        daftar_buku[new_id] = data_restore
                        isi_recycle_bin.remove(found)
                        print(f"Buku '{found['Judul']}' berhasil dipulihkan dengan ID baru: {new_id}\n")
                    
                    elif konfirmasi == 'n':
                        print('Pemulihan dibatalkan\n')
                    
                    else:
                        gagal()
                else:
                    print("Nomor tidak ditemukan di recycle bin\n")
            else:
                gagal()

        elif pilihan_menu_hapus == '2':
            nomor_hapus = input('Masukkan nomor buku yang ingin dihapus permanen: ')
            if nomor_hapus.isdigit():
                nomor_hapus = int(nomor_hapus)
                if 1 <= nomor_hapus <= len(isi_recycle_bin):
                    item = isi_recycle_bin[nomor_hapus - 1]
                    konfirmasi = input(f"Yakin ingin menghapus permanen buku '{item['Judul']}'? (y/n): ").lower()
                    if konfirmasi == 'y':
                        isi_recycle_bin.pop(nomor_hapus - 1)
                        print(f"Buku '{item['Judul']}' berhasil dihapus permanen\n")

                    elif konfirmasi == 'n':
                        print('Pemulihan dibatalkan\n')

                    else:
                        gagal()
                else:
                    print("Nomor tidak ditemukan di recycle bin\n")
            else:
                gagal()

        elif pilihan_menu_hapus == '3':
            return
        else:
            gagal()

# ========== PROGRAM UTAMA ==========
while(True):
    print(
    '\n========= LOGIN ATAU DAFTAR PERPUSKU ==========\n'
    '1. Login\n'
    '2. Daftar Akun\n'
    '3. Exit\n'
    '==============================================='
    )
    pilih_menu_login = input('Pilih menu (1/2/3): ')

    if pilih_menu_login == '1':
        role = login_akun()
        if role == 'admin':
            menu_admin() 
        elif role == 'user':
            menu_user() 
    elif pilih_menu_login == '2':
        daftar_akun()
    elif pilih_menu_login == '3':
        print('\nSelamat Tinggal!')
        break
    else:
        gagal() # Input tidak valid