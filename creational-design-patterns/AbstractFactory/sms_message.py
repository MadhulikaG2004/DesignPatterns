from message import Message
class SMSMessage(Message):
    def set_content(self, to, body):
        self.to=to
        self.body=body
    def format(self):
        return f"SMS to <{self.to}>: {self.body}"