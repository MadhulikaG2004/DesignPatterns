from abc import ABC,abstractmethod
class Logger(ABC):
    @abstractmethod
    def logging(self,content):
        pass
