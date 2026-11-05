# 🧾 Test Case: Form Registrasi — Teknik Boundary Value Analysis

| Field | Detail |
|---|---|
| **Nama Project** | ShopEasy E-Commerce Platform |
| **Modul** | Registrasi / Pendaftaran Akun Baru |
| **Teknik Testing** | Black Box — Boundary Value Analysis (BVA) |
| **Dibuat oleh** | [Nama Kamu] |
| **Tanggal** | 5 November 2026 |

---

## Deskripsi

Pengujian form registrasi menggunakan metode **Black Box Testing** dengan teknik **Boundary Value Analysis (BVA)**. Teknik ini menguji nilai-nilai pada batas minimum dan maksimum dari setiap input field.

---

## Batasan Input Field

### Field: Nama Lengkap
- **Minimum:** 3 karakter
- **Maksimum:** 50 karakter

### Field: Password
- **Minimum:** 8 karakter
- **Maksimum:** 20 karakter
- **Ketentuan:** Harus mengandung huruf besar, huruf kecil, angka, dan karakter spesial

### Field: Nomor Telepon
- **Minimum:** 10 digit
- **Maksimum:** 13 digit
- **Format:** Hanya angka, diawali 08

### Field: Umur
- **Minimum:** 17 tahun
- **Maksimum:** 60 tahun

---

## Tabel Test Case — Nama Lengkap (min: 3, max: 50)

| Test ID | Skenario Pengujian | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-REG-001 | Input nama dengan 2 karakter (di bawah batas minimum) | `Ab` | Muncul pesan error: *"Nama minimal 3 karakter"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-002 | Input nama dengan 3 karakter (tepat di batas minimum) | `Abi` | Sistem menerima input, registrasi berhasil | Sistem menerima input | ✅ Pass |
| TC-REG-003 | Input nama dengan 4 karakter (satu di atas minimum) | `Abid` | Sistem menerima input, registrasi berhasil | Sistem menerima input | ✅ Pass |
| TC-REG-004 | Input nama dengan 25 karakter (nilai tengah) | `Muhammad Salman Al Farisi` | Sistem menerima input, registrasi berhasil | Sistem menerima input | ✅ Pass |
| TC-REG-005 | Input nama dengan 49 karakter (satu di bawah maksimum) | 49 karakter huruf | Sistem menerima input, registrasi berhasil | Sistem menerima input | ✅ Pass |
| TC-REG-006 | Input nama dengan 50 karakter (tepat di batas maksimum) | 50 karakter huruf | Sistem menerima input, registrasi berhasil | Sistem menerima input | ✅ Pass |
| TC-REG-007 | Input nama dengan 51 karakter (di atas batas maksimum) | 51 karakter huruf | Muncul pesan error: *"Nama maksimal 50 karakter"* | Muncul pesan error sesuai | ✅ Pass |

---

## Tabel Test Case — Password (min: 8, max: 20)

| Test ID | Skenario Pengujian | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-REG-008 | Input password 7 karakter (di bawah minimum) | `Test@12` | Muncul pesan error: *"Password minimal 8 karakter"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-009 | Input password 8 karakter (tepat di batas minimum) | `Test@123` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-010 | Input password 9 karakter (satu di atas minimum) | `Test@1234` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-011 | Input password 20 karakter (tepat di batas maksimum) | `TestPassword@12345!` (20 char) | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-012 | Input password 21 karakter (di atas maksimum) | `TestPassword@123456!!` (21 char) | Muncul pesan error: *"Password maksimal 20 karakter"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-013 | Input password tanpa huruf besar | `test@1234` | Muncul pesan error: *"Password harus mengandung huruf besar"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-014 | Input password tanpa angka | `TestPassword@` | Muncul pesan error: *"Password harus mengandung angka"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-015 | Input password tanpa karakter spesial | `TestPass1234` | Muncul pesan error: *"Password harus mengandung karakter spesial"* | Muncul pesan error sesuai | ✅ Pass |

---

## Tabel Test Case — Nomor Telepon (min: 10, max: 13 digit)

| Test ID | Skenario Pengujian | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-REG-016 | Input nomor telepon 9 digit (di bawah minimum) | `081234567` | Muncul pesan error: *"Nomor telepon minimal 10 digit"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-017 | Input nomor telepon 10 digit (batas minimum) | `0812345678` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-018 | Input nomor telepon 13 digit (batas maksimum) | `0812345678901` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-019 | Input nomor telepon 14 digit (di atas maksimum) | `08123456789012` | Muncul pesan error: *"Nomor telepon maksimal 13 digit"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-020 | Input nomor telepon mengandung huruf | `08abc12345` | Muncul pesan error: *"Nomor telepon hanya boleh angka"* | Muncul pesan error sesuai | ✅ Pass |

---

## Tabel Test Case — Umur (min: 17, max: 60)

| Test ID | Skenario Pengujian | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-REG-021 | Input umur 16 tahun (di bawah minimum) | `16` | Muncul pesan error: *"Umur minimal 17 tahun"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-022 | Input umur 17 tahun (batas minimum) | `17` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-023 | Input umur 18 tahun (satu di atas minimum) | `18` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-024 | Input umur 30 tahun (nilai tengah) | `30` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-025 | Input umur 59 tahun (satu di bawah maksimum) | `59` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-026 | Input umur 60 tahun (batas maksimum) | `60` | Sistem menerima input | Sistem menerima input | ✅ Pass |
| TC-REG-027 | Input umur 61 tahun (di atas maksimum) | `61` | Muncul pesan error: *"Umur maksimal 60 tahun"* | Muncul pesan error sesuai | ✅ Pass |
| TC-REG-028 | Input umur dengan huruf | `dua puluh` | Muncul pesan error: *"Umur harus berupa angka"* | Muncul pesan error sesuai | ✅ Pass |

---

## Ringkasan Hasil

| Total Test Case | Pass | Fail | Blocked | Not Executed |
|---|---|---|---|---|
| 28 | 28 | 0 | 0 | 0 |

**Pass Rate: 100%**
