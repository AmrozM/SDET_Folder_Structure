import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_orangehrm_login(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(USERNAME, PASSWORD)
    #page.wait_for_timeout(timeout=10000)
    expect(login.dashboard_button).to_be_visible()
     #Wait for dashboard using URL pattern
    page.wait_for_url(re.compile(r".*/dashboard.*"), timeout=15000)
    expect(page).to_have_url(re.compile(".*dashboard.*"))
    assert re.search(r"/dashboard", page.url, re.IGNORECASE), page.url
#    assert "dashboard" in page.url.lower()