from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page : Page):
        self.page = page
        self.login_heading = page.locator(".SignInForm-paper h1")
        self.userName = page.locator("#username")
        self.password = page.locator("#password")
        self.signInButton = page.locator('[data-test="signin-submit"]')
        self.SuccessLoginMessage = page.get_by_text("Get Started with Real World App")

    def SignIn(self,username,password):
        self.userName.click()
        self.userName.fill(username)
        self.password.click()
        self.password.fill(password)
        self.signInButton.click()

    def get_login_heading(self):
        return self.login_heading    
    def get_success_login_message(self):
        return self.SuccessLoginMessage