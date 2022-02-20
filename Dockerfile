# Official Python runtime as a parent image
FROM python:3.10.2

# Set default value through ARG, then get the value from from command-line argument
ARG APP_ENV=dev
ENV APP_ENV ${APP_ENV}

# Ensure Python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root
RUN mkdir /wordle-cli

# Set the working directory
WORKDIR /wordle-cli

# Load only requirements and install
ADD ./requirements /wordle-cli/requirements
RUN pip install -r /wordle-cli/requirements/${APP_ENV}.txt

# Load the current directory contents into the container at WORKDIR
ADD . /wordle-cli

ENTRYPOINT ["python", "./wordle-cli/game.py"]