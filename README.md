# Salsabil Rinaldi's Quality Assurance Portfolio

> **Quality Assurance Engineer** dengan spesialisasi dalam **Manual Testing**, **Test Case Design (Equivalence Partitioning & Boundary Value Analysis)**, **Web Security Auditing**, **API/GraphQL Testing**, dan **Automation Testing (Selenium & Python)**. Penulis Pertama (*First Author*) artikel ilmiah terakreditasi nasional bidang pengujian perangkat lunak di **Journal of Informatics and Communications Technology (JICT)**.

---

##  Profil

Halo! Saya Salsabil Rinaldi, lulusan Teknologi Rekayasa Perangkat Lunak, Sekolah Vokasi IPB University. Sebagai seorang praktisi Quality Assurance, saya berfokus pada penjaminan mutu perangkat lunak end-to-end melalui siklus hidup pengujian terstruktur (Software Testing Life Cycle / STLC).

Saya berpengalaman merancang dokumen perencanaan pengujian (Test Plan / DUPL), matriks skenario uji mendalam (Equivalence Partitioning & Boundary Value Analysis), analisis kerentanan konfigurasi web (HTTP Security Headers & Injeksi SQL/XSS), hingga pengujian penerimaan pengguna (User Acceptance Testing / UAT).

| Kategori | Rincian Keahlian |
|---|---|
| **Metodologi Pengujian** | Black-Box Testing, Functional Testing, Regression Testing, Non-Functional (Performance & Security), Cross-Browser Testing, UAT |
| **Teknik Desain Test Case** | Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Decision Table, Error Guessing, RBAC Verification |
| **Artefak QA** | Dokumen Pengujian Perangkat Lunak (DUPL), Test Plan, High-Level Scenarios, Defect/Bug Reports, UAT Sign-off Sheets |
| **Keamanan & Audit Web** | Audit HTTP Headers (CSP, CORS Wildcard `*`, X-Frame-Options), Verifikasi Proteksi SQL Injection & Cross-Site Scripting (XSS) |
| **API Testing** | GraphQL (Hot Chocolate), REST API, Status Code & Payload Validation, Postman, Bearer JWT Auth |
| **Otomasi Pengujian** | Selenium WebDriver (Python), Pytest (Headless CI/CD Pipeline Mode) |
| **Tools & Kolaborasi** | Chrome DevTools, Postman, Git & GitHub, Google Sheets, VS Code, MySQL |

---

##  Proyek Unggulan & Pengalaman Nyata

