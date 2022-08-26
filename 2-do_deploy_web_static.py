#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from os.path import exists
from fabric.api import put, run, env
env.hosts = ['75.101.241.158', '34.229.138.135']
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        noExtension = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExtension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, noExtension))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExtension))
        run('rm -rf {}{}/web_static'.format(path, noExtension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExtension))
        return True
    except Exception:
        return False
