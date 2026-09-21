from playwright.sync_api import Page

class NewTransaction:
    def __init__(self,page):
        self.page = page
        self.NewTransactionButton = self.page.locator('[href="/transaction/new"]')
        self.AllTransactionContact =self.page.locator('[data-test="users-list"] li')
        self.TransactionSearchContact = self.page.locator('#user-list-search-input')
        self.TransactionPersonName = self.page.locator(".MuiBox-root h2")
        self.TransactionMoney = self.page.locator('#amount')
        self.TransactionNote = self.page.get_by_placeholder("Add a note")
        self.TransactionRequestButton = self.page.locator('[data-test="transaction-create-submit-request"]')
        self.TransactionPayButton = self.page.locator('[data-test="transaction-create-submit-payment"]')
        self.TransactionSuccesfullMsg = self.page.locator('[class="MuiBox-root css-jtg8mn"] [class="MuiGrid-root MuiGrid-item css-13i4rnv-MuiGrid-root"] h2')
        self.ReturnTotransactionBtn = self.page.locator('[data-test="new-transaction-return-to-transactions"]')
        self.CreateNewTransaction = self.page.locator('[data-test="new-transaction-create-another-transaction"]')

    def ClickNewTransactionButton(self):
        self.NewTransactionButton.click()

    def GetAllTransactionContact(self):
        return self.AllTransactionContact

    def FillTransactionContact(self,name):
        self.TransactionSearchContact.fill(name)

    def GetTransactionContactName(self):
        return self.TransactionPersonName 

    def FillTransactionDetails(self,amount,note):
        self.TransactionMoney.fill(amount)
        self.TransactionNote.fill(note)

    def ClickReturnToTransaction(self):
        self.ReturnTotransactionBtn.click()

    def ClickCreatenewTransaction(self):
        self.CreateNewTransaction.click()

    def ClickTransactionPayBtn(self):
        self.TransactionPayButton.click()

    def ClickTransactionRequestBtn(self):
        self.TransactionRequestButton.click()    

    def GetTransactionSuccessFullMsg(self):
        return self.TransactionSuccesfullMsg    

