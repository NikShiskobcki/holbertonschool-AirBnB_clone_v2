#!/usr/bin/python3
"""fabric script that distributes archive to web servers"""

from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['54.167.116.248', '50.17.74.91']


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


def deploy():
    """deploys page"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
