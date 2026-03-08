from pages.home_page import HomePage

def test_open_home_page(page):
    home = HomePage(page)
    home.open()
    assert "Google" in page.title()

from pages.home_page import HomePage

def test_open_google(page):
    home = HomePage(page)
    home.open()
    assert "Google" in page.title()