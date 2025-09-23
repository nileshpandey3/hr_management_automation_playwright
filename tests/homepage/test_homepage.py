import pytest
import re
from playwright.sync_api import Page
from playwright.sync_api import  expect
from setup import HOMEPAGE, BASE_URL

@pytest.mark.homepage
class TestDashboard:

    @pytest.fixture(autouse=True)
    def setup_class(cls, hrm_page: Page):
        cls.page = hrm_page
        cls.page.goto(HOMEPAGE)

    @pytest.mark.side_nav_list_items_count
    def test_side_nav_list_items_count(self):
        items = self.page.get_by_label("Sidepanel").get_by_role("link")
        expect(items).to_have_count(13)
        
    @pytest.mark.side_nav_admin
    def test_side_nav_admin(self):
        expect(self.page.get_by_role("link", name="Admin")).to_be_visible

    @pytest.mark.side_nav_pim
    def test_side_nav_pim(self):
        expect(self.page.get_by_role("link", name="PIM")).to_be_visible

    @pytest.mark.side_nav_leave
    def test_side_nav_leave(self):
        expect(self.page.get_by_role("link", name="Leave")).to_be_visible

    @pytest.mark.side_nav_time
    def test_side_nav_time(self):
        expect(self.page.get_by_role("link", name="Time")).to_be_visible

    @pytest.mark.side_nav_recrt
    def test_side_nav_recrt(self):
        expect(self.page.get_by_role("link", name="Recruitment")).to_be_visible

    @pytest.mark.side_nav_my_info
    def test_side_nav_my_info(self):
        expect(self.page.get_by_role("link", name="My Info")).to_be_visible

    @pytest.mark.side_nav_my_perf
    def test_side_nav_my_perf(self):
        expect(self.page.get_by_role("link", name="Performance")).to_be_visible

    @pytest.mark.side_nav_my_dash
    def test_side_nav_my_dash(self):
        expect(self.page.get_by_role("link", name="Dashboard")).to_be_visible

    @pytest.mark.side_nav_my_dir
    def test_side_nav_my_dir(self):
        expect(self.page.get_by_role("link", name="Directory")).to_be_visible

    @pytest.mark.side_nav_my_maintnce
    def test_side_nav_my_maintnce(self):
        expect(self.page.get_by_role("link", name="Maintenance")).to_be_visible

    @pytest.mark.side_nav_my_claim
    def test_side_nav_my_claim(self):
        expect(self.page.get_by_role("link", name="Claim")).to_be_visible

    @pytest.mark.side_nav_my_buzz
    def test_side_nav_my_buzz(self):
        expect(self.page.get_by_role("link", name="Buzz")).to_be_visible


