# 🔌 API Test Cases: User Endpoint

| Field | Detail |
|---|---|
| **Nama Project** | ShopEasy E-Commerce Platform |
| **Base URL** | `https://staging.shopeasy-demo.com/api` |
| **Tool** | Postman |
| **Dibuat oleh** | [Nama Kamu] |
| **Tanggal** | 5 November 2026 |

---

## Deskripsi

Pengujian REST API untuk endpoint user authentication pada aplikasi ShopEasy. Pengujian dilakukan menggunakan **Postman** untuk memvalidasi response status code, response body, dan error handling.

---

## 1. API: POST /api/auth/login

### Endpoint Detail

| Field | Detail |
|---|---|
| **Method** | POST |
| **URL** | `/api/auth/login` |
| **Content-Type** | application/json |
| **Auth** | Tidak perlu (public endpoint) |

### Request Body Format

```json
{
  "email": "string",
  "password": "string"
}
```

### Test Cases

| Test ID | Skenario | Request Body | Expected Status Code | Expected Response | Actual Result | Status |
|---|---|---|---|---|---|---|
| API-LGN-001 | Login dengan kredensial valid | `{"email": "user@shopeasy.com", "password": "Test@1234"}` | `200 OK` | `{"success": true, "token": "<jwt_token>", "user": {"id": 1, "email": "user@shopeasy.com"}}` | Sesuai | ✅ Pass |
| API-LGN-002 | Login dengan email tidak terdaftar | `{"email": "notfound@email.com", "password": "Test@1234"}` | `401 Unauthorized` | `{"success": false, "message": "Email atau password salah"}` | Sesuai | ✅ Pass |
| API-LGN-003 | Login dengan password salah | `{"email": "user@shopeasy.com", "password": "WrongPass"}` | `401 Unauthorized` | `{"success": false, "message": "Email atau password salah"}` | Sesuai | ✅ Pass |
| API-LGN-004 | Login tanpa field email | `{"password": "Test@1234"}` | `400 Bad Request` | `{"success": false, "message": "Email wajib diisi"}` | Sesuai | ✅ Pass |
| API-LGN-005 | Login tanpa field password | `{"email": "user@shopeasy.com"}` | `400 Bad Request` | `{"success": false, "message": "Password wajib diisi"}` | Sesuai | ✅ Pass |
| API-LGN-006 | Login dengan body kosong | `{}` | `400 Bad Request` | `{"success": false, "message": "Email dan password wajib diisi"}` | Sesuai | ✅ Pass |
| API-LGN-007 | Login dengan format email invalid | `{"email": "invalidemail", "password": "Test@1234"}` | `422 Unprocessable Entity` | `{"success": false, "message": "Format email tidak valid"}` | Sesuai | ✅ Pass |

---

## 2. API: POST /api/auth/register

### Endpoint Detail

| Field | Detail |
|---|---|
| **Method** | POST |
| **URL** | `/api/auth/register` |
| **Content-Type** | application/json |
| **Auth** | Tidak perlu (public endpoint) |

### Request Body Format

```json
{
  "name": "string",
  "email": "string",
  "password": "string",
  "phone": "string"
}
```

### Test Cases

| Test ID | Skenario | Request Body | Expected Status Code | Expected Response | Actual Result | Status |
|---|---|---|---|---|---|---|
| API-REG-001 | Register dengan data valid | `{"name": "Test User", "email": "newuser@email.com", "password": "Test@1234", "phone": "081234567890"}` | `201 Created` | `{"success": true, "message": "Registrasi berhasil"}` | Sesuai | ✅ Pass |
| API-REG-002 | Register dengan email yang sudah terdaftar | `{"name": "Test", "email": "user@shopeasy.com", "password": "Test@1234", "phone": "081234567890"}` | `409 Conflict` | `{"success": false, "message": "Email sudah terdaftar"}` | Sesuai | ✅ Pass |
| API-REG-003 | Register tanpa field name | `{"email": "new@email.com", "password": "Test@1234", "phone": "081234567890"}` | `400 Bad Request` | `{"success": false, "message": "Nama wajib diisi"}` | Sesuai | ✅ Pass |
| API-REG-004 | Register dengan password kurang dari 8 karakter | `{"name": "Test", "email": "new@email.com", "password": "Test1", "phone": "081234567890"}` | `422 Unprocessable Entity` | `{"success": false, "message": "Password minimal 8 karakter"}` | Sesuai | ✅ Pass |

---

## 3. API: GET /api/users/profile

### Endpoint Detail

| Field | Detail |
|---|---|
| **Method** | GET |
| **URL** | `/api/users/profile` |
| **Auth** | Bearer Token (JWT) |

### Test Cases

| Test ID | Skenario | Header | Expected Status Code | Expected Response | Actual Result | Status |
|---|---|---|---|---|---|---|
| API-PRF-001 | Get profile dengan token valid | `Authorization: Bearer <valid_token>` | `200 OK` | `{"success": true, "data": {"id": 1, "name": "Test User", "email": "user@shopeasy.com"}}` | Sesuai | ✅ Pass |
| API-PRF-002 | Get profile tanpa token | *(tanpa header Authorization)* | `401 Unauthorized` | `{"success": false, "message": "Token tidak ditemukan"}` | Sesuai | ✅ Pass |
| API-PRF-003 | Get profile dengan token expired | `Authorization: Bearer <expired_token>` | `401 Unauthorized` | `{"success": false, "message": "Token sudah kadaluarsa"}` | Sesuai | ✅ Pass |
| API-PRF-004 | Get profile dengan token invalid | `Authorization: Bearer invalidtoken123` | `403 Forbidden` | `{"success": false, "message": "Token tidak valid"}` | Sesuai | ✅ Pass |

---

## Ringkasan Hasil

| Endpoint | Total Test | Pass | Fail |
|---|---|---|---|
| POST /api/auth/login | 7 | 7 | 0 |
| POST /api/auth/register | 4 | 4 | 0 |
| GET /api/users/profile | 4 | 4 | 0 |
| **Total** | **15** | **15** | **0** |

**Pass Rate: 100%**
