import logging

class logger_class :
    @staticmethod
    def log_gen_method():
     log_file = logging.FileHandler(".\\Logs\\bankapp.log")
     log_format = logging.Formatter("%(asctime)s : %(levelname)s :%(funcname)s: %(message)s")
     log_file.setFormatter(log_format)
     logger = logging.getLogger()
     logger.addHandler(log_file)
     logger.setLevel(logging.INFO)
     return logger

