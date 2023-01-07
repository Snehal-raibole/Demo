import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("engineLog.log")  # file log location

    file_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") # file formate syntax "time:levelName:TcName:errorMessgae"
    file_handler.setFormatter(file_formatter)  #pass file format to file handler

    logger.addHandler(file_handler)   #give file_handler (format & log)location to logger object

    logger.setLevel(logging.WARNING)
    logger.debug("Its Debug Logs")
    logger.info("Its Info Logs")
    logger.warning("Its Warning Logs")
    logger.error("Its Error Logs")
    logger.critical("Its Critical Logs")
