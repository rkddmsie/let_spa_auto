from pages.login_page import LoginPage
from utils.config import BASE_URL

def test_login_success(page):
    page.goto(f"{BASE_URL}/login")

    login_page = LoginPage(page)
    login_page.login("admin", "123456")

    assert "dashboard" in page.url