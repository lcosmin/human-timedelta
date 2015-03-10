import re
import datetime


# TODO: accept things like 1 day instead of 1 days

_regex = "|".join([r"(?:(?P<seconds>\d+(?:\.\d+)?)\s*(?:s|seconds))",
                   r"(?:(?P<minutes>\d+(?:\.\d+)?)\s*(?:m|minutes))",
                   r"(?:(?P<hours>\d+(?:\.\d+)?)\s*(?:h|hours))",
                   r"(?:(?P<days>\d+(?:\.\d+)?)\s*(?:d|days))"])

_rex = re.compile(_regex, re.I)


def parse(s):
    """
    Parse human specific timedelta and return :class:`datetime.timedelta` object
    """
    td = {"days": 0.0, "hours": 0.0, "minutes": 0.0, "seconds": 0.0}

    for m in _rex.finditer(s):
        for k in td.keys():
            v = m.group(k)
            if v is not None:
                td[k] = float(v)

    return datetime.timedelta(days=td["days"],
                              seconds=td["seconds"],
                              minutes=td["minutes"],
                              hours=td["hours"])
