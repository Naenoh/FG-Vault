from fabric import task

hosts = ["fgld"]
base_folder = "/opt/fgld/"
docker_folder = base_folder + "docker"
frontend_folder = base_folder + "frontend"
basecmd = "cd " + base_folder + " && "
dockercmd = "cd " + docker_folder + " && "
frontcmd = "cd " + frontend_folder + " && "

@task(hosts=hosts)
def deploy(c):
    """
    Deploys the master branch on the server
    """
    print("Deploying new version of the app")
    c.run(basecmd + "git pull")
    c.run(frontcmd + "npm run build")
    c.run(dockercmd + "docker-compose down")
    c.run(dockercmd + "docker-compose build")
    c.run(dockercmd + "docker-compose up -d")
    c.run(dockercmd + "docker-compose exec gunicorn python manage.py db upgrade")
    print("Done")

@task(hosts=hosts)
def restart(c):
    """
    Restarts the app
    """
    print("Restarting Docker Containers")
    print("Done")
    c.run(dockercmd + "docker-compose restart")

@task(help={'filename': "Name of the sql file to run"}, hosts=hosts)
def psql(c, filename=""):
    """
    Run the specified SQL file, or open a psql shell if no file is given
    """
    if (filename != ""):
        print("Running SQL script {}".format(filename))
        c.put(filename, remote=base_folder)
        c.run(dockercmd + "docker-compose exec -T postgres psql -U fgtdUser fgtd < " + base_folder + filename, pty=True)
        c.run("rm " + base_folder + filename)
        print("Done")
    else:
        print("Connecting to PSQL")
        c.run(dockercmd + "docker-compose exec -T postgres psql -U fgtdUser fgtd", pty=True)

@task(hosts=hosts)
def ssh(c):
    """
    Connect to the server with SSH
    """
    print("Connecting to VPS")
    c.run("bash", pty=True)

@task(help={'servicename': "Name of the docker service to connect to"}, hosts=hosts)
def service(c, servicename):
    """
    Connect to the specified docker service (super duper bugged rn)
    """
    print("Connecting to service {}".format(servicename))
    c.run(dockercmd + "docker-compose exec -T {} sh".format(servicename), pty=True)

@task(help={'file': "Name of file to dump to"}, hosts=hosts)
def dbdump(c, file="dump.dmp"):
    """
    Dumps the database to the given file (-f), or dump.dmp if none is given
    """
    print("Dumping database contents to file {}".format(file))
    print("Done")

@task(help={'file': "Name of the file to restore from"}, hosts=hosts)
def dbrestore(c, file="dump.dmp"):
    """
    Restore the database from the given file (-f), or dump.dmp if none is given
    """
    print("Restoring database contents from file {}".format(file))
    print("Done")


@task(hosts=hosts)
def test(c):
    c.run('echo $0')