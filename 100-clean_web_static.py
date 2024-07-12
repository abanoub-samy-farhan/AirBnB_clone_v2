from fabric.api import run, local, env

env.hosts = ['<web-01 IP>', '<web-02 IP>']

def do_clean(number=0):
    number = int(number)
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -f".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number))


