from email_message import EmailMessage
from email_sender import EmailSender
from notification_service import NotificationService
class EmailFactory(NotificationService):
    def create_message(self):
        return EmailMessage()
    def create_sender(self):
        return EmailSender()
