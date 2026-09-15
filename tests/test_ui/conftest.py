from playwright.sync_api import Page,Playwright
import pytest

@pytest.fixture(scope = "function")
def browser_context(playwright : Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context(record_video_dir = "report/videos")
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope = "function")
def page(browser_context):
    browser_context.tracing.start(screenshots=True,snapshots=True)
    page = browser_context.new_page()
    page.goto("http://localhost:3000")
    yield page
    page.close()
    browser_context.tracing.stop(path="report/trace.zip")
   

