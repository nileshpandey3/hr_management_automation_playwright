import pytest
import re
from playwright.sync_api import Page
from playwright.sync_api import  expect
from setup import HOMEPAGE, BASE_URL

@pytest.mark.homepage_layout
class TestDashboardLayout:

    @pytest.fixture(autouse=True)
    def setup_class(cls, hrm_page: Page):
        cls.page = hrm_page
        cls.page.goto(HOMEPAGE)
    
    def test_layout_items_time(self):
        expect(self.page.get_by_text("Time at Work")).to_be_visible

    def test_layout_items_my_actions(self):
        expect(self.page.get_by_text("My Actions")).to_be_visible
    
    def test_layout_items_q_launch(self):
        expect(self.page.get_by_text("Quick Launch")).to_be_visible

    def test_layout_items_buzz(self):
        expect(self.page.get_by_text("Buzz Latest Posts")).to_be_visible

    def test_layout_items_emp_leave(self):
        expect(self.page.get_by_text("Employees on Leave Today")).to_be_visible

    def test_layout_items_emp_distribtn(self):
        expect(self.page.get_by_text("Employee Distribution by Sub Unit")).to_be_visible

    def test_layout_items_emp_distribtn_loc(self):
        expect(self.page.get_by_text("Employee Distribution by Location")).to_be_visible

