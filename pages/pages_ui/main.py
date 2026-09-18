from playwright.sync_api import Page

class MainPage:
    def __init__(self,page):
        self.page = page
        self.getStartedMsg = self.page.get_by_text("Get Started with Real World App")
        self.nextGetStartedMsg = self.page.locator('[data-test="user-onboarding-next"]')
        self.createBankAccountMsg = self.page.get_by_text("Create Bank Account")
        self.bankName = self.page.get_by_placeholder("Bank Name") 
        self.routingNumber = self.page.get_by_placeholder("Routing Number")
        self.accountNumber = self.page.get_by_placeholder("Account Number")
        self.saveBankInfo = self.page.locator('[data-test="bankaccount-submit"]')
        self.finishedMsg = self.page.get_by_text("Finished")
        self.finishedButton = self.page.locator('[data-test="user-onboarding-next"]')

    def get_getStartedMsg(self):
        return self.getStartedMsg

    def click_nextStartedMsg(self):
        self.nextGetStartedMsg.click()

    def get_createBankAccountMsg(self):
        return self.createBankAccountMsg

    def enterBankInfo(self,bankName,routingNumber,accountNumber):
        self.bankName.fill(bankName)
        self.routingNumber.fill(routingNumber)
        self.accountNumber.fill(accountNumber)
        self.saveBankInfo.click()  

    def get_finishedMsg(self):
        return self.finishedMsg

    def click_finishedButton(self):
        self.finishedButton.click()    