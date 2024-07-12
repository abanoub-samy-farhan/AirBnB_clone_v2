from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<web-01 IP>', '<web-02 IP>']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/" + archive_no_ext

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}/".format(archive_name, path_no_ext))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}/web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_ext))
        return True
    except Exception as e:
        return False

