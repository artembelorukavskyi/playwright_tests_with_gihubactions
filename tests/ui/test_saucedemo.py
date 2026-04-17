from utils.config import Config

from playwright.sync_api import Page, expect, Playwright


def test_login_and_navigation(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')

    page.get_by_test_id('add-to-cart-sauce-labs-backpack').click()
    expect(page.get_by_test_id('shopping-cart-badge')).to_have_text('1')

    page.get_by_test_id('remove-sauce-labs-backpack').click()
    expect(page.get_by_test_id('shopping-cart-badge')).not_to_be_visible()

    page.get_by_test_id('item-4-title-link').click()
    expect(page.get_by_test_id('inventory-item-name')).to_have_text('Sauce Labs Backpack')

def test_products_count_on_page(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')
    expect(page.get_by_test_id('inventory-item')).to_have_count(6)

def test_add_products(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')

    page.get_by_test_id('add-to-cart-sauce-labs-backpack').click()
    expect(page.get_by_test_id('shopping-cart-badge')).to_have_count(1)

    page.get_by_test_id('item-4-title-link').click()
    expect(page.get_by_test_id('inventory-item-name')).to_have_text('Sauce Labs Backpack')
    expect(page.get_by_test_id('remove')).to_have_text('Remove')
    expect(page.get_by_test_id('remove')).to_be_enabled()

def test_remove_products(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')

    page.get_by_test_id('add-to-cart-sauce-labs-backpack').click()
    expect(page.get_by_test_id('shopping-cart-badge')).to_have_count(1)

    page.get_by_test_id('item-4-title-link').click()
    expect(page.get_by_test_id('inventory-item-name')).to_have_text('Sauce Labs Backpack')
    expect(page.get_by_test_id('remove')).to_have_text('Remove')
    expect(page.get_by_test_id('remove')).to_be_enabled()

    page.get_by_test_id('remove').click()
    expect(page.get_by_test_id('add-to-cart')).to_have_text('Add to cart')
    expect(page.get_by_test_id('add-to-cart')).to_be_enabled()
    expect(page.get_by_test_id('shopping-cart-link')).to_be_empty()


def test_sort_products_to_low_price(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')

    page.get_by_test_id('product-sort-container').select_option('lohi')
    expect(page.get_by_test_id('product-sort-container')).to_have_value('lohi')
    expect(page.get_by_test_id('inventory-item-price').first).to_have_text('$7.99')


def test_e2e(page: Page):
    page.goto(Config.SAUCE_URL)

    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()

    expect(page).to_have_url(f'{Config.SAUCE_URL}/inventory.html')

    page.get_by_test_id('add-to-cart-sauce-labs-backpack').click()
    page.get_by_test_id('shopping-cart-link').click()

    page.get_by_test_id('checkout').click()
    expect(page.get_by_test_id('title')).to_have_text('Checkout: Your Information')

    page.get_by_test_id('firstName').fill('John')
    page.get_by_test_id('lastName').fill('Doe')
    page.get_by_test_id('postalCode').fill('21000')

    page.get_by_test_id('continue').click()
    page.get_by_test_id('finish').click()

    expect(page.get_by_test_id('complete-header')).to_have_text('Thank you for your order!')
