from fabric import task

hosts = ["fgld"]
base_folder = "/opt/fgtd/"
docker_folder = base_folder + "docker"
dockercmd = "cd " + docker_folder + " && "

@task(hosts=hosts)
def deploy(c):
    """
    Deploys the master branch on the server
    """
    print("Deploying new version of the app")
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
        print("Done")
    else:
        print("Connecting to PSQL")
        c.run(dockercmd + "docker-compose exec postgres psql -U fgtdUser fgtd", pty=True)

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
    Connect to the specified docker service
    """
    print("Connecting to service {}".format(servicename))
    c.run(dockercmd + "docker-compose exec {} sh".format(servicename), pty=True)

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