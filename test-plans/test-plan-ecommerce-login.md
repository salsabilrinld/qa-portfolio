# 📋 Test Plan: Modul Login — ShopEasy E-Commerce

| Field | Detail |
|---|---|
| **Nama Project** | ShopEasy E-Commerce Platform |
| **Modul** | Autentikasi Pengguna (Login) |
| **Versi** | 1.0 |
| **Dibuat oleh** | [Nama Kamu] |
| **Tanggal** | 5 November 2026 |
| **Status** | Final |

---

## 1. Pendahuluan

Dokumen test plan ini berisi strategi pengujian untuk modul Login pada aplikasi web e-commerce ShopEasy. Modul login memungkinkan pengguna yang sudah terdaftar untuk masuk ke sistem menggunakan email dan password.

## 2. Tujuan Pengujian

- Memverifikasi bahwa pengguna terdaftar dapat login dengan kredensial yang valid
- Memverifikasi bahwa sistem menampilkan pesan error yang tepat untuk input yang tidak valid
- Memverifikasi fungsionalitas "Lupa Password"
- Memverifikasi fungsionalitas "Ingat Saya" (Remember Me)
- Memverifikasi keamanan sistem (percobaan login gagal berulang)

## 3. Ruang Lingkup (Scope)

### 3.1 Dalam Ruang Lingkup (In Scope)

| No | Fitur | Deskripsi |
|---|---|---|
| 1 | Login Email/Password | Login standar dengan kredensial terdaftar |
| 2 | Lupa Password | Reset password melalui link email |
| 3 | Ingat Saya | Checkbox untuk session yang persisten |
| 4 | Penguncian Akun | Kunci akun setelah 5x percobaan login gagal |
| 5 | Validasi Input | Format email, persyaratan password |
| 6 | Pesan Error | Tampilan error yang sesuai |

### 3.2 Di Luar Ruang Lingkup (Out of Scope)

- Modul registrasi / pendaftaran akun baru
- Two-factor authentication (direncanakan untuk v2.0)
- Login via Google / Facebook / Apple

## 4. Pendekatan Pengujian (Test Approach)

| Jenis Pengujian | Deskripsi |
|---|---|
| **Black Box Testing** | Menguji fungsionalitas tanpa melihat kode sumber |
| **Equivalence Partitioning** | Membagi input ke dalam kelas valid dan invalid |
| **Boundary Value Analysis** | Menguji nilai batas minimum dan maksimum input |
| **Negative Testing** | Menguji dengan input yang tidak valid |
| **Regression Testing** | Memastikan fitur lama tetap berfungsi setelah perubahan |

## 5. Lingkungan Pengujian (Test Environment)

| Komponen | Detail |
|---|---|
| **Sistem Operasi** | Windows 11, macOS |
| **Browser** | Chrome 120+, Firefox 121+, Edge 120+ |
| **Mobile** | Chrome (Android), Safari (iOS) |
| **URL Staging** | https://staging.shopeasy-demo.com |
| **Test Data** | Akun test yang sudah terdaftar di database staging |

## 6. Kriteria Masuk (Entry Criteria)

- [x] Pengembangan modul login sudah selesai
- [x] Kode sudah di-deploy ke environment staging
- [x] Data test (akun pengguna) sudah disiapkan
- [x] Environment test stabil dan bisa diakses
- [x] Dokumen requirement sudah di-review

## 7. Kriteria Keluar (Exit Criteria)

- [ ] Semua test case critical dan high-priority sudah dieksekusi
- [ ] Semua bug critical dan high-severity sudah diperbaiki dan diverifikasi ulang
- [ ] Pass rate test case ≥ 95%
- [ ] Tidak ada bug Severity 1 (Blocker) atau Severity 2 (Critical) yang masih terbuka
- [ ] Test summary report sudah disiapkan

## 8. Jadwal Pengujian

| Fase | Mulai | Selesai | PIC |
|---|---|---|---|
| Desain Test Case | 06 Nov 2026 | 08 Nov 2026 | [Nama Kamu] |
| Setup Environment | 08 Nov 2026 | 09 Nov 2026 | Tim DevOps |
| Eksekusi Test — Round 1 | 10 Nov 2026 | 13 Nov 2026 | [Nama Kamu] |
| Perbaikan Bug & Retest | 14 Nov 2026 | 15 Nov 2026 | Dev + QA |
| Regression Testing | 16 Nov 2026 | 17 Nov 2026 | [Nama Kamu] |
| Sign-off | 18 Nov 2026 | 18 Nov 2026 | QA Lead |

## 9. Risiko dan Mitigasi

| No | Risiko | Dampak | Probabilitas | Mitigasi |
|---|---|---|---|---|
| 1 | Environment staging tidak stabil | Tinggi | Sedang | Koordinasi dengan DevOps; siapkan backup environment |
| 2 | Requirement berubah di tengah testing | Tinggi | Rendah | Review requirement dengan BA sebelum desain test |
| 3 | Waktu testing terbatas | Sedang | Sedang | Prioritaskan test case critical; gunakan risk-based testing |

## 10. Deliverables

- [x] Test Plan (dokumen ini)
- [ ] Test Cases
- [ ] Bug Reports
- [ ] Test Execution Report
- [ ] Test Summary Report
