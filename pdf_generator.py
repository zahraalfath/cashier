from fpdf import FPDF
from datetime import datetime
import os

def buat_pdf_struk(daftar_pesanan, menu, total_bayar, item_counter):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(0, 10, "WARUNG MAKAN KELOMPOK 2", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, "Jl. Raya Kelompok D2", ln=True, align='C')
    pdf.cell(0, 5, "Telp: 081234567889", ln=True, align='C')
    pdf.cell(0, 5, "=" * 22, ln=True)

    # Waktu
    waktu = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    pdf.set_font("Arial", size=9)
    pdf.cell(0, 5, f"Tanggal: {waktu}", ln=True)
    pdf.cell(0, 5, "-" * 50, ln=True)

    # Item
    pdf.set_font("Arial", size=10)
    for pesanan in daftar_pesanan:
        if pesanan["makanan"]:
            harga = menu["makanan"].get(pesanan["makanan"], 0)
            subtotal = harga * pesanan["jumlah_makan"]
            pdf.cell(0, 6, f"{pesanan['makanan']} x{pesanan['jumlah_makan']} = Rp {subtotal:,}", ln=True)

        if pesanan["minuman"]:
            harga = menu["minuman"].get(pesanan["minuman"], 0)
            subtotal = harga * pesanan["jumlah_minum"]
            pdf.cell(0, 6, f"{pesanan['minuman']} x{pesanan['jumlah_minum']} = Rp {subtotal:,}", ln=True)

    # Total
    pdf.cell(0, 5, "-" * 50, ln=True)
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, f"TOTAL: Rp {total_bayar:,}", ln=True)

    # Simpan
    os.makedirs("pdf", exist_ok=True)
    filename = f"pdf/struk_{datetime.now().strftime('%H%M%S')}.pdf"
    pdf.output(filename)

    return filename
