from sms_message import SMSMessage
from sms_sender import SMSSender
from notification_service import NotificationService
class smsFactory(NotificationService):
    def create_message(self):
        return SMSMessage()
    def create_sender(self):
        return SMSSender()
