from playwright.sync_api import Page, expect
from setup import BASE_URL
import pytest
import re
import os
# create a new incognito browser context


@pytest.fixture(scope="session")
def hrm_page(browser):
    username = os.environ["APP_USERNAME"]
    password = os.environ["APP_PASSWORD"]
    context = browser.new_context()
    page = context.new_page()
    # Go to the starting url before each test.
    page.goto(BASE_URL)

    # Interact with login form & save the auth state
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("heading", name="Dashboard").wait_for(state="visible", timeout=10000)
    yield page
    page.close