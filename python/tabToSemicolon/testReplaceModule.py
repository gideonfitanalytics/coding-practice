import re


def replaceTabs(c):
    return re.sub("\t", ";", c)
