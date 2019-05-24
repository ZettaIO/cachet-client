from datetime import datetime


def to_datetime(timestamp: str):
    """
    Convert string to datetime of format '2019-05-24 09:26:22'

    Args:
        timestamp (str): String timestamp

    Returns:
        datetime if input is a valid datetime string
    """
    if timestamp is None:
        return None

    return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
