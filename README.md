Description
====================

Wordle game in the terminal with Python 3 

Usage
============================

Installation
----------------

This project was created with docker, to learn more about docker: https://www.docker.com/get-started 

```bash
cd yourProjectFolder
git clone https://github.com/Chayemor/wordle-cli.git
```

With this step done you have successfully cloned the repo. Now before running with docker-compose it's 
important to set up the .env variables that docker needs.

Set up
-----------------

There's a file with the name .env_template, copy the file and rename to .env and fill out with desired 
data or leave example data. It's the names of the variables in there that are important, the actual values you write are not.

```bash
cd wordle-cli
cp .env_template .env
```

The variable names are self explanatory to their function. If you feel like playing with the code, it's best then to set the .env variable
**APP_ENV** to "dev" (without double quotes). By default, .env_template has that value set to dev, that way
if an error occurs, you will get more information about it. You can just as easily set it to prod. 

Run
-----------------

Assuming you are in the repository folder, all that's left to do is build the docker container, then run it. Note: You must be running Python 3 when you do the docker commands.
 
```bash
docker-compose build
docker-compose run --rm wordle-cli
```

That's it. Have fun playing!

Running Tests
============================

To run tests you must be inside the running container labeled **wordle-cli**. 
To log into the docker container take a look at **Common Docker commands --> Log into a docker container**.


```bash
python test the_app_name.route.to.test.file
```

You should look for the following output:

```bash
root@115f46c7f03e:/django-docker# python test users.tests.tests
......
----------------------------------------------------------------------
Ran 6 tests in 12.621s

OK
Destroying test database for alias 'default'...
```

Search for the **OK** which means all tests have passed. You can find the numerous test over
at each app's directory under tests.

Common Docker commands
============================

## View running containers 

```bash
docker ps
```
```bash 
CONTAINER ID        IMAGE                            COMMAND                  CREATED             STATUS              PORTS                    NAMES
115f46c7f03e        cmr_service_web                  "bash /entrypoint.sh"    2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   cmr_service
603f6d1c9db7        postgres:9.6                     "docker-entrypoint.s…"   4 days ago          Up 2 hours          0.0.0.0:5432->5432/tcp   cmr_service_postgres_1
```

You should get something like this. The last column, **NAMES** are the names of the running containers. If you ever want to log into one, you need that name. The 
**cmr_service** contains the actual code for the API, while the **cmr_service_postgres_1** is the container that holds the database itself. If you want to be
able to log into Postgres, you'd log into that container, and not **cmr_service**.

## Log into a docker container

```bash
docker exec -it docker_container_name bash
```

Example: **wordle-cli**

```bash
docker exec -it wordle-cli bash
```

Once logged in, if you do a simple ```ls``` you'd see the following:

```bash
root@115f46c7f03e:/django-docker# ls
Dockerfile  README.md 
```

## Start a container without a rebuild
Assuming you are in the same path as the root repo.

```bash
docker-compose up
```

## Force build of a container 
Assuming you are in the same path as the root repo.

```bash
docker-compose build --no-cache
```

## Kill everything
Something has gone awfully wrong and you need to do a mission abort, obliterating all
containers and images. Proceed with caution.

```bash
docker system prune
```