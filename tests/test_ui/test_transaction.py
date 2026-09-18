from playwright.sync_api import Page,expect
from pages.pages_ui.transaction import Transaction
import pytest

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