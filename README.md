# _Vector.ai Assignment_

## LLD
The basic implementation is that all the requests would be 
handled by a flask application that connects to postgresql to perform
all the CRUD operations, Kafka with Debezium is used inorder
to save the changes of the database into the kafka so that the large
number of requests can be handled by the kafka consumer.


## Tables: 

### continents:
#### id*, name, population, area,


### countries: 
#### id*, name, population, area, total_hospitals, total_national_parks


### cities:
#### id*, name, population, area, total_roads , total_trees

### APIs:

- [GET] /wiki/continents: Fetch the data from Continents table and return to client in json format.
- [POST] /wiki/add/continent: Add the data of a continent to the continent table by sending data in JSON format.
- [PUT] /wiki/update/continent/\<int:id\> : Update the data of the continent table by using ID & sending updated data in JSON format
- [DELETE] /wiki/del/continent/\<int:id\> : Delete the data of the continent table using ID
- [GET] /wiki/countries: Fetch the data from countries table and return to client in json format.
- [POST] /wiki/add/country: Add the data of a country to the country table by sending data in JSON format.
- [PUT] /wiki/update/country/\<int:id\> : Update the data of the country table by using ID & sending updated data in JSON format
- [DELETE] /wiki/del/country/\<int:id\> : Delete the data of the country table using ID
- [GET] /wiki/cities: Fetch the data from cities table and return to client in json format.
- [POST] /wiki/add/continent: Add the data of a city to the city table by sending data in JSON format.
- [PUT] /wiki/update/city/\<int:id\> : Update the data of the city table by using ID & sending updated data in JSON format
- [DELETE] /wiki/del/city/\<int:id\> : Delete the data of the city table using ID
