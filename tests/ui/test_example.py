from utils.config import Config

def test_google(page):
    page.goto(Config.BASE_URL)
    assert 'Google' in page.title()
