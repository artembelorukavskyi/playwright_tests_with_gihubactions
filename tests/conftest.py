import pytest

@pytest.fixture(scope='session', autouse=True)
def configure_playwright(playwright):
    playwright.selectors.set_test_id_attribute('data-test')
