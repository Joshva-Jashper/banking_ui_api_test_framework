from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.website_logo = page.locator(".SignUpForm-logo")
        self.signUpHeading = page.locator(".SignUpForm-paper h1")
        self.firstName = page.locator('#firstName')
        self.lastName = page.locator("#lastName")
        self.userName = page.locator('#username')
        self.password = page.locator('#password')
        self.confirmPassword = page.locator("#confirmPassword")
        self.signUpButton = page.locator('[data-test="signup-submit"]')
        self.dontHaveAccount = page.locator('[data-test="signup"]')

    def SignUp(self, firstName: str, lastName: str, userName: str, password: str, confirmPassword: str):
        self.firstName.click()
        self.firstName.fill(firstName)
        self.lastName.click()
        self.lastName.fill(lastName)
        self.userName.click()
        self.userName.fill(userName)
        self.password.click()
        self.password.fill(password)
        self.confirmPassword.click()
        self.confirmPassword.fill(confirmPassword)
        self.signUpButton.click()

    def get_website_logo(self):
        return self.website_logo
    
    def get_signUp_heading(self):
        return self.signUpHeading
    
    def click_dont_have_account(self):
        self.dontHaveAccount.click()
    

        
        
        
            
        
        
        
        
        
        