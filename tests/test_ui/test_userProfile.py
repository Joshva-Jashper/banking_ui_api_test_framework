from playwright.sync_api import Page
from pages.pages_ui.user_account import UserSetting
from pages.pages_ui.main import MainPage
import pytest
from faker import Faker

@pytest.mark.ui 
def test_UpdateUserProfile(page : Page):
    UserSettingPage = UserSetting(page)
    MainPageUI = MainPage(page)
    faker = Faker()
    FirstName = faker.first_name()
    LastName = faker.last_name()
    Email = faker.email()
    PhoneNumber = faker.random_int(min=1000000000, max=9999999999)
    MainPageUI.ClickMyAccountButton()

    UserSettingPage.UpdateUser(FirstName,LastName,Email,str(PhoneNumber))
    page.wait_for_timeout(2000)

    UserName = MainPageUI.GetAccountUserName().inner_text()

    assert UserName in f"{FirstName} {LastName}"
