#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['75.101.241.158', '34.229.138.135']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Task 2"""
    if (exists(archive_path) is False):
        return False

    archive_name = archive_path.split('/')[-1]
    my_folder = archive_name.split('.')[0]
    releases_path = "/data/web_static/releases/{0}/".format(my_folder)
    archive_remote_path = "/tmp/{0}".format(archive_name)

    put(archive_path, archive_remote_path)
    run("mkdir -p {}".format(releases_path))
    run("tar -zxf {0} -C {1}".format(archive_remote_path,
                                     releases_path))
    run("rm {0}".format(archive_remote_path))
    run("mv -f {}web_static/* {}".format(releases_path, releases_path))
    run("rm -rf {}web_static".format(releases_path))
    run("ln -fs {0} /data/web_static/current".format(releases_path))
    return True


def deploy():
    """Task 3"""
    file = do_pack()
    if file is False:
        return False
    return do_deploy(file)
