from menu import menu
from datetime import datetime
from pdf_generator import buat_pdf_struk

# ================= LOG FUNCTION =================
def log_rapi(daftar_pesanan, total_bayar, item_counter, nama_pdf=None):
    waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write("="*50 + "\n")
        f.write(" " * 10 + "WARUNG MAKAN KELOMPOK 2\n")
        f.write(f"Tanggal: {waktu}\n")
        f.write("="*50 + "\n")
        f.write("===== RINGKASAN TRANSAKSI =====\n")
        for p in daftar_pesanan:
            if p["makanan"]:
                f.write(f"Makanan : {p['makanan']} x {p['jumlah_makan']}\n")
            if p["minuman"]:
                f.write(f"Minuman : {p['minuman']} x {p['jumlah_minum']}\n")
        f.write("-"*50 + "\n")
        f.write(f"Total Item  : {item_counter}\n")
        f.write(f"Total Bayar : Rp {total_bayar:,.0f}\n")
        f.write("="*50 + "\n")
        if nama_pdf:
            f.write(f"PDF berhasil dibuat: {nama_pdf}\n")
            f.write("="*50 + "\n")
        # Tambahkan 2 baris kosong sebagai jarak antar transaksi
        f.write("\n\n")


# ================= TAMPIL MENU DI LAYAR =================
print("=" * 60)
print(f"{'MAKANAN':<20} | {'HARGA':<10} | {'MINUMAN':<15} | {'HARGA':<10}")
print("=" * 60)
for (makanan, harga_m), (minuman, harga_min) in zip(menu["makanan"].items(),
                                                    menu["minuman"].items()):
    print(f"{makanan:<20} | Rp {harga_m:<8} | {minuman:<15} | Rp {harga_min:<8}")
print("=" * 60)


# ================= INPUT PESANAN =================
daftar_pesanan = []
ulang = "y"

while ulang.lower() == "y":
    pesanan_makanan = input("Pilih Makanan (kosongkan jika tidak mau): ").strip()
    if pesanan_makanan:
        jumlah_makan = int(input("Jumlah Makanan : "))
    else:
        jumlah_makan = 0

    pesanan_minum = input("Pilih Minuman (kosongkan jika tidak mau): ").strip()
    if pesanan_minum:
        jumlah_minum = int(input("Jumlah Minuman : "))
    else:
        jumlah_minum = 0

    daftar_pesanan.append({
        "makanan": pesanan_makanan,
        "jumlah_makan": jumlah_makan,
        "minuman": pesanan_minum,
        "jumlah_minum": jumlah_minum
    })

    ulang = input("Tambah pesanan lagi? (y/n): ")


# ================= HITUNG TOTAL =================
total_bayar = 0
item_counter = 0

for pesanan in daftar_pesanan:
    if pesanan["makanan"]:
        harga = menu["makanan"].get(pesanan["makanan"], 0)
        total_bayar += harga * pesanan["jumlah_makan"]
        item_counter += 1
    if pesanan["minuman"]:
        harga = menu["minuman"].get(pesanan["minuman"], 0)
        total_bayar += harga * pesanan["jumlah_minum"]
        item_counter += 1


# ================= PDF (OPSIONAL) =================
BUAT_PDF = True  # ubah True jika ingin PDF

if BUAT_PDF:
    nama_file_pdf = buat_pdf_struk(
        daftar_pesanan,
        menu,
        total_bayar,
        item_counter
    )
else:
    nama_file_pdf = None


# ================= TULIS KE FILE.TXT =================
log_rapi(daftar_pesanan, total_bayar, item_counter, nama_file_pdf)

# ================= OUTPUT KE LAYAR =================
print("\n===== RINGKASAN TRANSAKSI =====")
for p in daftar_pesanan:
    if p["makanan"]:
        print(f"Makanan : {p['makanan']} x {p['jumlah_makan']}")
    if p["minuman"]:
        print(f"Minuman : {p['minuman']} x {p['jumlah_minum']}")
print(f"Total Item  : {item_counter}")
print(f"Total Bayar : Rp {total_bayar:,.0f}")


if nama_file_pdf:
    print(f"PDF berhasil dibuat: {nama_file_pdf}")
else:
    print("PDF tidak dibuat (mode TXT saja)")
