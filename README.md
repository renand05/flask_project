# Flask Api Project 
The goal of this project is to demonstrate a possible solution of the take-home-task given by addi.

## Solution

This API was developed in order to demonstrate how to solve the proposed challenge. The idea followed to solve the task was to develop an API in flask in which customers are created and then through a worker execute the validations needed for KYC purposes. The idea with this approach is to separate the creation of customers from further validations. In this way, we keep api calls fast and we left the complexity of handling request to an external service that will have that as its own responsibility.

### Interact with API

In the following link (https://go.postman.co/workspace/My-Workspace~0a361f66-acb4-4877-83b8-9df6e54a8679/collection/12756371-8203d252-4ed5-47c2-a7da-94014cae3f5c) you can check how to interact with the api and create customers that will be then validated.

## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Format](#format)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/renand05/flask_project.git
$ cd <my-project-name>
```

Then install dependencies and check that it works

```bash
$ make server.install      # Install the pip dependencies on the docker container
$ make server.start        # Run the container containing your local python server
```

The API runs locally on docker containers. You can easily change the python version you are willing to use [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/docker-compose.yml#L4), by fetching a docker image of the python version you want.

## Commands

You can display availables make commands using `make`.

While developing, you will probably rely mostly on `make server.start`; however, there are additional scripts at your disposal:

| `make <script>`      | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `server.install`     | Install the pip dependencies on the server's container.                      |
| `server.start`       | Run your local server in its own docker container.                           |
| `server.upgrade`     | Upgrade pip packages interactively.                                          |
| `database.connect`   | Connect to your docker database.                                             |
| `database.init`      | Connect to your docker database.                                             |
| `database.migrate`   | Generate a database migration file using alembic, based on your model files. |
| `database.upgrade`   | Run the migrations until your database is up to date.                        |
| `database.downgrade` | Downgrade your database by one migration.                                    |
| `test`               | Run unit tests with pytest in its own container.                             |
| `format.black`       | Format python files using Black.                                             |
| `format.isort`       | Order python imports using isort.                                            |

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :

```bash
$ make database.connect
```

In order to create migrations in the docker postgres yo must run the following commands:

```bash
$ make database.init
$ make database.migrate
$ make database.upgrade
```

In this way migrations will be generated by the container, it may possible that you can only edit it via `sudo` or by running `chown` on the generated file.

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── migrations               		# Database's migrations settings
├── app                      		# Application source code
│   ├── common               		# Python common packages in the app
│   │   ├── constants.py     		# Constants RegEx used in the app
│   │   └── exceptions.py    		# list of exceptions used in the app
│   ├── customers            		# Python api methods for customers
│   │   └── api_v1_0         		# customer v1 api 
│   |   |      └── __init__.py
│   │   │      └── resources.py         # Python Customer v1 resources
│   │   │      └── tasks.py             # Python tasks connection 
│   ├̣̣────── models.py                   # Python SqlAlchemy models 
│   ├── ext.py        			# Instantiation of database
├── config            			# Project configuration settings
└── docker              		# Project docker configuration
└── makefiles              		# Project shell scripts  
└── requirements              		# Python dependencies requirements 
└── worker              		# Tasks worker code
└── tests              			# Unit tests source code
└── entrypoint.py              		# application entrypoint
└── manage.py              		# cli commands to manipulate app
```

## Development

To develop locally, execute:

```bash
$ make server.start           # Create the containers containing your python server in your terminal
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./app/` or in `./worker/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can add objects in your database that will only be used in your tests, see example.
You can run your tests in their own container with the command:

```bash
$ make test
```

## Format

The code is formatted using [Black](https://github.com/python/black) and [Isort](https://pypi.org/project/isort/). You have the following commands to your disposal:

```bash
$ make format.black # Apply Black on every file
$ make format.isort # Apply Isort on every file
```


