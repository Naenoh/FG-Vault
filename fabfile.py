from fabric import task

hosts = ["fgld"]
base_folder = "/opt/fgld/"
docker_folder = base_folder + "docker"
frontend_folder = base_folder + "frontend"
basecmd = "cd " + base_folder + " && "
dockercmd = "cd " + docker_folder + " && "
frontcmd = "cd " + frontend_folder + " && "

@task(hosts=hosts)
def deploy(c, frontend=False, backend=False, migrate=False):
    """
    Deploys the master branch on the server
    """
    print("Deploying new version of the app")
    if frontend or backend or migrate:
        c.run(basecmd + "git pull")
    if frontend:
        c.run(frontcmd + "npm run build")
    if backend:
        c.run(dockercmd + "sudo docker-compose up -d --build")
    if migrate:
        c.run(dockercmd + "sudo docker-compose exec gunicorn python manage.py db upgrade", pty=True)
    print("Done")

@task(hosts=hosts)
def restart(c):
    """
    Restarts the app
    """
    print("Restarting Docker Containers")
    c.run(dockercmd + "sudo docker-compose restart")
    print("Done")

@task(help={'filename': "Name of the sql file to run"}, hosts=hosts)
def psql(c, filename=""):
    """
    Run the specified SQL file, or open a psql shell if no file is given
    """
    if (filename != ""):
        print("Running SQL script {}".format(filename))
        c.put(filename, remote=base_folder)
        c.run(dockercmd + "sudo docker-compose exec -T postgres bash -c 'psql -U \"$POSTGRES_USER\" \"$POSTGRES_DB\"' < " + base_folder + filename.split("/")[-1], pty=True)
        c.run("rm " + base_folder + filename.split("/")[-1])
        print("Done")
    else:
        print("Connecting to PSQL")
        c.run(dockercmd + "sudo docker-compose exec postgres bash -c 'psql -U \"$POSTGRES_USER\" \"$POSTGRES_DB\"'", pty=True)

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
    c.run(dockercmd + "sudo docker-compose exec -T {} sh".format(servicename), pty=True)

@task(help={'file': "Name of file to dump to"}, hosts=hosts)
def dbdump(c, file="dump.dmp"):
    """
    Dumps the database to the given file (-f), or dump.dmp if none is given
    """
    print("Dumping database contents to file {}".format(file))
    c.run(dockercmd + "sudo docker-compose exec postgres pg_dump -Fc -U fgtdUser -f /usr/share/dumps/{} fgtd".format(file), pty=True)
    c.get("/home/fgld/dumps/{}".format(file))
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
    c.run(dockercmd + "sudo docker-compose exec -T postgres echo \"$POSTGRES_DB\"")