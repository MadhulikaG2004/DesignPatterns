from sender import Sender
from message import Message
class EmailSender(Sender):
    def send(self, message: Message):
        print(f"Sending via SMTP: {message.format()}")