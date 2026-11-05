# 🐛 Bug Report: BUG-002

| Field | Detail |
|---|---|
| **Bug ID** | BUG-002 |
| **Judul** | Form registrasi menerima format email yang tidak valid |
| **Project** | ShopEasy E-Commerce Platform |
| **Modul** | Registrasi |
| **Reporter** | [Nama Kamu] |
| **Tanggal Ditemukan** | 11 November 2026 |
| **Status** | Open |
| **Severity** | Major |
| **Priority** | Medium |
| **Assignee** | Frontend Developer |

---

## Deskripsi

Form registrasi menerima dan memproses email dengan format yang tidak valid. Pengguna bisa mendaftarkan akun baru dengan email `user@` (tanpa domain). Sistem seharusnya menolak email yang tidak memiliki domain name lengkap.

## Pre-condition

- Halaman registrasi dapat diakses
- Tidak ada akun dengan email `user@` yang sudah terdaftar

## Steps to Reproduce (Langkah Reproduksi)

| Step | Aksi |
|---|---|
| 1 | Buka browser Chrome versi 120 |
| 2 | Akses halaman registrasi: `https://staging.shopeasy-demo.com/register` |
| 3 | Masukkan nama: `Test User` |
| 4 | Masukkan email: `user@` |
| 5 | Masukkan password: `Test@1234` |
| 6 | Masukkan konfirmasi password: `Test@1234` |
| 7 | Klik tombol "Daftar" |

## Expected Result (Hasil yang Diharapkan)

Sistem menolak input dan menampilkan pesan validasi: *"Masukkan alamat email yang valid"*

## Actual Result (Hasil Aktual)

Sistem menerima email `user@` dan akun berhasil terdaftar. Pengguna diarahkan ke halaman verifikasi email.

## Screenshot

> *(Sertakan screenshot form registrasi yang berhasil dengan email invalid)*
>
> ![Register Bug Screenshot](placeholder-screenshot-register-bug.png)

## Environment

| Komponen | Detail |
|---|---|
| **OS** | Windows 11 |
| **Browser** | Chrome 120.0.6099.130 |
| **Environment** | Staging |
| **URL** | https://staging.shopeasy-demo.com/register |

## Analisa Tambahan

- Browser built-in validation tidak memvalidasi email `user@` sebagai invalid
- Validasi di backend juga tidak ada (API `/api/auth/register` return `201 Created`)
- Perlu ditambahkan validasi email yang ketat di frontend (regex) dan backend

## Severity & Priority Justification

- **Severity: Major** — Data email tidak valid masuk ke database; bisa menyebabkan error saat kirim email verifikasi
- **Priority: Medium** — Bukan blocker, tapi harus diperbaiki sebelum release ke production
