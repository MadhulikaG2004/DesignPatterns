from LoggerFactory import LoggerFactory
if __name__=="__main__":
    file_logger=LoggerFactory.create_logger("file")
    file_logger.logging("Hello")
    