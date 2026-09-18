from playwright.sync_api import Page,expect
from pages.pages_ui.login import LoginPage
from pages.pages_ui.register import RegisterPage
from pages.pages_ui.main import MainPage
import pytest
from faker import Faker

@pytest.mark.ui 
@pytest.mark.smoke
@pytest.mark.no_auth
def test_login_with_valid_credentials(page:Page):
    register_page = RegisterPage(page)
    faker = Faker()
    register_page.click_dont_have_account()
    register_page.click_dont_have_account()


    expect(register_page.get_website_logo()).to_be_visible()
    expect(register_page.get_signUp_heading()).to_be_visible()
    expect(register_page.get_signUp_heading()).to_contain_text("Sign Up")
    user_name = faker.user_name()
    password = faker.password()
    register_page.SignUp(faker.first_name(),faker.last_name(),user_name,password,password)
    login_page = LoginPage(page)
    expect(login_page.get_login_heading()).to_be_visible()
    expect(login_page.get_login_heading()).to_contain_text("Sign in")
    login_page.SignIn(user_name,password)
    expect(login_page.get_success_login_message()).to_be_visible()
    expect(login_page.get_success_login_message()).to_contain_text("Get Started with Real World App")

@pytest.mark.ui 
@pytest.mark.no_auth
def test_login_with_invalid_credentials(page:Page):
    login_page = LoginPage(page)
    login_page.SignIn("joshbkjcechjewnjwehj","joshva2006@")
    expect(login_page.get_invalid_login_msg()).to_be_visible()
    expect(login_page.get_invalid_login_msg()).to_contain_text("Username or password is invalid")

@pytest.mark.ui 
@pytest.mark.no_auth
def test_successfull_login_logout(page:Page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)
    main_page = MainPage(page)
    register_page = RegisterPage(page)
    faker = Faker()
    register_page.click_dont_have_account()
    register_page.click_dont_have_account()


    expect(register_page.get_website_logo()).to_be_visible()
    expect(register_page.get_signUp_heading()).to_be_visible()
    expect(register_page.get_signUp_heading()).to_contain_text("Sign Up")
    user_name = faker.user_name()
    password = faker.password()
    register_page.SignUp(faker.first_name(),faker.last_name(),user_name,password,password)
    login_page = LoginPage(page)
    expect(login_page.get_login_heading()).to_be_visible()
    expect(login_page.get_login_heading()).to_contain_text("Sign in")
    login_page.SignIn(user_name,password)
    expect(login_page.get_success_login_message()).to_be_visible()
    expect(login_page.get_success_login_message()).to_contain_text("Get Started with Real World App")

    expect(main_page.get_getStartedMsg()).to_contain_text("Get Started with Real World App")
    main_page.click_nextStartedMsg()
    main_page.enterBankInfo(faker.bank(),faker.aba(),faker.pystr(min_chars=9,max_chars=12));

    expect(main_page.get_finishedMsg()).to_contain_text("Finished")
    main_page.click_finishedButton()

    login_page.get_clickLogoutButton()
    expect(login_page.get_login_heading()).to_contain_text("Sign in")



