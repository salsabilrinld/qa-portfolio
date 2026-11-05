# Test Cases: Fitur Registrasi Akun
Dokumentasi spesifikasi dan hasil pengujian fungsional modul Registrasi Akun Sistem Informasi TPQ Nurul Iman menggunakan teknik Boundary Value Analysis (BVA). Teknik *Boundary Value Analysis (BVA)* diterapkan pada formulir registrasi akun karena field input mewajibkan batasan rentang (*range*) karakter tertentu, yang dikelompokkan ke dalam tiga kondisi batas:
- Batas Bawah: Nilai di batas minimum ($x$) dan satu nilai di bawah batas minimum ($x - 1$).
- Nilai Batas Valid: Berada tepat di batas rentang ($x$ dan $y$).
- Batas Atas: Nilai di batas maksimum ($y$) dan satu nilai di atas batas maksimum ($y + 1$).

---

## Tabel Pelaksanaan Uji Fitur Registrasi Akun

| Kode Skenario | Kode Hasil | Field yang Diuji | Kondisi Pengujian | Nilai Batas Uji (*Boundary Value*) | Hasil yang Diharapkan (*Expected Output*) | Hasil Pengujian Aktual (*Actual Output*) | Status Validasi |
|---|---|---|---|---|---|---|---|
| **B01** | **BP01** | Nama Lengkap | Panjang minimum valid | `= 3` karakter | Sistem menerima input dan registrasi diproses | Input diterima sistem |  **Valid (Pass)** |
| **B02** | **BP02** | Nama Lengkap | Di bawah panjang minimum | `< 3` karakter | Sistem menolak dan menampilkan pesan error: *"Nama minimal 3 karakter"* | Sistem menolak dan menampilkan pesan error: *"Nama minimal 3 karakter"* |  **Valid (Pass)** |
| **B03** | **BP03** | Nama Lengkap | Panjang maksimum valid | `= 50` karakter | Sistem menerima input dan registrasi diproses | Input diterima sistem |  **Valid (Pass)** |
| **B04** | **BP04** | Nama Lengkap | Melebihi panjang maksimum | `> 50` karakter | Sistem menolak dan menampilkan pesan error: *"Nama maksimal 50 karakter"* | Input tetap **Diterima** oleh sistem tanpa peringatan |  **Invalid (Fail)** |
| **B05** | **BP05** | Email | Format email valid | Mengandung simbol `@` | Sistem menerima input format email | Input diterima sistem |  **Valid (Pass)** |
| **B06** | **BP06** | Email | Format email tidak valid | Tanpa simbol `@` | Sistem menolak dan menampilkan pesan: *"Please include an '@' in the email address"* | Menampilkan pesan: *"Please include an '@' in the email address"* |  **Valid (Pass)** |
| **B07** | **BP07** | Password | Panjang minimum valid | `= 8` karakter | Sistem menerima input kata sandi | Input diterima sistem |  **Valid (Pass)** |
| **B08** | **BP08** | Password | Di bawah panjang minimum | `< 8` karakter | Sistem menolak dan menampilkan pesan error: *"Kata sandi minimal 8 karakter"* | Menampilkan pesan error: *"Kata sandi minimal 8 karakter"* |  **Valid (Pass)** |
| **B09** | **BP09** | Password | Panjang maksimum valid | `= 16` karakter | Sistem menerima input kata sandi | Input diterima sistem |  **Valid (Pass)** |
| **B10** | **BP10** | Password | Melebihi panjang maksimum | `> 16` karakter | Sistem menolak dan menampilkan pesan error: *"Kata sandi maksimal 16 karakter"* | Input tetap **Diterima** oleh sistem tanpa peringatan |  **Invalid (Fail)** |
| **B11** | **BP11** | Konfirmasi Password | Nilai cocok (*match*) dengan password | Pass: `"abc12345"`<br>Konfirmasi: `"abc12345"` | Sistem memvalidasi kesamaan password dan pendaftaran dilanjutkan | Input diterima sistem |  **Valid (Pass)** |
| **B12** | **BP12** | Konfirmasi Password | Nilai tidak cocok (*mismatch*) | Pass: `"abc12345"`<br>Konfirmasi: `"abc123"` | Sistem menolak dan menampilkan pesan error: *"Kata sandi tidak cocok"* | Menampilkan pesan error: *"Kata sandi tidak cocok"* |  **Valid (Pass)** |
| **B13** | **BP13** | Verifikasi Email | Server email aktif dan domain valid | Menggunakan akun email valid | Pengguna menerima email tautan aktivasi/verifikasi di kotak masuk Gmail | Pengguna menerima email verifikasi di Gmail |  **Valid (Pass)** |
| **B14** | **BP14** | Verifikasi Email | Server email gagal mengirim / down | Simulasi server down / salah domain | Sistem menangani kegagalan dengan menampilkan pesan: *"Gagal mengirim email verifikasi, coba lagi nanti"* | Menampilkan pesan: *"Gagal mengirim email verifikasi, coba lagi nanti"* | **Valid (Pass)** |

---

## Analisis Hasil Pengujian

- Total Test Case: 14 Kasus Uji
- Status Valid (Sesuai): 12 Kasus Uji (85.7%)
- Status Invalid (Cacat / Bug): 2 Kasus Uji (14.3%) — BP04 & BP10
- Temuan QA:
  - Validasi batas minimum (`minlength`) pada nama (3 char) dan password (8 char) telah bekerja dengan sempurna.
  - Namun, validasi batas atas (`maxlength`) pada sisi frontend dan backend masih belum diterapkan pada field Nama Lengkap (>50) dan Password (>16), sehingga masukan yang melebihi batas batas tetap dapat masuk ke sistem.
