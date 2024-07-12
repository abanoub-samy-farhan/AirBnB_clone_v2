from fabric.api import task
from datetime import datetime

@task
def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

