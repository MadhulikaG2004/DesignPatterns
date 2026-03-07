from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def notify(self,msg):
	    pass
class EmailNotification(Notification):
    def notify(self,msg):
	    print(f"email notification..,{msg}")
class SMSNotification(Notification):
    def notify(self,msg):
	    print(f"sms notification…,{msg}")
class NotificationAdapter(Notification):
	def __init__(self,adapter):
		self.adapter=adapter
	def notify(self,msg):
		self.adapter.notification(msg)
class YahooNotification:
	def notification(self,msg):
		print(f"yahoo notification,{msg}")
if __name__=="__main__":
	notify= NotificationAdapter(YahooNotification())
	notify.notify("hello")
