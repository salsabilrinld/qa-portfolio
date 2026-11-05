"""
Test Automation: Halaman Login — ShopEasy E-Commerce
Framework: Selenium WebDriver + pytest
Author: [Nama Kamu]
Date: November 2026

Script ini mengotomatiskan pengujian fungsional halaman login
menggunakan Selenium WebDriver dengan Python dan pytest.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# ============================================================
# KONFIGURASI
# ============================================================

BASE_URL = "https://staging.shopeasy-demo.com"
LOGIN_URL = f"{BASE_URL}/login"

# Test data
VALID_EMAIL = "user@shopeasy.com"
VALID_PASSWORD = "Test@1234"
INVALID_EMAIL = "tidakada@email.com"
INVALID_PASSWORD = "SalahPassword123"


# ============================================================
# FIXTURE — Setup dan Teardown browser
# ============================================================

@pytest.fixture
def driver():
    """Setup Chrome browser sebelum setiap test."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Jalankan tanpa GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # Teardown — tutup browser setelah test selesai
    driver.quit()


# ============================================================
# TEST CASES
# ============================================================

class TestLoginPage:
    """Test suite untuk halaman login ShopEasy."""

    def test_login_page_elements(self, driver):
        """
        TC-AUTO-001: Verifikasi elemen-elemen halaman login tampil dengan benar.

        Expected: Field email, field password, tombol Masuk, dan link
        Lupa Password harus terlihat di halaman login.
        """
        driver.get(LOGIN_URL)

        # Verifikasi field email ada
        email_field = driver.find_element(By.ID, "email")
        assert email_field.is_displayed(), "Field email tidak ditemukan"

        # Verifikasi field password ada
        password_field = driver.find_element(By.ID, "password")
        assert password_field.is_displayed(), "Field password tidak ditemukan"

        # Verifikasi tombol Masuk ada
        login_button = driver.find_element(By.ID, "btn-login")
        assert login_button.is_displayed(), "Tombol Masuk tidak ditemukan"
        assert login_button.text == "Masuk", f"Teks tombol salah: {login_button.text}"

        # Verifikasi link Lupa Password ada
        forgot_password_link = driver.find_element(By.LINK_TEXT, "Lupa Password?")
        assert forgot_password_link.is_displayed(), "Link Lupa Password tidak ditemukan"

    def test_login_valid_credentials(self, driver):
        """
        TC-AUTO-002: Login dengan email dan password yang valid.

        Expected: Pengguna berhasil login dan diarahkan ke halaman Dashboard.
        """
        driver.get(LOGIN_URL)

        # Masukkan email valid
        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(VALID_EMAIL)

        # Masukkan password valid
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(VALID_PASSWORD)

        # Klik tombol Masuk
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()

        # Tunggu sampai redirect ke Dashboard
        WebDriverWait(driver, 10).until(
            EC.url_contains("/dashboard")
        )

        # Verifikasi URL saat ini adalah halaman Dashboard
        assert "/dashboard" in driver.current_url, \
            f"Tidak redirect ke dashboard. URL saat ini: {driver.current_url}"

    def test_login_empty_email(self, driver):
        """
        TC-AUTO-003: Login dengan email kosong.

        Expected: Muncul pesan validasi "Email wajib diisi".
        """
        driver.get(LOGIN_URL)

        # Kosongkan field email (langsung skip)
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(VALID_PASSWORD)

        # Klik tombol Masuk
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()

        # Verifikasi pesan error muncul
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "Email wajib diisi" in error_message.text, \
            f"Pesan error tidak sesuai: {error_message.text}"

    def test_login_empty_password(self, driver):
        """
        TC-AUTO-004: Login dengan password kosong.

        Expected: Muncul pesan validasi "Password wajib diisi".
        """
        driver.get(LOGIN_URL)

        # Masukkan email valid
        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(VALID_EMAIL)

        # Kosongkan field password (langsung skip)

        # Klik tombol Masuk
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()

        # Verifikasi pesan error muncul
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "Password wajib diisi" in error_message.text, \
            f"Pesan error tidak sesuai: {error_message.text}"

    def test_login_wrong_password(self, driver):
        """
        TC-AUTO-005: Login dengan password yang salah.

        Expected: Muncul pesan error "Email atau password salah".
        """
        driver.get(LOGIN_URL)

        # Masukkan email valid
        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(VALID_EMAIL)

        # Masukkan password salah
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(INVALID_PASSWORD)

        # Klik tombol Masuk
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()

        # Verifikasi pesan error muncul
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "Email atau password salah" in error_message.text, \
            f"Pesan error tidak sesuai: {error_message.text}"

    def test_login_invalid_email_format(self, driver):
        """
        TC-AUTO-006: Login dengan format email yang tidak valid.

        Expected: Muncul validasi format email.
        """
        driver.get(LOGIN_URL)

        # Masukkan email dengan format salah
        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys("emailtanpaat.com")

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(VALID_PASSWORD)

        # Klik tombol Masuk
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()

        # Verifikasi pesan validasi muncul
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "email yang valid" in error_message.text.lower(), \
            f"Pesan error tidak sesuai: {error_message.text}"
