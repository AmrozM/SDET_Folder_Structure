class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.google.com")