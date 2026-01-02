from fpdf import FPDF
from datetime import datetime
import os

def buat_pdf_struk(daftar_pesanan, menu, total_bayar, item_counter):
    pdf = FPDF()
    pdf.add_page()
    
    # Atur margin
    pdf.set_margins(left=15, top=10, right=15)
    
    # Header
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 8, "WARUNG MAKAN KELOMPOK 2", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, "Jl. Raya Kelompok D2", ln=True, align='C')
    pdf.cell(0, 5, "Telp: 081234567889", ln=True, align='C')
    
    # Garis pemisah header
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(8)
    
    # Waktu
    pdf.set_font("Arial", size=10)
    waktu = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    pdf.cell(0, 6, f"Tanggal: {waktu}", ln=True)
    pdf.cell(0, 6, "=" * 23, ln=True)
    
    # Header tabel item
    pdf.set_font("Arial", style='B', size=10)
    pdf.cell(100, 8, "Item", border=0)
    pdf.cell(30, 8, "Jumlah", border=0, align='C')
    pdf.cell(40, 8, "Subtotal", border=0, align='R')
    pdf.ln()
    pdf.cell(0, 2, "-" * 143, ln=True)
    
    # Item pesanan
    pdf.set_font("Arial", size=10)
    for pesanan in daftar_pesanan:
        # Makanan
        if pesanan.get("makanan"):
            nama_item = pesanan["makanan"]
            jumlah = pesanan["jumlah_makan"]
            harga = menu["makanan"].get(pesanan["makanan"], 0)
            subtotal = harga * jumlah
            
            pdf.cell(100, 8, f"{nama_item[:40]}", border=0)
            pdf.cell(30, 8, f"x{jumlah}", border=0, align='C')
            pdf.cell(40, 8, f"Rp {subtotal:,}", border=0, align='R')
            pdf.ln()
        
        # Minuman
        if pesanan.get("minuman"):
            nama_item = pesanan["minuman"]
            jumlah = pesanan["jumlah_minum"]
            harga = menu["minuman"].get(pesanan["minuman"], 0)
            subtotal = harga * jumlah
            
            pdf.cell(100, 8, f"{nama_item[:40]}", border=0)
            pdf.cell(30, 8, f"x{jumlah}", border=0, align='C')
            pdf.cell(40, 8, f"Rp {subtotal:,}", border=0, align='R')
            pdf.ln()
    
    # Garis pemisah sebelum total
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(8)
    
    # Total dengan format yang lebih jelas
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(130, 10, "TOTAL", border=0)
    pdf.cell(40, 10, f"Rp {total_bayar:,}", border=0, align='R')
    pdf.ln(15)
    
    # Footer
    pdf.set_font("Arial", style='I', size=9)
    pdf.cell(0, 5, "Terima kasih atas kunjungan Anda", ln=True, align='C')
    pdf.cell(0, 5, "Silakan datang kembali", ln=True, align='C')
    
    # Simpan file
    os.makedirs("pdf", exist_ok=True)
    filename = f"pdf/struk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    
    return filename