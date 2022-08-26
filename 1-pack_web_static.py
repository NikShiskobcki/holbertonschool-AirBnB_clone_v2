#!/usr/bin/python3
"""script generates a tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Task 1"""
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    local('mkdir -p versions')
    file = 'versions/web_static_{}.tgz'.format(time)
    file_ = local('tar -czvf {} web_static'.format(file))
    if file_.failed:
        return None
    else:
        return file
