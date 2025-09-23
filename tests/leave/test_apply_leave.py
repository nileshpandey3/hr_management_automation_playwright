import pytest
import re
from playwright.sync_api import Page
from playwright.sync_api import  expect
from setup import LEAVE

@pytest.mark.homepage_layout
class TestDashboardLayout:

    @pytest.fixture(autouse=True)
    def setup_class(cls, hrm_page: Page):
        cls.page = hrm_page
        cls.page.goto(LEAVE)
    
    def test_apply_leave(self):
        expect(self.page.locator("div").filter(has_text=re.compile(r"^From Date$")).nth(1)).to_be_visible
        # Click the calendar icon
        self.page.locator(".oxd-icon.bi-calendar").first.click
        self.page.get_by_role("listitem").filter(has_text="January").locator("i")
        # TODO complete the remaining steps























