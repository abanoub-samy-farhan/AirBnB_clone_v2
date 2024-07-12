from fabric.api import local
from datetime import datetime

def do_pack():
    local("mkdir -p versions")
    now = datetime.now()
    formatted_time = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(formatted_time)
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path

