# MENLOBEN SUPERMARKET
![Landing Page](https://github.com/leyeseyi/menloben-supermarket/blob/main/screeshots/Welcome%20Page.png?raw=true)

A new digitally enabled inventory application for stores to manage products. This application performs the following:

1. User authentication (store-keeper / manager)
![Login Page](https://github.com/leyeseyi/menloben-supermarket/blob/main/screeshots/Login%20Page.png?raw=true)
2. Allows store-keeper / shop managers to add new products, delete products and edit quantity of exisiting products.
![Add Product](https://github.com/leyeseyi/menloben-supermarket/blob/main/screeshots/New%20Product%20Page.png?raw=true)
3. Allows the shop managers to notify the supplier through SMS using the Vonage API.
![Dashboard](https://github.com/leyeseyi/menloben-supermarket/blob/main/screeshots/Items%20Dashboard.png?raw=true)

# Getting Started

### Installing Dependencies

#### Python 3.10.1

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `root` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. 


## Running the server

From within the `./menloben-supermarket` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

For Mac Users
```bash
export FLASK_APP=run.py;
```

For Windows users
```bash
set FLASK_APP=run.py;
```
To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.