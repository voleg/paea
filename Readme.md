Description
===========

this is an algorithms runner web service.
It has a user interface that's allows to run algorithms implementations.

The service is represented with 3 packages:

- Algos service 
- Web service
- UI


Algos service 
-------------

there are 2 parts:

- algos package.
- celery app that runs calculation requests using `algos.interface` facade

Wrapping main functionality in celery task allows to control execution, set time limits and get errors even if some calculation request literally kills python interpreter.


Web service
-----------

also two parts here:

- Django ReST API application
- celery worker that processes calculation results

With django ReST API application user can: 

- create calculation request
- get a list of calculations (with their statuses)
- restart previously created calculation request


UI
--
User interface build with React.JS, Bootstrap 4
it is a simple user interface allowing user:

- fire a calculation request of one of tree implemented algorithms
- view calc. request status
- view the result and calculation duration


Install
=======

``` 
docker-compose up -d 
``` 


Elasticsearch note
------------------
You may have to configute `max_map_count`

https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

```
$ sudo sysctl -w vm.max_map_count=262144
```
