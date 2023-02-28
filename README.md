# Constellations API made in Flask

### Endpoints:
1. __GET all constellations:__ /api/v1/constellations
```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars/1'
```

2. __POST add new constellation(s):__ /api/v1/constellations
```
curl --location 'http://127.0.0.1:5000/api/v1/constellations' \
--header 'Content-Type: application/json' \
--data '[
    {
        "name": "Andromeda",
        "abbr": "And",
        "right_ascension": "00h 40m to 02h 50m",
        "stars": [
            {
                "name": "Alpheratz"
            },
            {
                "name": "Mirach"
            },
            {
                "name": "Adhil"
            }
        ]
    }
]'
```

3. __GET a constellation by id:__ /api/v1/constellation/<<int:constellation_id>>
```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/5'
```

4. __PUT updated a constellation by id:__ /api/v1/constellation/<<int:constellation_id>>
```
curl --location --request PUT 'http://127.0.0.1:5000/api/v1/constellation/1' \
--header 'Content-Type: application/json' \
--data '{
        "name": "Andromeda333",
        "abbr": "And",
        "right_ascension": "00h 40m to 02h 50m",
        "stars": [
            {
                "name": "Alpheratz22"
            },
            {
                "name": "Mirach"
            },
            {
                "name": "Adhil"
            }
        ]
    }'
```

5. __DELETE one single constellations by id:__ /api/v1/constellation/<<int:constellation_id>>
```
curl --location --request DELETE 'http://127.0.0.1:5000/api/v1/constellation/1'
```

6. __GET all stars from one single constellation by id:__ /api/v1/constellation/<<int:constellation_id>>/stars
```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars'
```

7. __GET one single star by id from a constellation:__ /api/v1/constellation/<<int:constellation_id>>/stars/<<int:star_id>>
```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars/1'
```

### Setup local DB.
For this project is used a sqlite data base. To create de DB we use flask_migrate, run:
```
    flask db init
    flask db migrate
    flask db upgrade
```