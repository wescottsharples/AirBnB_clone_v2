#!/usr/bin/python3
"""
    Fabric script generates a .tgz archinve from the contents of
    the web_static folder of AirBnB Clone repo, using the function
    do_pack.
"""

import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """generates an .tgz archive from web_static folder"""

    try:
        name = "web_static_" + datetime.utcnow().strftime("%Y%m%d%H%M%s") + ".tgz"
        local("mkdir -p versions")
        path = "versions/{}".format(name)
        local("tar -cfvz {} web_static".format(path))
        return path
    except:
        return None
