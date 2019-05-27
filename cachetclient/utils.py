import re
from datetime import datetime


def to_datetime(timestamp: str):
    """
    Convert string to datetime of formats::

        '2019-05-24 09:26:22'
        'Friday 24th May 2019 10:01:44'

    Args:
        timestamp (str): String timestamp

    Returns:
        datetime if input is a valid datetime string
    """
    if timestamp is None:
        return None

    try:
        # '2019-05-24 09:26:22'
        return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        pass

    try:
        # 'Friday 1st May 2019 10:01:44'. Used in verified_at for subscribers
        sub_timestamp = re.sub(r"\b([0123]?[0-9])(st|th|nd|rd)\b", r"\1", timestamp)
        return datetime.strptime(sub_timestamp, '%A %d %B %Y %H:%M:%S')
    except ValueError:
        pass

    raise ValueError("datetime string '{}' not supported".format(timestamp))
