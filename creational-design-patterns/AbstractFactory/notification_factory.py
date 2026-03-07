from abc import abstractmethod,ABC
from message import Message
from sender import Sender
class NotificationFactory(ABC):
    @abstractmethod
    def create_message(self) -> Message:
        pass

    @abstractmethod
    def create_sender(self) -> Sender:
        pass