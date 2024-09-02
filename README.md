

## Description

ALU-AirBnB represents a full-stack Web application developed from scratch consisting of command interpreter, Web interface, API, and DB. The goal of the project is to build a replica of the [Airbnb Website](https://www. airbnb. com/ And then this application should be run on a server. The project is developed in Python HTML/ CSS Javascript with database support in MySQL and SQLAlchemy. The final version of this project will have:The final version of this project will have:

- A Command line interface for processing data, this is similar to shell for the development and debugging of applications.
- Web Application that may include static and dynamic features of a website’s front-end.
- The other is creation of a comprehensive database to facilitate the management of backend functionalities.
- An API, which gives the front end of the system control over the back end of the application to retrieve data and to post information.


## Files and Directories
- >[```models```](. /models/) folder will contain all the class used in the entire project. In an OOP project, a class referred to as “model” is an abstraction, and describes an object/instance.
- >[```tests```](. /tests) folder will include all the unit tests.
- The [```console. py```](. /console. py) is the chief script of the command interpreter.
- The general architecture of models is cultivated in the [```models/base_model. py```](. /models/base_model. py) file and it is the base for all models. It contains common elements:
- attributes: As it can be seen there are ```id```, ```created_at”, and ```updated_at”.
- methods: ```save()``` as well as the ```to_json()``` method
- > [```models/engine```](/models/engine/) folder stores all storage classes (that have the same prototype). Currently, it contains: ```file_storage. py``` file.


### Interactive mode (example)

```bash
$ . /console. py
(hbnb) help
Documented commands (type help <topic>):Documented commands (type help <topic>):
========================================
All EOF create destroy help q quit show update
(hbnb)
(hbnb)
(hbnb) quit
$
```

## Tests

Tests for this project are written in the [tests](. /tests)
directory. To run the entire test suite simultaneously, execute the following command:To run the entire test suite simultaneously, execute the following command:

```
To run all the tests I simply open the terminal and type the following command $ python3 -m unit test discover tests
```

Alternatively, you can specify a single test file to run at a time:Alternatively, you can specify a single test file to run at a time:

```
And when I run the task below, it should execute the unittest. py file within the test_models directory which contains the Base model test file:py
```



""""
## OWNER & GITHUB
Byusa M Martin De Poles "https://github.com/BYUSAA3
