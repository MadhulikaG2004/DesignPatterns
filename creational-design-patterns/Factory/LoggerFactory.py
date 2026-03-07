from FileLogger import FileLogger
from ConsoleLogger import ConsoleLogger
class LoggerFactory:
    def create_logger(logger_type:str):
        if logger_type=="file":
            return FileLogger()
        elif logger_type=="console":
            return ConsoleLogger()
        else:
            return "Invalid Logger Type provided!"