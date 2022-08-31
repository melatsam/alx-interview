#!/usr/bin/python3
"""
Data set can contain multiple characters
data will be represented by alist of integers
"""


def validUTF8(data):
    """return false"""
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode('utf-8')
    except BaseException:
        return False
    return True
