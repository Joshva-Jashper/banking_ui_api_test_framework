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
        self.TransactionAction = self.page.locator('[data-test^="transaction-action"]')
        self.TransactionAmount = self.page.locator('[data-test^="transaction-amount"]')
        self.TransactionDescription = self.page.locator('[data-test="transaction-description"]')
        self.TransactionComment = self.page.get_by_placeholder("Write a comment...")
        self.TransactionLike = self.page.locator('[data-test^="transaction-like-button"]')
        self.TransactionLikeCount = self.page.locator('[data-test^="transaction-like-count"]')
        self.AllTransactionComments = self.page.locator('[data-test="comments-list"] li')
        self.CurrentAccountBalance = self.page.locator('[data-test="sidenav-user-balance"]')

        

    def GetCurrentBalance(self):
        return self.CurrentAccountBalance

    def clickEveryTransaction(self):
        self.EveryTransaction.click()

    def clickFreindsTransaction(self):
        self.FreindsTransaction.click()

    def clickMyTransaction(self):
        self.MyTransaction.click()

    def GetAllTransactionUnderTabs(self):
        return self.AllTransactionUnderTabs;     

    def GetTransactionTitle(self):
        return self.TransactionTitle

    def GetTransactionSender(self):
        return self.TransactionSender

    def GetTransactionReceiver(self):
        return self.TransactionReceiver

    def GetTransactionAction(self):
        return self.TransactionAction

    def GetTransactionAmount(self):
        return self.TransactionAmount

    def GetTransactionComment(self):
        return self.TransactionComment

    def GetTransactionDescription(self):
        return self.TransactionDescription

    def FillTransactionComment(self,comment):
        self.TransactionComment.fill(comment)
        self.TransactionComment.press("Enter")

    def ClickTransactionLike(self):
        self.TransactionLike.click()     

    def GetTransactionLike(self):
        return self.TransactionLike    

    def GetTransactionLikeCount(self):
        return self.TransactionLikeCount   

    def GetAllTransactionComments(self):
        return self.AllTransactionComments  
