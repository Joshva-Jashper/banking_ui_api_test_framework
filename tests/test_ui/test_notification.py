from playwright.sync_api import Page,expect

from pages.pages_ui.notification import Notification
from pages.pages_ui.new_transaction import NewTransaction
from pages.pages_ui.main import MainPage
from pages.pages_ui.transaction import Transaction
from faker import Faker
import pytest

@pytest.mark.ui
def test_PaymentRequestPaid(page : Page,SecondPage : Page):
    NotificationPage1 = Notification(page)
    NotificationPage2 = Notification(SecondPage)
    NewTransactionPage1 = NewTransaction(page)
    NewTransactionPage2 = NewTransaction(SecondPage)
    MainPageUI1 = MainPage(page)
    MainPageUI2 = MainPage(SecondPage)
    
    AccountUserName1 = MainPageUI1.GetAccountUserName().inner_text()
    AccountUserName2 = MainPageUI2.GetAccountUserName().inner_text()
    print(AccountUserName2)
    faker = Faker()
    NewTransactionPage1.ClickNewTransactionButton()
    NewTransactionPage1.FillTransactionContact(AccountUserName2)
    page.wait_for_timeout(5000)
    FirstTransactionContact = NewTransactionPage1.GetAllTransactionContact().first
    FirstTransactionContact.click()
    
    Amount = faker.random_int(min=30,max=30000)
    Note = faker.text()
    NewTransactionPage1.FillTransactionDetails(str(Amount),Note)
    NewTransactionPage1.ClickTransactionPayBtn()
    MainPageUI2.ClickNotificationButton()
    MainPageUI2.ClickHomeButton()
    MainPageUI2.ClickNotificationButton()
    expect(NotificationPage2.GetNotificationTitle()).to_contain_text("Notifications")
    MainPageUI2.ClickDropDown()
    FirstNotification = NotificationPage2.GetAllNotificationPaymentReceived().first
    expect(FirstNotification).to_contain_text("received payment.")    
    NotificationReadBtn = NotificationPage2.GetAllNotificationReadBtn().first
    NotificationReadBtn.click()

@pytest.mark.ui
def test_PaymentLike(page : Page , SecondPage : Page):
    NotificationPage1 = Notification(page)
    NotificationPage2 = Notification(SecondPage)
    NewTransactionPage1 = NewTransaction(page)
    NewTransactionPage2 = NewTransaction(SecondPage)
    TransactionPage1 = Transaction(page)
    MainPageUI1 = MainPage(page)
    MainPageUI2 = MainPage(SecondPage)
    
    AccountUserName1 = MainPageUI1.GetAccountUserName().inner_text()
    AccountUserName2 = MainPageUI2.GetAccountUserName().inner_text()
    print(AccountUserName2)
    faker = Faker()
    NewTransactionPage1.ClickNewTransactionButton()
    NewTransactionPage1.FillTransactionContact(AccountUserName2)
    page.wait_for_timeout(5000)
    FirstTransactionContact = NewTransactionPage1.GetAllTransactionContact().first
    FirstTransactionContact.click()
    
    Amount = faker.random_int(min=30,max=30000)
    Note = faker.text()
    NewTransactionPage1.FillTransactionDetails(str(Amount),Note)
    NewTransactionPage1.ClickTransactionPayBtn()
    MainPageUI2.ClickNotificationButton()
    MainPageUI2.ClickHomeButton()
    MainPageUI2.ClickNotificationButton()
    expect(NotificationPage2.GetNotificationTitle()).to_contain_text("Notifications")
    MainPageUI2.ClickDropDown()
    FirstNotification = NotificationPage2.GetAllNotificationPaymentReceived().first
    expect(FirstNotification).to_contain_text("received payment.")    
    NotificationReadBtn = NotificationPage2.GetAllNotificationReadBtn().first
    NotificationReadBtn.click()

    MainPageUI1.ClickHomeButton()
    TransactionPage1.clickMyTransaction()
    FirstTransaction = TransactionPage1.GetAllTransactionUnderTabs().first
    FirstTransaction.click()
    TransactionPage1.ClickTransactionLike()
    MainPageUI2.ClickDropDown()
    MainPageUI2.ClickHomeButton()
    MainPageUI2.ClickNotificationButton()
    expect(NotificationPage2.GetNotificationTitle()).to_contain_text("Notifications")
    MainPageUI2.ClickDropDown()
    FirstNotification = NotificationPage2.GetAllNotificationLike().first
    expect(FirstNotification).to_contain_text("liked a transaction.")    
    NotificationReadBtn = NotificationPage2.GetAllNotificationReadBtn().first
    NotificationReadBtn.click()


@pytest.mark.ui
def test_PaymentComment(page : Page , SecondPage : Page):
    NotificationPage1 = Notification(page)
    NotificationPage2 = Notification(SecondPage)
    NewTransactionPage1 = NewTransaction(page)
    NewTransactionPage2 = NewTransaction(SecondPage)
    TransactionPage1 = Transaction(page)
    MainPageUI1 = MainPage(page)
    MainPageUI2 = MainPage(SecondPage)
    
    AccountUserName1 = MainPageUI1.GetAccountUserName().inner_text()
    AccountUserName2 = MainPageUI2.GetAccountUserName().inner_text()
    print(AccountUserName2)
    faker = Faker()
    NewTransactionPage1.ClickNewTransactionButton()
    NewTransactionPage1.FillTransactionContact(AccountUserName2)
    page.wait_for_timeout(5000)
    FirstTransactionContact = NewTransactionPage1.GetAllTransactionContact().first
    FirstTransactionContact.click()
    
    Amount = faker.random_int(min=30,max=30000)
    Note = faker.text()
    NewTransactionPage1.FillTransactionDetails(str(Amount),Note)
    NewTransactionPage1.ClickTransactionPayBtn()
    MainPageUI2.ClickNotificationButton()
    MainPageUI2.ClickHomeButton()
    MainPageUI2.ClickNotificationButton()
    expect(NotificationPage2.GetNotificationTitle()).to_contain_text("Notifications")
    MainPageUI2.ClickDropDown()
    FirstNotification = NotificationPage2.GetAllNotificationPaymentReceived().first
    expect(FirstNotification).to_contain_text("received payment.")    
    NotificationReadBtn = NotificationPage2.GetAllNotificationReadBtn().first
    NotificationReadBtn.click()

    MainPageUI1.ClickHomeButton()
    TransactionPage1.clickMyTransaction()
    FirstTransaction = TransactionPage1.GetAllTransactionUnderTabs().first
    FirstTransaction.click()
    TransactionPage1.FillTransactionComment(faker.text())
    MainPageUI2.ClickDropDown()
    MainPageUI2.ClickHomeButton()
    MainPageUI2.ClickNotificationButton()
    expect(NotificationPage2.GetNotificationTitle()).to_contain_text("Notifications")
    MainPageUI2.ClickDropDown()
    FirstNotification = NotificationPage2.GetAllNotificationComment().first
    expect(FirstNotification).to_contain_text("commented on a transaction.")    
    NotificationReadBtn = NotificationPage2.GetAllNotificationReadBtn().first
    NotificationReadBtn.click()












