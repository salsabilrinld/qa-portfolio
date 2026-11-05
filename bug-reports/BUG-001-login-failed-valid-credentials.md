# 🐛 Bug Report: BUG-001

| Field | Detail |
|---|---|
| **Bug ID** | BUG-001 |
| **Judul** | Login gagal meskipun menggunakan email dan password yang valid |
| **Project** | ShopEasy E-Commerce Platform |
| **Modul** | Login |
| **Reporter** | [Nama Kamu] |
| **Tanggal Ditemukan** | 10 November 2026 |
| **Status** | Open |
| **Severity** | Critical |
| **Priority** | High |
| **Assignee** | Backend Developer |

---

## Deskripsi

Pengguna tidak dapat login menggunakan email dan password yang valid dan terdaftar. Setelah menekan tombol "Masuk", sistem menampilkan pesan error *"Email atau password salah"* padahal kredensial sudah benar. Bug ini terjadi secara konsisten.

## Pre-condition

- Akun `user@shopeasy.com` sudah terdaftar di database staging
- Password: `Test@1234` sudah terverifikasi benar di database

## Steps to Reproduce (Langkah Reproduksi)

| Step | Aksi |
|---|---|
| 1 | Buka browser Chrome versi 120 |
| 2 | Akses halaman login: `https://staging.shopeasy-demo.com/login` |
| 3 | Masukkan email: `user@shopeasy.com` |
| 4 | Masukkan password: `Test@1234` |
| 5 | Klik tombol "Masuk" |

## Expected Result (Hasil yang Diharapkan)

Pengguna berhasil login dan diarahkan ke halaman Dashboard.

## Actual Result (Hasil Aktual)

Muncul pesan error berwarna merah: *"Email atau password salah"*. Pengguna tetap berada di halaman login.

## Screenshot

> *(Sertakan screenshot pesan error di sini)*
>
> ![Login Error Screenshot](placeholder-screenshot-login-error.png)

## Environment

| Komponen | Detail |
|---|---|
| **OS** | Windows 11 |
| **Browser** | Chrome 120.0.6099.130 |
| **Environment** | Staging |
| **URL** | https://staging.shopeasy-demo.com/login |

## Analisa Tambahan

- Diperiksa di Chrome DevTools → Tab Network: API `/api/auth/login` mengembalikan status `500 Internal Server Error`
- Response body: `{"error": "database connection timeout"}`
- Kemungkinan penyebab: koneksi database pada server staging bermasalah

## Severity & Priority Justification

- **Severity: Critical** — Pengguna sama sekali tidak bisa login ke aplikasi
- **Priority: High** — Fitur login adalah core feature; harus segera diperbaiki
