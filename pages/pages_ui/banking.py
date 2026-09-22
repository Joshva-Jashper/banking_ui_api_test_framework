from playwright.sync_api import Page

class Banking:
    def __init__(self,page:Page):
        self.page = page
        self.BankAccountTitle = self.page.locator('[class="MuiTypography-root MuiTypography-h6 MuiTypography-gutterBottom css-mpyo7s-MuiTypography-root"]')
        self.CreateBankAccountBtn = self.page.locator('[data-test="bankaccount-new"]')
        self.AllBankAccountsName = self.page.locator('[data-test="bankaccount-list"] li p')
        self.BankAccountDeleteBtn = self.page.locator('[data-test="bankaccount-delete"]')

    def GetBankAccountTitle(self):
        return self.BankAccountTitle

    def ClickCreateAccountBtn(self):
        self.CreateBankAccountBtn.click()

    def GetAllBankAccountName(self):
        return self.AllBankAccountsName

    def GetAllBankAccountDeleteBtn(self):
        return self.BankAccountDeleteBtn
            