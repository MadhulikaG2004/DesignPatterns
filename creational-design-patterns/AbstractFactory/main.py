from notification_service import NotificationService
from email_factory import EmailFactory
if __name__=="__main__":
    service=NotificationService(EmailFactory())
    service.notify("alice@example.com", "Your order has been shipped!")