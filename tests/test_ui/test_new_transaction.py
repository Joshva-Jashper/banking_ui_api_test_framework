from playwright.sync_api import Page,expect
import pytest
from pages.pages_ui.transaction import Transaction
from pages.pages_ui.new_transaction import NewTransaction
from utils.json_read import read_json_file
from faker import Faker

@pytest.mark.ui 
@pytest.mark.smoke
@pytest.mark.parametrize("name,transaction", read_json_file("test_data/test_contact.json"))
def test_createNewPayment(page:Page,name,transaction):
    TransactionPage = Transaction(page)
    NewTransactionPage = NewTransaction(page)
    faker = Faker()
    NewTransactionPage.ClickNewTransactionButton()
    NewTransactionPage.FillTransactionContact(name)
    FirstTransactionContact = NewTransactionPage.GetAllTransactionContact().first
    FirstTransactionContact.click()
    Amount = faker.random_int(min=30,max=30000)
    Note = faker.text()
    NewTransactionPage.FillTransactionDetails(str(Amount),Note)

    if transaction == "Pay":
        NewTransactionPage.ClickTransactionPayBtn()
    else:
        NewTransactionPage.ClickTransactionRequestBtn()

    NewTransactionPage.ClickReturnToTransaction()

    TransactionPage.clickMyTransaction()

    TransactionPage.GetAllTransactionUnderTabs().first.click()

    TransactionAmount = TransactionPage.GetTransactionAmount().inner_text()
    CleanAmount = (
        TransactionAmount.replace("$", "")
        .replace("-", "")
        .replace("+", "")
        .replace(",", "")
        .split(".")[0]  
        .strip()    
    )
    assert int(CleanAmount) == Amount
    TransacionNote = TransactionPage.GetTransactionDescription().inner_text().replace("\n"," ").strip()
    CleanNote = Note.replace("\n"," ").strip()
    assert TransacionNote == CleanNote

    TransactionAction = TransactionPage.GetTransactionAction().inner_text().strip()

    if (TransactionAction == "requested"):
        assert transaction == "Request"
    else:
        assert transaction == "Pay"    


@pytest.mark.ui 
@pytest.mark.parametrize("amount",read_json_file("test_data/amount.json"))
@pytest.mark.xfail(reason= "its allowing both Zero and Negative Values")
def test_PaymentWithZeroMoney(page:Page,amount):
    if isinstance(amount,tuple):
        amount = amount[0]
    TransactionPage = Transaction(page)
    NewTransactionPage = NewTransaction(page)
    faker = Faker()
    NewTransactionPage.ClickNewTransactionButton()
    NewTransactionPage.FillTransactionContact("Ted Parisian")
    FirstTransactionContact = NewTransactionPage.GetAllTransactionContact().first
    FirstTransactionContact.click()
    NewTransactionPage.FillTransactionDetails(amount,faker.text())
    NewTransactionPage.ClickTransactionPayBtn()
    TransactionMsg = NewTransactionPage.GetTransactionSuccessFullMsg().inner_text()

    expect(TransactionMsg).not_to_be_visible()
    

@pytest.mark.ui 
@pytest.mark.xfail(reason="with less Balance allowing to Pay Higher")
def test_PayExceedsCurrentBalance(page:Page):
    TransactionPage = Transaction(page)
    NewTransactionPage = NewTransaction(page)
    CurrentBalance = TransactionPage.GetCurrentBalance().inner_text()
    CurrentBalance_ = int(float(CurrentBalance.replace("$","").strip()))
    faker = Faker()
    NewTransactionPage.ClickNewTransactionButton()
    NewTransactionPage.FillTransactionContact("Ted Parisian")
    FirstTransactionContact = NewTransactionPage.GetAllTransactionContact().first
    FirstTransactionContact.click()
    NewTransactionPage.FillTransactionDetails(str(CurrentBalance_ +20),faker.text())
    NewTransactionPage.ClickTransactionPayBtn()

    TransactionMsg = NewTransactionPage.GetTransactionSuccessFullMsg()

    expect(TransactionMsg).not_to_be_visible()

   

    



    
    



    







