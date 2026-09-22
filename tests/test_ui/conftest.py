from playwright.sync_api import Page,Playwright,expect
import pytest
from pages.pages_ui.register import RegisterPage
from pages.pages_ui.login import LoginPage
from pages.pages_ui.main import MainPage
from faker import Faker

@pytest.fixture(scope = "function")
def browser_context(request,playwright : Playwright,storage_state):
    browser = playwright.chromium.launch(headless = False)

    if "no_auth" in request.node.keywords:
        context = browser.new_context(record_video_dir = "report/videos")
    else:
        context = browser.new_context(record_video_dir = "report/videos",storage_state=storage_state)
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope = "function")
def SecondbrowserContext(request,playwright : Playwright,SecondStorageState):
    browser = playwright.chromium.launch(headless = False)

    if "no_auth" in request.node.keywords:
        context = browser.new_context(record_video_dir = "report/videos")
    else:
        context = browser.new_context(record_video_dir = "report/videos",storage_state=SecondStorageState)
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope = "session")
def storage_state(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000")
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

    token_path = "auth/token.json"
    context.storage_state(path=token_path)

    page.close()
    context.close()
    browser.close()
    return token_path



@pytest.fixture(scope = "session")
def SecondStorageState(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000")
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

    token_path = "auth/token2.json"
    context.storage_state(path=token_path)

    page.close()
    context.close()
    browser.close()
    return token_path



@pytest.fixture(scope = "function")
def page(browser_context):
    browser_context.tracing.start(screenshots=True,snapshots=True)
    page = browser_context.new_page()
    page.goto("http://localhost:3000")
    yield page
    page.close()
    browser_context.tracing.stop(path="report/trace.zip")
   

@pytest.fixture(scope = "function")
def SecondPage(SecondbrowserContext):
    SecondbrowserContext.tracing.start(screenshots=True,snapshots=True)
    page = SecondbrowserContext.new_page()
    page.goto("http://localhost:3000")
    yield page
    page.close()
    SecondbrowserContext.tracing.stop(path="report/trace.zip")