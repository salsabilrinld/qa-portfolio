# Test Automation Suite: LMS Tutoring Academy

## Tech Stack Otomasi

| Komponen | Spesifikasi |
|---|---|
| Bahasa Pemrograman | Python 3.10+ |
| Framework Pengujian | `pytest` (Test Runner & Fixtures) |
| Browser Automation | `selenium` (WebDriver v4+) |
| Opsi Eksekusi | Headless Chrome (Cocok untuk GitHub Actions / CI/CD Pipeline) |
| Target URL | `https://tutor-academy-alpha.vercel.app/` |

---

## Skenario yang Diotomatisasi

1. TC-AUTO-001 (Ref: TC-001): Validasi ketersediaan dan interaksi formulir registrasi siswa.
2. TC-AUTO-002 (Ref: TC-003): Otomasi alur login peran Admin (`admin@lms.com`).
3. TC-AUTO-003 (Ref: TC-004): Otomasi alur login peran Siswa (`siswa@lms.com`).
4. TC-AUTO-004 (Ref: TC-017): Pengecekan SLA waktu muat halaman (*Page Load Time* < 5 detik).
5. TC-AUTO-005 (Ref: TC-019): Uji ketahanan keamanan form terhadap injeksi SQL (`' OR '1'='1`).
6. TC-AUTO-006 (Ref: TC-020): Verifikasi konsistensi rendering layout pada resolusi desktop 1920x1080.

---

## Panduan Menjalankan Script

### 1. Persiapan Virtual Environment & Instalasi Dependensi
```bash
# Masuk ke folder automation
cd automation

# Buat virtual environment (opsional namun disarankan)
python -m venv venv
# Aktifkan (Windows):
venv\Scripts\activate

# Install dependensi
pip install selenium pytest
```

### 2. Eksekusi Pengujian
```bash
# Menjalankan seluruh test suite dengan output detail (verbose)
pytest test_lms_tutoring.py -v

# Menjalankan test dengan menampilkan log print (console output)
pytest test_lms_tutoring.py -v -s
```

### 3. Integrasi ke CI/CD (GitHub Actions)
Script ini telah dirancang menggunakan flag `--headless=new` sehingga dapat langsung dieksekusi di dalam runner Linux/Windows pada pipeline otomatisasi GitHub Actions tanpa memerlukan antarmuka grafis (GUI).
