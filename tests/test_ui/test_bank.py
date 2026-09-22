from playwright.sync_api import Page,expect
import pytest
from pages.pages_ui.main import MainPage
from pages.pages_ui.banking import Banking
from utils.json_read import read_json_file

@pytest.mark.ui 
@pytest.mark.parametrize("BankName,RoutingNumber,AccountNumber,Status,ValidationError",read_json_file("test_data/bank_acount.json"))
def test_AddBankAccount(page:Page,BankName,RoutingNumber,AccountNumber,Status,ValidationError):
    MainPageUI = MainPage(page)
    BankingPage = Banking(page)
    MainPageUI.ClickBankAccount()
    BankingPage.ClickCreateAccountBtn()
    MainPageUI.bankName.fill(BankName)
    MainPageUI.routingNumber.fill(RoutingNumber)
    MainPageUI.accountNumber.fill(AccountNumber)
    if Status == "invalid":
        if "routing" in ValidationError:
            expect(MainPageUI.GetRoutingnumberError()).to_contain_text("Must contain a valid routing number")
            assert ValidationError == "Must contain a valid routing number"
        elif "least 9" in ValidationError:
            expect(MainPageUI.GetAccountNumberError()).to_contain_text("Must contain at least 9 digits")
            assert ValidationError == "Must contain at least 9 digits"
        elif "least 5" in ValidationError:
            expect(MainPageUI.GetBankNameError()).to_contain_text("Must contain at least 5 characters")   
            assert ValidationError == "Must contain at least 5 characters"
        else:
            expect(MainPageUI.GetAccountNumberError()).to_contain_text("Must contain no more than 12 digits") 
            assert ValidationError == "Must contain no more than 12 digits"

    else:          
        MainPageUI.saveBankInfo.click()
        expect(BankingPage.GetBankAccountTitle()).to_contain_text("Bank Accounts")
        FirtAccountName = BankingPage.GetAllBankAccountName().last
        assert FirtAccountName.inner_text() == BankName  

        
@pytest.mark.ui 
def test_DeleteBankAccount(page:Page):
    MainPageUI = MainPage(page)
    BankingPage = Banking(page)
    MainPageUI.ClickBankAccount()
    BankingPage.ClickCreateAccountBtn()
    MainPageUI.bankName.fill("Axis Bank")
    MainPageUI.routingNumber.fill("123456789")
    MainPageUI.accountNumber.fill("9876543221")
    MainPageUI.saveBankInfo.click()
    expect(BankingPage.GetBankAccountTitle()).to_contain_text("Bank Accounts")
    FirtAccountName = BankingPage.GetAllBankAccountName().last
    assert FirtAccountName.inner_text() == "Axis Bank"  
    BankAccountDeleteBtn = BankingPage.GetAllBankAccountDeleteBtn().last
    BankAccountDeleteBtn.click()
    AccountNameAfterDelete = BankingPage.GetAllBankAccountName().last
    expect(AccountNameAfterDelete).to_contain_text("(Deleted)")
    assert AccountNameAfterDelete.inner_text() == "Axis Bank (Deleted)"






    




