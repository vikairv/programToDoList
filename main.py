tasks = []

def show_menu():
    print("\n=== APLIKASI TO DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Keluar")

def tambah_tugas():
    nama = input("Nama tugas        : ")
    mapel = input("Mata pelajaran    : ")
    deadline = input("Deadline (tgl)    : ")

    tugas = {
        "nama": nama,
        "mapel": mapel,
        "deadline": deadline
    }

    tasks.append(tugas)
    print("✅ Tugas berhasil ditambahkan!")

def lihat_tugas():
    if not tasks:
        print("📭 Belum ada tugas.")
    else:
        print("\n📋 DAFTAR TUGAS:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['nama']} | {t['mapel']} | Deadline: {t['deadline']}")

while True:
    show_menu()
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        print("👋 Keluar dari aplikasi.")
        break
    else:
        print("❌ Pilihan tidak valid.")