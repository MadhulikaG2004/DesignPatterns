from message import Message
class EmailMessage(Message):
    def set_content(self, to, body):
        self.to=to
        self.body=body
    def format(self):
        return f"Email to <{self.to}>: {self.body}"
    