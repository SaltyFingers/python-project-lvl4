### Hexlet tests and linter status:
[![Actions Status](https://github.com/SaltyFingers/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/SaltyFingers/python-project-lvl4/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/8d3fe4f6a0732058de10/maintainability)](https://codeclimate.com/github/SaltyFingers/python-project-lvl4/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/8d3fe4f6a0732058de10/test_coverage)](https://codeclimate.com/github/SaltyFingers/python-project-lvl4/test_coverage)

### Description of [Task Manager](https://still-castle-99759.herokuapp.com/):
This is a task manager app. It's allows you to create tasks, statuses, labels and link it to each other, filter tasks. Also you can assign an executor to created task.
To use this app you should register and log in.

### How to install:
To istall an app from GitHub on Your PC use command
    
    pip install git+https://github.com/SaltyFingers/python-project-lvl4

in your terminal.

Create ``.env`` file in main project's directory and create local variable:

    SECRET_KEY='this is your secret key'

Then use command

    pip install -r requirements.txt

to install all dependencies

To run app at local host http://127.0.0.1:8000/ use command:

    make run

