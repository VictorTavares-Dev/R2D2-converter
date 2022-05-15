from datetime import datetime


def get_datetime():
    """
    Gets current datetime in format 'YYYY-mm-dd HH:MM:SS.ffffff'

    Parameters
    ----------
        None.

    Returns
    -------
        current_datetime : str
            a string formatted datetime
    """
    current_datetime = str(datetime.now())
    return current_datetime
