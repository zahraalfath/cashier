from fpdf import FPDF
from datetime import datetime
import os

def buat_pdf_struk(daftar_pesanan, menu, total_bayar):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(15, 10, 15)

    def garis():
        y = pdf.get_y() + 2
        pdf.line(10, y, 200, y)
        pdf.ln(6)

    # HEADER
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "WARUNG MAKAN KELOMPOK 2", ln=True, align="C")
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, "Jl. Raya Kelompok D2", ln=True, align="C")
    pdf.cell(0, 5, "Telp: 081234567889", ln=True, align="C")
    garis()

    # WAKTU
    waktu = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    pdf.cell(0, 6, f"Tanggal: {waktu}", ln=True)
    pdf.cell(0, 6, "=" * 23, ln=True)

    # HEADER TABEL
    pdf.set_font("Arial", "B", 10)
    pdf.cell(100, 8, "Item")
    pdf.cell(30, 8, "Jumlah", align="C")
    pdf.cell(40, 8, "Subtotal", align="R")
    pdf.ln()
    pdf.cell(0, 2, "-" * 143, ln=True)

    # ISI ITEM
    pdf.set_font("Arial", size=10)
    for p in daftar_pesanan:
        for jenis, key_jml, key_menu in [
            ("makanan", "jumlah_makan", "makanan"),
            ("minuman", "jumlah_minum", "minuman")
        ]:
            if p.get(jenis):
                nama = p[jenis][:40]
                jumlah = p[key_jml]
                subtotal = menu[key_menu].get(p[jenis], 0) * jumlah
                pdf.cell(100, 8, nama)
                pdf.cell(30, 8, f"x{jumlah}", align="C")
                pdf.cell(40, 8, f"Rp {subtotal:,}", align="R")
                pdf.ln()

    garis()

    # TOTAL
    pdf.set_font("Arial", "B", 12)
    pdf.cell(130, 10, "TOTAL")
    pdf.cell(40, 10, f"Rp {total_bayar:,}", align="R")
    pdf.ln(12)

    # FOOTER
    pdf.set_font("Arial", "I", 9)
    pdf.cell(0, 5, "Terima kasih atas kunjungan Anda", ln=True, align="C")
    pdf.cell(0, 5, "Silakan datang kembali", ln=True, align="C")

    os.makedirs("pdf", exist_ok=True)
    file = f"pdf/struk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(file)
    return file