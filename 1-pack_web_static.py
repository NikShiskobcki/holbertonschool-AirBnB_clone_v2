#!/usr/bin/python3
"""Fabric script that generates.tgz archive from contents of web_static"""
from datetime import datetime
from fabric.api import run, local


def do_pack():
    """function for tgz archive"""
    try:
        local('mkdir -p versions')
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = "versions/web_static_" + time + ".tgz"
        local("tar -cvzf" + filepath + " web_static")
        return filepath
    except Exception:
        return None
