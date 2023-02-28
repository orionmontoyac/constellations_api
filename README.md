# Constellations API
### Setup local DB.
For this project is used a sqlite data base. To create de DB we use flask_migrate, run:
```
    flask db init
    flask db migrate
    flask db upgrade
```

## Endpoints:
#### GET all contellations: 
https://shrouded-peak-23826.herokuapp.com/api/v1.0/constellations/
#### Get constellation by ID:
https://shrouded-peak-23826.herokuapp.com/api/v1.0/constellations/id
id: from 1 to 88
#### Get star by  constellation ID and Star number:
https://shrouded-peak-23826.herokuapp.com/api/v1.0/constellations/id?star=star_number
id: from 1 to 88
star_number: from 0 to # of constellation's stars