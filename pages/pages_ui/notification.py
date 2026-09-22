from playwright.sync_api import Page

class Notification:
    def __init__(self,page):
        self.page = page
        self.NotificationTitle = self.page.locator('[class="MuiTypography-root MuiTypography-h6 MuiTypography-gutterBottom css-mpyo7s-MuiTypography-root"]')
        self.AllNotification = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]:has-text("received")')
        self.NotificaitonReadBtn = self.page.locator('[data-test^="notification-mark-read"]')


    def GetNotificationTitle(self):
        return self.NotificationTitle

    def GetAllNotification(self):
        return self.AllNotification

    def GetAllNotificationReadBtn(self):
        return self.NotificaitonReadBtn        