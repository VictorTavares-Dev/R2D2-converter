import logging
from pythonjsonlogger import jsonlogger
from app.utils import get_datetime
from app.config import SERVICE_NAME, ROOT_DIR

# Sets logger and handler for class
logger = logging.getLogger()
logger.disabled = True  # Disables log inputs in console application
logger.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter()

if len(logger.handlers) > 0:
    logger.handlers[0].setFormatter(formatter)
else:
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)


class Logger:
    """
    A class to represent a log service.

    Attributes
    ----------
    log_file: txt
        text file of the current execution named in the format 'Log_<SERVICE_NAME>_<CURRENT_DATETIME>'. Stored in
        /Logs directory of the project.

    Methods
    -------
    log_formatter(): dict
        formats and writes the step log based on levels of severity and time of input in log_file.
    info(): void
        logs messages in an info level.
    warn(): void
        logs messages in a warning level.
    error(): void
        logs messages in an error level.
    """
    def __init__(self):
        self.log_file = open(f'{ROOT_DIR}\\Logs\\{"Log_" + SERVICE_NAME + "_" + get_datetime().replace(" ","_").replace(":","") + ".txt"}', "w+")

    def log_formatter(self, level, message, stack_trace=None):
        """
        Formats and writes the step log based on levels of severity and time of input in log_file.

        Parameters
        ----------
            level : str
                level of a log input (INFO, WARN or ERROR).
            message: str
                the message to be inserted in a log input.
            stack_trace: str
                a traceback of the exception raised at ERROR level.
        Returns
        -------
            formatted_log: str
                formatted log of a log input.
        """
        if level == "ERROR":
            formatted_log = f"{get_datetime()} - {level}: {message}. {stack_trace}"
        else:
            formatted_log = f"{get_datetime()} - {level}: {message}"

        self.log_file.write(f"{formatted_log}\n")
        return formatted_log

    def info(self, message):
        """
        Insert log input of INFO level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.

        Returns
        -------
            None.
        """
        logger.info(self.log_formatter(level='INFO', message=message))

    def warn(self, message):
        """
        Insert log input of WARN level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.

        Returns
        -------
            None.
        """
        logger.warning(self.log_formatter(level='WARN', message=message))

    def error(self, message, stack_trace=None):
        """
        Insert log input of ERROR level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.
            stack_trace: str
                a traceback of the exception raised at this level.

        Returns
        -------
            None.
        """
        logger.error(self.log_formatter(level='ERROR', message=message, stack_trace=stack_trace))
