import arrow


def utcnow_datetime_aware():
    """Returns timezone-aware datetime for the current UTC moment"""

    return arrow.utcnow().datetime
