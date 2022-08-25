#!/usr/bin/python3
"""fabric script that distributes archive to web servers"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['web-01.n1k.tech', 'web-02.n1k.tech']

def do_deploy(archive_path):
    """function to distribute archive"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        return True
    except Exception:
        return False
