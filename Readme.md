# Description

this is an algorithms runner web service.
It has a user interface allowing to run algorithms implementations.

The service is represented with 3 packages:

* Algos service `./algos`
* Web service `./web`
* UI `./ui`


## Algos service package 

there are 2 parts:

* algos package (an actual algorithms implementations)
* celery app that runs calculation requests using `algos.interface` facade

Wrapping main functionality in celery task allows to control execution, set time limits and get errors even if some calculation request literally kills python interpreter.


## Web service package

also two parts here:

* Django ReST API application
* celery worker that processes calculation results

With django ReST API application user can: 

* create calculation request
* get a list of calculations (with their statuses)
* restart previously created calculation request


the Elasticsearch is used as storage because of ease of integrating to a project, and for demonstration purpose.


## UI package

User interface build with React.JS, Bootstrap 4
it is a simple user interface allowing:

* fire a calculation request of one of tree implemented algorithms
* view calc. request status
* view the result and calculation duration


# Install

``` 
docker-compose up -d 
``` 

## Elasticsearch note

You may have to configure `max_map_count` on docker host

https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

```
$ sudo sysctl -w vm.max_map_count=262144
```

# Usage

follow  http://localhost/ 
