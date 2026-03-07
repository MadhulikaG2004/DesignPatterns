from Logger import Logger
class FileLogger(Logger):
    def logging(self,content:str):
        print(f"File Logger:{content}")
        