### 1.  [Publikasi Jurnal Ilmiah JICT: Sistem Informasi TPQ Nurul Iman](./projects/tpq-nurul-iman/)
Penelitian pengujian fungsional sistem informasi manajemen lembaga pendidikan menggunakan kombinasi **Equivalence Partitioning (EP)** dan **Boundary Value Analysis (BVA)** yang dipublikasikan secara terbuka (*Open Access*).
- **Peran**: **Penulis Pertama (First Author)**
- **Institusi**: Teknologi Rekayasa Perangkat Lunak, Sekolah Vokasi IPB University
- **Jurnal**: *Journal of Informatics and Communications Technology (JICT)*, Vol. 7, No. 2, Hal. 083–096, Desember 2025. ISSN: 2686-1089. DOI: [10.52661](https://doi.org/10.52661)
- **Cakupan Pengujian (29 Test Cases)**:
  -  [01. Test Cases Fitur Login (Equivalence Partitioning)](./projects/tpq-nurul-iman/01-test-cases-login-ep.md) — 7 kasus uji login kredensial valid, invalid, email format `@`, dan validasi field kosong (100% Valid).
  -  [02. Test Cases Fitur Registrasi (Boundary Value Analysis)](./projects/tpq-nurul-iman/02-test-cases-register-bva.md) — 14 kasus uji batas ekstrem nama (=3, <3, =50, >50), password (=8, <8, =16, >16), konfirmasi sandi, dan simulasi server email (Menemukan 2 defek batas atas).
  -  [03. Test Cases Pendaftaran Santri Baru (Equivalence Partitioning)](./projects/tpq-nurul-iman/03-test-cases-pendaftaran-santri-ep.md) — 8 kasus uji data santri, integritas NIK 16 digit, validasi rentang usia kelahiran 2013–2020, dan sanitasi nomor telepon.
  -  [04. Analisis Evaluasi & Temuan Cacat (Defect Analysis)](./projects/tpq-nurul-iman/04-evaluasi-temuan-bug.md) — Evaluasi tingkat kelulusan 86% vs 14% anomali, serta rekomendasi perbaikan validasi batas karakter dan regex telepon seluler.

---

### 2.  [Pembuatan Learning Management System (LMS) untuk Tutoring Academy](./projects/lms-tutoring-academy/)
Aplikasi web *standalone* bimbingan belajar dengan arsitektur modern (React, ASP.NET Core, GraphQL Hot Chocolate, dan AI Eye Tracking ViT) yang di-deploy ke Vercel (`https://tutor-academy-alpha.vercel.app/`).
- **Peran**: QA Engineer / Lead Tester (Tim 14th Legion / Kelompok Finesawit)
- **Reviewer**: Dr. Sofiyanti Indriasari S.Kom., M.Kom. & Dr. Medhanita Dewi Renanti S.Kom., M.Kom.
- **Artefak Pengujian**:
  -  [01. Test Plan (DUPL v3.0)](./projects/lms-tutoring-academy/01-test-plan.md) — Rencana uji lengkap modul F-01 s.d F-13, entry/exit criteria, dan analisis risiko.
  -  [02. Test Scenarios](./projects/lms-tutoring-academy/02-test-scenarios.md) — 14 skenario uji tingkat tinggi (SC-001 s.d SC-014).
  -  [03. Functional Test Cases](./projects/lms-tutoring-academy/03-test-cases-functional.md) — 16 matriks kasus uji fungsional (TC-001 s.d TC-016).
  -  [04. Non-Functional Test Cases](./projects/lms-tutoring-academy/04-test-cases-non-functional.md) — Pengujian performa (<5s), otentikasi ketat, injeksi SQL/XSS, dan kompatibilitas 4 browser.
  -  [05. Detailed Equivalence Partitioning](./projects/lms-tutoring-academy/05-test-cases-equivalence-partitioning.md) — Kasus uji detail registrasi, hak akses, dan login dieksekusi langsung oleh Salsabil Rinaldi.
  -  [06. Bug Reports & Security Audit](./projects/lms-tutoring-academy/06-bug-reports.md) — Temuan cacat CSP Header, CORS Overly Permissive (*), dan Missing Anti-Clickjacking.
  -  [07. Regression Testing](./projects/lms-tutoring-academy/07-regression-testing.md) — Matriks pengujian regresi pasca perbaikan bug dan migrasi database.
  -  [08. User Acceptance Testing (UAT)](./projects/lms-tutoring-academy/08-user-acceptance-testing-uat.md) — Evaluasi 6 skenario proses bisnis bersama stakeholder.

---

### 3.  [Test Automation Suite (Selenium + Pytest)](./automation/)
Script pengujian otomatis untuk memvalidasi alur regresi smoke test pada antarmuka web secara *headless* (mendukung CI/CD Pipeline).
- File script: [`test_lms_tutoring.py`](./automation/test_lms_tutoring.py)
- Cakupan: Pengecekan elemen form registrasi, login multi-role, verifikasi SLA waktu muat halaman (< 5 detik), dan uji kekebalan form terhadap SQL Injection.

---

### 4.  [API & GraphQL Testing](./api-testing/)
Dokumentasi pengujian mutation dan query backend **ASP.NET Core** dengan **GraphQL (Hot Chocolate Server)**.
- File dokumentasi: [`graphql-api-test-cases.md`](./api-testing/graphql-api-test-cases.md)
- Cakupan: Mutasi registrasi siswa, autentikasi multi-role login JWT, dan otorisasi pembatasan konten modul berbayar.

---

## Struktur Direktori Repository

```
qa-portfolio/
│
├── 📄 README.md                                    # Profil utama & katalog portofolio
├── 📄 .gitignore                                   # Konfigurasi file pengabaian Git
│
├── 📂 projects/
│   ├── 📂 tpq-nurul-iman/                         # Proyek Publikasi JICT (Penulis Pertama: Salsabil Rinaldi)
│   │   ├── 📄 README.md                            # Sinopsis jurnal, metodologi STLC, & ringkasan hasil
│   │   ├── 🧾 01-test-cases-login-ep.md            # 7 kasus uji Login (Equivalence Partitioning)
│   │   ├── 🧾 02-test-cases-register-bva.md        # 14 kasus uji Registrasi (Boundary Value Analysis)
│   │   ├── 🧾 03-test-cases-pendaftaran-santri-ep.md # 8 kasus uji Pendaftaran Santri Baru (EP)
│   │   └── 🐛 04-evaluasi-temuan-bug.md            # Evaluasi 86% vs 14% & analisis detail cacat sistem
│   │
│   └── 📂 lms-tutoring-academy/                   # Proyek Sistem Pembelajaran (React, ASP.NET Core, GraphQL, AI ViT)
│       ├── 📋 01-test-plan.md                      # Rencana pengujian lengkap (DUPL v3.0)
│       ├── 🎯 02-test-scenarios.md                 # 14 skenario uji sistem (SC-001 - SC-014)
│       ├── 🧾 03-test-cases-functional.md          # 16 kasus uji fungsional (TC-001 - TC-016)
│       ├── 🛡️ 04-test-cases-non-functional.md      # Kasus uji performa, keamanan, & portabilitas
│       ├── 🔬 05-test-cases-equivalence-partitioning.md # Kasus uji rinci Equivalence Partitioning
│       ├── 🐛 06-bug-reports.md                    # Temuan cacat sistem & audit security header
│       ├── 🔁 07-regression-testing.md             # Matriks pengujian regresi pasca bug fix
│       └── 👥 08-user-acceptance-testing-uat.md    # Lembar pelaksanaan & pernyataan UAT
│
├── 📂 automation/                                  # Modul Otomasi Pengujian
│   ├── 📄 README.md                                # Petunjuk instalasi & eksekusi pytest
│   └── 🐍 test_lms_tutoring.py                     # Script otomatisasi Selenium WebDriver
│
├── 📂 api-testing/                                 # Pengujian Antarmuka API
│   └── 🔌 graphql-api-test-cases.md                # GraphQL & REST API test matrix
│
└── 📂 .github/ISSUE_TEMPLATE/                      # Template Pelaporan Bug Standar
    └── 🐛 bug-report-template.yml                  # GitHub Issue form untuk pelaporan cacat
```

---

## 🛠️ Perangkat & Teknologi (Tools & Badges)

<p align="left">
  <img src="https://img.shields.io/badge/Testing-Black%20Box%20%7C%20EP%20%7C%20BVA-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Publication-JICT%20Journal%20Dec%202025-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />
  <img src="https://img.shields.io/badge/Chrome_DevTools-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

---

## 📫 Kontak & Tautan Profesional

- **Nama**: Salsabil Rinaldi
- **NIM**: J0403231073
- **Institusi**: Sekolah Vokasi IPB University
- **Email Akademik**: `isabelrinaldi@apps.ipb.ac.id`
- **Email Pribadi**: `salsabilrinaldi@gmail.com`
- **LinkedIn**: [linkedin.com/in/salsabil-rinaldi](https://linkedin.com/in/salsabil-rinaldi)
- **GitHub**: [github.com/salsabilrinaldi](https://github.com/salsabilrinaldi)

---

*Portofolio ini disusun secara transparan menggunakan data pengujian empiris dari publikasi artikel ilmiah resmi Journal of Informatics and Communications Technology (JICT) dan Dokumen Pengujian Perangkat Lunak (DUPL).*
