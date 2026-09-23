from playwright.sync_api import Page

class Notification:
    def __init__(self,page):
        self.page = page
        self.NotificationTitle = self.page.locator('[class="MuiTypography-root MuiTypography-h6 MuiTypography-gutterBottom css-mpyo7s-MuiTypography-root"]')
        self.AllNotificationPaymentReceived = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]:has-text("received")')
        self.NotificaitonReadBtn = self.page.locator('[data-test^="notification-mark-read"]')
        self.AllNotificationLike = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]:has-text("liked a transaction.")')
        self.AllNotificationComment = self.page.locator('[class="MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-13s1204-MuiTypography-root"]:has-text("commented on a transaction.")')




    def GetNotificationTitle(self):
        return self.NotificationTitle

    def GetAllNotificationPaymentReceived(self):
        return self.AllNotificationPaymentReceived

    def GetAllNotificationReadBtn(self):
        return self.NotificaitonReadBtn        

    def GetAllNotificationLike(self):
        return self.AllNotificationLike

    def GetAllNotificationComment(self):
            return self.AllNotificationComment