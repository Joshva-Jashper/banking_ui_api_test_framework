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
        self.DropDownButton = self.page.locator('[data-test="sidenav-toggle"]')
        self.HomeButton = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]').nth(0)
        self.MyAccountButton = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]').nth(1)
        self.BankAccount = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]').nth(2)
        self.Notification = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]').nth(3)
        self.RoutingnumberError = self.page.locator('#bankaccount-routingNumber-input-helper-text')
        self.AccountNumberLessThenError = self.page.locator('#bankaccount-accountNumber-input-helper-text')
        self.BankNameError = self.page.locator("#bankaccount-bankName-input-helper-text")
        self.AccountUserName = self.page.locator('[data-test="sidenav-user-full-name"]')
        



    def get_getStartedMsg(self):
        return self.getStartedMsg

    def click_nextStartedMsg(self):
        self.nextGetStartedMsg.click()

    def get_createBankAccountMsg(self):
        return self.createBankAccountMsg

    def ClickDropDown(self):
        self.DropDownButton.click()

    def enterBankInfo(self,bankName,routingNumber,accountNumber):
        self.bankName.fill(bankName)
        self.routingNumber.fill(routingNumber)
        self.accountNumber.fill(accountNumber)
        self.saveBankInfo.click()  

    def get_finishedMsg(self):
        return self.finishedMsg

    def click_finishedButton(self):
        self.finishedButton.click()    

    def ClickHomeButton(self):
        self.HomeButton.click()

    def ClickMyAccountButton(self):
        self.MyAccountButton.click()

    def ClickBankAccount(self):
        self.BankAccount.click()

    def ClickNotificationButton(self):
        self.Notification.click()                

    def GetRoutingnumberError(self):
        return self.RoutingnumberError

    def GetAccountNumberError(self):
        return self.AccountNumberLessThenError

    def GetBankNameError(self):
        return self.BankNameError

    def GetAccountUserName(self):
        return self.AccountUserName