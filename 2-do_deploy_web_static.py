#!/usr/bin/python3
"""contains do_pack and do_deploy functions"""
from fabric.api import *

env.hosts = ["34.73.145.109", "35.196.46.86"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """generates an .tgz archive from web_static folder"""

    name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        local("mkdir -p versions")
        path = "versions/{}".format(name)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to my web servers"""

    if not archive_path:
        return False

    try:
        filename = archive_path.split('/')[-1]
        name = filename.split('.')[0]
        path = "/data/web_static/releases/{}/".format(name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current")
        return True
    except:
        return False
