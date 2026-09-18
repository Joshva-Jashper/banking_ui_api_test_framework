from playwright.sync_api import Page,expect
from pages.pages_ui.transaction import Transaction
import pytest
from faker import Faker

@pytest.mark.ui
@pytest.mark.smoke
def test_transactionPage(page:Page):
    transaction_page = Transaction(page)
    transaction_page.clickEveryTransaction()
    allTransactionsUnderEveryone = transaction_page.GetAllTransactionUnderTabs().all()
    assert len(allTransactionsUnderEveryone) > 2

    transaction_page.clickFreindsTransaction()
    allTransactionsUnderFreinds = transaction_page.GetAllTransactionUnderTabs().all()
    assert len(allTransactionsUnderFreinds) == 0

    transaction_page.clickMyTransaction()
    allTransactionsUnderMine = transaction_page.GetAllTransactionUnderTabs().all()
    assert len(allTransactionsUnderMine) == 0

@pytest.mark.ui 
def test_singleTransaction(page:Page):
    transaction_page = Transaction(page)
    FirstTransaction = transaction_page.GetAllTransactionUnderTabs().all()[0]
    FirstTransaction.click()
    expect(transaction_page.GetTransactionTitle()).to_contain_text("Transaction Detail")
    Action = ["requested","paid"]
    expect(transaction_page.GetTransactionSender()).to_be_visible()
    expect(transaction_page.GetTransactionReceiver()).to_be_visible()
    expect(transaction_page.GetTransactionLike()).to_be_visible()
    expect(transaction_page.GetTransactionDescription()).to_be_visible()
    expect(transaction_page.GetTransactionAmount()).to_be_visible()
    TransactionAction = transaction_page.GetTransactionAction().inner_text()

    assert TransactionAction.strip() in Action

@pytest.mark.ui 
def test_TransactionLikeCount(page):
    transaction_page = Transaction(page)
    FirstTransaction = transaction_page.GetAllTransactionUnderTabs().all()[0]
    FirstTransaction.click()
    TransactionLikeCountBefore = int(transaction_page.GetTransactionLikeCount().inner_text())
    transaction_page.ClickTransactionLike()
    TransactionLikeCountAfter = int(transaction_page.GetTransactionLikeCount().inner_text())
    assert TransactionLikeCountBefore + 1 == TransactionLikeCountAfter 

    
@pytest.mark.ui 
def test_CommentSection(page):
    transactionPage = Transaction(page)
    FirstTransaction = transactionPage.GetAllTransactionUnderTabs().all()[0]
    faker = Faker()
    FirstTransaction.click()
    comment = faker.text().replace("\n", " ")
    transactionPage.FillTransactionComment(comment)
    FirstTransactionComment = transactionPage.GetAllTransactionComments().last.inner_text()
    assert FirstTransactionComment == comment


    