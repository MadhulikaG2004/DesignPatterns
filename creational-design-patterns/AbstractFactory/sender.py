from abc import ABC,abstractmethod
from message import Message
class Sender(ABC):
    @abstractmethod
    def send(self,message:Message):
        pass
