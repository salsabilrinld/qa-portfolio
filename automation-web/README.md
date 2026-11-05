# 🤖 Web Automation — Login Test (Selenium + Python)

Folder ini berisi script automation dasar menggunakan **Selenium WebDriver** dan **Python** untuk mengotomatiskan pengujian halaman login.

> **Catatan:** Script ini dibuat sebagai contoh untuk menunjukkan pemahaman dasar tentang test automation. Untuk project nyata, disarankan menggunakan framework seperti **pytest** dengan **Page Object Model (POM)**.

---

## Cara Menjalankan

### 1. Install dependencies

```bash
pip install selenium pytest
```

### 2. Download ChromeDriver

Download ChromeDriver yang sesuai dengan versi Chrome Anda dari:
https://chromedriver.chromium.org/downloads

### 3. Jalankan test

```bash
pytest test_login.py -v
```

---

## Struktur File

```
automation-web/
├── README.md           → Dokumentasi ini
└── test_login.py       → Script test automation login
```

---

## Test Scenarios yang Di-automate

| No | Skenario | Method |
|---|---|---|
| 1 | Login dengan kredensial valid | `test_login_valid_credentials` |
| 2 | Login dengan email kosong | `test_login_empty_email` |
| 3 | Login dengan password kosong | `test_login_empty_password` |
| 4 | Login dengan password salah | `test_login_wrong_password` |
| 5 | Validasi elemen halaman login | `test_login_page_elements` |
