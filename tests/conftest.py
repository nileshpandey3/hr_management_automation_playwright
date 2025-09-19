from playwright.sync_api import Page, expect
from setup import BASE_URL
import pytest
import re
# create a new incognito browser context


@pytest.fixture(scope="session")
def hrm_page(browser):
    context = browser.new_context()
    page = context.new_page()
    # Go to the starting url before each test.
    page.goto(BASE_URL)

    # Interact with login form & save the auth state
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.context.storage_state(path="state.json")
    page.get_by_role("heading", name="Dashboard").wait_for(state="visible", timeout=10000)
    yield page
    page.close