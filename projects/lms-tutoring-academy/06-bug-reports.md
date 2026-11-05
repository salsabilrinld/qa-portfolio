# 🐛 Bug Reports & Security Audit Findings

Daftar temuan cacat sistem (*Defect Reports*) dan audit konfigurasi keamanan pada aplikasi **LMS Tutoring Academy** (`https://tutor-academy-alpha.vercel.app/`).

---

## Ringkasan Klasifikasi Bug

| Level Severity | Dampak Terhadap Sistem | Level Priority | Urgensi Tindakan |
|---|---|---|---|
| **Critical** | Sistem lumpuh total atau data pengguna mengalami kerusakan permanen | **Critical** | Harus segera diselesaikan sebelum tahapan rilis |
| **High** | Fitur utama terhenti dan tidak ada solusi alternatif (*workaround*) | **High** | Perlu diselesaikan dalam sprint pengembangan berjalan |
| **Medium** | Fitur sekunder berjalan namun konfigurasi keamanan belum memenuhi standar | **Medium** | Ditangani setelah penyelesaian isu tingkat tinggi |
| **Low** | Isu kosmetik, teks, atau ketergantungan skrip minor | **Low** | Ditinjau apabila sumber daya waktu tersedia |

---

## 1. BUG-001: Content Security Policy (CSP) Header Not Set

| Field | Keterangan |
|---|---|
| **Bug ID** | **BUG-001** |
| **Judul Bug** | Header Content Security Policy (CSP) Tidak Dikonfigurasi pada Web Server |
| **Modul** | Security / HTTP Response Headers |
| **Target URL** | `https://tutor-academy-alpha.vercel.app/` |
| **Severity** | **Medium** |
| **Priority** | **Medium** |
| **Status** | **Open** |
| **Assigned To** | Dev Security / DevOps Engineer |

### Langkah Reproduksi (Steps to Reproduce)
1. Buka terminal atau konsol cURL / Postman / DevTools Audit.
2. Kirim request HTTP GET ke endpoint hosting produksi: `https://tutor-academy-alpha.vercel.app/`.
3. Analisa seluruh parameter pada response header yang dikembalikan server.

```bash
curl -I https://tutor-academy-alpha.vercel.app/
```

### Expected vs Actual Result
- **Expected Result**: Respons HTTP menyertakan header `Content-Security-Policy` dengan direktif ketat (`default-src 'self'; script-src 'self' ...`) untuk mencegah serangan Cross-Site Scripting (XSS) dan injeksi data inline.
- **Actual Result**: Header `Content-Security-Policy` tidak ditemukan sama sekali pada respons server Vercel.

---

## 2. BUG-002: Cross-Domain Misconfiguration (CORS Overly Permissive)

| Field | Keterangan |
|---|---|
| **Bug ID** | **BUG-002** |
| **Judul Bug** | Konfigurasi CORS Terlalu Terbuka (*Wildcard Access*) |
| **Modul** | Security / API Configuration |
| **Target URL** | `https://tutor-academy-alpha.vercel.app/` |
| **Severity** | **Medium** |
| **Priority** | **Medium** |
| **Status** | **Open** |
| **Assigned To** | Dev Security / DevOps Engineer |

### Langkah Reproduksi (Steps to Reproduce)
1. Kirim HTTP request dengan menyertakan header origin arbitrer (`Origin: https://attacker-domain.com`).
2. Periksa baris respon header `Access-Control-Allow-Origin`.

### Expected vs Actual Result
- **Expected Result**: Header `Access-Control-Allow-Origin` dikonfigurasi secara ketat hanya mengizinkan *whitelisted domain* tepercaya aplikasi, atau ditiadakan jika tidak dibutuhkan.
- **Actual Result**: Terdeteksi konfigurasi wildcard `Access-Control-Allow-Origin: *` yang mengizinkan pembacaan respons oleh domain pihak ketiga tanpa autentikasi origin yang aman.

---

## 3. BUG-003: Missing Anti-Clickjacking Header (X-Frame-Options)

| Field | Keterangan |
|---|---|
| **Bug ID** | **BUG-003** |
| **Judul Bug** | Proteksi Anti-Clickjacking Tidak Aktif (Header X-Frame-Options Hilang) |
| **Modul** | Security / HTTP Headers |
| **Target URL** | `https://tutor-academy-alpha.vercel.app/` |
| **Severity** | **Medium** |
| **Priority** | **Medium** |
| **Status** | **Open** |
| **Assigned To** | Dev Security / DevOps Engineer |

### Langkah Reproduksi (Steps to Reproduce)
1. Akses halaman utama sistem LMS.
2. Lakukan inspeksi keamanan framing pada respons HTTP.
3. Coba muat halaman aplikasi di dalam tag HTML `<iframe>` pada domain eksternal.

### Expected vs Actual Result
- **Expected Result**: Server mengirimkan header `X-Frame-Options: DENY` atau `X-Frame-Options: SAMEORIGIN` (atau `frame-ancestors 'self'` pada CSP) untuk melindungi aplikasi dari eksploitasi pembajakan klik (*Clickjacking*).
- **Actual Result**: Aplikasi tidak menyertakan proteksi `X-Frame-Options` maupun pembatasan iframe, memungkinkan situs disematkan ke dalam framing halaman eksternal tanpa proteksi.

---

## 4. BUG-004: Cross-Domain JavaScript Source File Inclusion

| Field | Keterangan |
|---|---|
| **Bug ID** | **BUG-004** |
| **Judul Bug** | Pemanggilan Skrip Eksternal Pihak Ketiga Tanpa Subresource Integrity |
| **Modul** | Security / Third-Party Dependencies |
| **Target URL** | `https://tutor-academy-alpha.vercel.app/` |
| **Severity** | **Low** |
| **Priority** | **Low** |
| **Status** | **Open** |
| **Assigned To** | Frontend Developer |

### Langkah Reproduksi (Steps to Reproduce)
1. Buka *source code* (Ctrl+U) halaman utama frontend.
2. Telusuri elemen tag `<script>` eksternal yang di-inject ke dalam DOM.

### Expected vs Actual Result
- **Expected Result**: Seluruh file JavaScript dimuat dari domain internal terverifikasi atau menggunakan *Subresource Integrity (SRI)* jika memanggil CDN publik.
- **Actual Result**: Aplikasi memuat skrip eksternal secara asinkron dari domain luar: `https://mcp.figma.com/mcp/html-to-design/capture.js` yang tertinggal dari plugin prototyping desain.
