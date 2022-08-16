import re


def to_camel_case(text):
    return ''.join(x.lower() if (not x.istitle() and x == re.split('_|-', text)[0]) else x.lower().capitalize() for x in
                   re.split('_|-', text))
