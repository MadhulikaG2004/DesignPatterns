from abc import ABC,abstractmethod
class Message(ABC):
    @abstractmethod
    def set_content(self, to: str, body: str):
        pass

    @abstractmethod
    def format(self) -> str:
        pass