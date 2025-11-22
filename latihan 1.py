# latihan1_kontak.py
# Menyiapkan dictionary sesuai soal dan menjalankan operasi yang diminta

def latihan1():
    # buat dictionary awal
    contacts = {
        "bina": "081254782838",
        "Dipa": "085388826476"
    }

    print("Kontak awal:", contacts)
    print()

    # Tampilkan kontak bina
    print("Nomor bina:", contacts.get("Ari"))
    print()

    # Tambah kontak nina
    contacts["nina"] = "087654652544"
    print("Setelah tambah nina:", contacts)
    print()

    # Ubah kontak Dipa
    contacts["Dipa"] = "088999776"
    print("Setelah ubah nomor dipa:", contacts)
    print()

    # Tampilkan semua Nama
    print("Semua nama:", list(contacts.keys()))
    # Tampilkan semua Nomor
    print("Semua nomor:", list(contacts.values()))
    print()

    # Tampilkan daftar Nama dan nomornya (iterasi)
    print("Daftar nama dan nomor:")
    for name, number in contacts.items():
        print(f" - {name}: {number}")
    print()

    # Hapus kontak Dina
    if "Dipa" in contacts:
        del contacts["Dipa"]
        print("Setelah hapus Dipa:", contacts)
    else:
        print("Dipa tidak ditemukan untuk dihapus.")

if __name__ == "__main__":
    latihan1