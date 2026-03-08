# pages/base_page.py

from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self,page:Page):
        self.page=page

        def open(self, url: str):
            self.page.goto(url)

            def assert_title_contains(self, text:str):
                expect(self.page).to_have_title(lambda t: text in t)