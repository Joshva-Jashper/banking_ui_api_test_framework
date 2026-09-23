from playwright.sync_api import Page

class UserSetting:
    def __init__(self,page):
        self.page = page
        self.UserFirstName = self.page.locator("#user-settings-firstName-input")
        self.UserLastName = self.page.locator('#user-settings-lastName-input')
        self.UserEmail = self.page.locator('#user-settings-email-input')
        self.UserPhoneNumber = self.page.locator('#user-settings-phoneNumber-input')
        self.SaveBtn = self.page.locator('[data-test="user-settings-submit"]')

    def UpdateUser(self,FirstName,LastName,Email,PhoneNumber):
        self.UserFirstName.fill(FirstName)
        self.UserLastName.fill(LastName)
        self.UserEmail.fill(Email)
        self.UserPhoneNumber.fill(PhoneNumber)
        self.SaveBtn.click()    
        