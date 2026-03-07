from Logger import Logger
class ConsoleLogger(Logger):
    def logging(self,content:str):
        print(f"Console Logger: {content}")
