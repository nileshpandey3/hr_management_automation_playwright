import pytest
import re
from playwright.sync_api import Page
from playwright.sync_api import  expect
from setup import LEAVE

@pytest.mark.leave_page
class TestLeavePage:

    @pytest.fixture(autouse=True)
    def setup_class(cls, hrm_page: Page):
        cls.page = hrm_page
        cls.page.goto(LEAVE)
    
    def test_leave_layout(self):
        pass
        # get_by_role("heading", name="Leave List")
        # get_by_text("No Records Found")
        # get_by_text("No Records Found")
        # get_by_role("columnheader", name="Date")