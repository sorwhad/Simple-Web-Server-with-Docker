### Description 
This is a simple realisation of a web-server. There are three services in total: the database, the database filling script and the web-server, each one being containerized with Docker. 

### How to use it?
* To populate the database put a data.csv file inside the bd-filler directory 
* To build the web-server type inside the base directory of the project
```
docker-compose up -d
```
* After completeing the building process open https://localhost:8000 to see the database contents 
