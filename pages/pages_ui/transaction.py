from playwright.sync_api import Page

class Transaction:
    def __init__(self,page):
        self.page = page
        self.EveryTransaction = self.page.locator('[href="/"]:has-text("EVERYONE")')
        self.FreindsTransaction = self.page.get_by_text("Friends")
        self.MyTransaction = self.page.get_by_text("Mine")
        self.AllTransactionUnderTabs = self.page.locator('[class="ReactVirtualized__Grid__innerScrollContainer"] li')
        self.TransactionTitle = self.page.get_by_text("Transaction Detail")
        self.TransactionSender = self.page.locator('[data-test^="transaction-sender"]').nth(1)
        self.TransactionReceiver = self.page.locator('[data-test^="transaction-receiver"]').nth(1)
        

        

    def clickEveryTransaction(self):
        self.EveryTransaction.click()

    def clickFreindsTransaction(self):
        self.FreindsTransaction.click()

    def clickMyTransaction(self):
        self.MyTransaction.click()

    def GetAllTransactionUnderTabs(self):
        return self.AllTransactionUnderTabs;          