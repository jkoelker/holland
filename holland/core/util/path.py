# $Id$
"""
Utility functions
"""

# Functions added here should really be as portable as possible
# and generally useful.

import os
import sys
import logging

LOGGER = logging.getLogger(__name__)

def ensure_dir(dir_path):
    """
    Ensure a directory path exists (by creating it if it doesn't).
    """

    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            LOGGER.debug("created directory %s" % dir_path)
            return True
        except OSError, e:
            # FIX ME: Need error codes/etc so this will exit(<code>) or raise
            # an appropriate holland exception
            LOGGER.error("os.makedirs(%s): %s" % (dir_path, e))
            raise
    return False

def protected_path(path):
    """
    Take a path, and if the file/dir exist pass back a protected path
    (suffixed).

    Returns:

        string = new file path

    Example:

        >>> mypath = '/tmp'
        >>> new_path = helpers.protected_path(mypath)
        >>> new_path
        '/tmp.0'
    """
    log = logging.getLogger(__name__)
    safety = 0
    safe_path = path
    while True:
        if os.path.exists(safe_path):
            safe_path = "%s.%s" % (path, safety)
        else:
            break
        safety = safety + 1
    return safe_path

def format_bytes(bytes, precision=2):
    """
    Format an integer number of bytes to a human
    readable string.

    If bytes is negative, this method raises ArithmeticError
    """
    import math

    if bytes < 0:
        raise ArithmeticError("Only Positive Integers Allowed")

    if bytes != 0:
        exponent = math.floor(math.log(bytes, 1024))
    else:
        exponent = 0

    return "%.*f%s" % (
        precision,
        bytes / (1024 ** exponent),
        ['B','KB','MB','GB','TB','PB','EB','ZB','YB'][int(exponent)]
    )


def normpath(path):
    from os.path import normpath, abspath
    return abspath(normpath(path))

def relpath(origin, dest):
    """
    Find the relative path between origin and dest
    """
    parts = []
    origin = os.path.normpath(origin)
    dest = os.path.normpath(dest)

    if origin == dest:
        return ""

    path = dest
    while True:
        head, tail = os.path.split(path)

        if not tail:
            break

        if head == origin:
            return os.path.join('', *([tail] + parts))
        else:
            parts.insert(0, tail)
        path = head
    return None

def getmount(path):
    """Return the mount point of a path

    :param path: path to find the mountpoint for

    :returns: str mounpoint path
    """

    path = os.path.realpath(path)

    while path != os.path.sep:
        if os.path.ismount(path):
            return path
        path = os.path.abspath(os.path.join(path, os.pardir))
    return path

def disk_capacity(target_path):
    """Find the total capacity of the filesystem that target_path is on

    :returns: integer number of bytes
    """
    path = getmount(target_path)
    info = os.statvfs(path)
    return info.f_frsize*info.f_blocks

def disk_free(target_path):
    """
    Find the amount of space free on a given path
    Path must exist.
    This method does not take into account quotas

    returns the size in bytes potentially available
    to a non privileged user
    """
    path = getmount(target_path)
    info = os.statvfs(path)
    return info.f_frsize*info.f_bavail

def directory_size(path):
    """
    Find the size of all files in a directory, recursively

    Returns the size in bytes on success
    """
    from os.path import join, getsize
    result = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            try:
                sz = getsize(join(root,name))
                result = result + sz
            except OSError, exc:
                pass
    return result
