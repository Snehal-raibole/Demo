import inspect
import logging

class BaseClass():
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("myLog.log")
        fileFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(fileFormatter)
        logger.addHandler(fileHandler)
