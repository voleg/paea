# Description

this is an algorithms runner web service.
It has a user interface allowing to run algorithms implementations.

The service is represented with 3 packages:

* Algos service `./algos`
* Web service `./web`
* UI `./ui`

tools: Python, Javascript, Redis, Elasticsearch, Celery, DRF, React.js, Bootstrap

## Algos service package 

there are 2 parts:

* algos package (an actual algorithms implementations)
* celery app that runs calculation requests using `algos.interface` facade

There is a separate "algos" installable package (tests included), and Celery application that using it. 
Wrapping main functionality in celery app allows to control execution, set time limits and get errors even if some calculation request literally kills python interpreter.

This service package runs under PyPy3, that allows pure python algorithms implementations run faster compared to standard CPython.

## Web service package

also two parts here:

* Django ReST API application
* celery worker that processes calculation results

With django ReST API application user can: 

* create calculation request
* get a list of calculations (with their statuses)
* restart previously created calculation request


the Elasticsearch is used as storage because of ease of integrating to a project, and for demonstration purpose. 
So in this django application i do not use django ORM and models, instead i use Documents and Index to store and interact with data.


## UI package

User interface build with React.JS, Bootstrap 4
it is a simple user interface allowing:

* fire a calculation request of one of tree implemented algorithms
* view calc. request status
* view the result and calculation duration

Being a static JS fronted app to a main web app this service package runs under NGINX.  


# Install

```bash
docker-compose up
``` 

wait all setup and loads. The last thing in log should be loading of UWSGI workers spawned. After that follow http://localhost/ 

Also you could run tests: 

```bash
make test
```

## Elasticsearch note (for Linux Docker host)

You may have to configure `max_map_count` if your docker host is Linux running machine. 

https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

```bash
$ sudo sysctl -w vm.max_map_count=262144
```

# Usage

follow  http://localhost/ 
