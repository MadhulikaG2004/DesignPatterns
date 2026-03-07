from abc import ABC,abstractmethod 
from notification_factory import NotificationFactory
class NotificationService:
   def __init__(self, factory: NotificationFactory):
        self.factory = factory

   def notify(self, to: str, body: str):
        message = self.factory.create_message()
        message.set_content(to, body)
        sender = self.factory.create_sender()
        sender.send(message)
