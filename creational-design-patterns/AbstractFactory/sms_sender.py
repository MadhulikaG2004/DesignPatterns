from sender import Sender 
from message import Message
class SMSSender(Sender):
    def send(self, message:Message):
        print(f"Sending via SMS: {message.format()}")
