import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(page):
    page.goto("https://naveenautomationlabs.com/opencart/index.php?route=account/register")
    yield page

    #browser = playwright.chromium.launch(headless=False, slow_mo=10)
    #browser = playwright.chromium.launch_persistent_context(headless=False, args='--start-maximized',viewport=True)
    #context = browser.new_context()
    #page = context.new_page()
