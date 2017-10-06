from django.conf import settings
from dateutil import tz
from pytz import timezone
from datetime import datetime

def to_localtz(datetime):
    """ Convert datetime to local tz (Localtimezone is theses defined in settings TIME_ZONE)

    Args:
        datetime (datetime.datetime): datetime to convert
    Returns:
        datetime (datetime.datetime): converted to local tz

    """
    return datetime.astimezone(timezone(settings.TIME_ZONE))

def to_utc(datetime):
    """ Convert datetime to utc

    Args:
        datetime (datetime.datetime): datetime to convert
    Returns:
        datetime.datetime converted to utc

    """
    local = tz.gettz(settings.TIME_ZONE)
    datetime = datetime.replace(tzinfo=local)

    return datetime.astimezone(tz.gettz('UTC'))


def to_datetime(s_datetime, in_utc = True, format="%Y-%m-%d %H:%M:%S"):
    """ String to datetime in UTC by default

    Args:
        datetime (String): datetime in format yyyy-mm-dd hh:mm:ss
        localtz (boolean): default False means UTC is used, True means local tz according to TIME_ZONE settings
    Returns:
        datetime (datetime.datetime): converted

    """
    dt = datetime.strptime("{}".format(s_datetime),format)
    if in_utc:
        return to_utc(dt)
    else:
        return to_localtz(dt)