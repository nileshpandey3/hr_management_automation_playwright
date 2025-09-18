from playwright.sync_api import Page, expect
from setup import BASE_URL
import pytest
# create a new incognito browser context

@pytest.mark.login
def test_login(page: Page):
    page.goto(BASE_URL)

    # Interact with login form
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    # Continue with the test
    storage = page.context.storage_state(path="state.json")
    