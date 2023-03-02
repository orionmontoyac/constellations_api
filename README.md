# Constellations API made in Flask

### Endpoints:
1. __GET all constellations:__ /api/v1/constellations
<details>
<summary>Example</summary>

```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars/1'
```
</details>

2. __POST add new constellation(s):__ /api/v1/constellations
<details>
<summary>Example</summary>

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
</details>

3. __GET a constellation by id:__ /api/v1/constellation/<<int:constellation_id>>
<details>
<summary>Example</summary>

```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/5'
```
</details>

4. __PUT updated a constellation by id:__ /api/v1/constellation/<<int:constellation_id>>
<details>
<summary>Example</summary>

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
</details>

5. __DELETE one single constellations by id:__ /api/v1/constellation/<<int:constellation_id>>
<details>
<summary>Example</summary>

```
curl --location --request DELETE 'http://127.0.0.1:5000/api/v1/constellation/1'
```
</details>

6. __GET all stars from one single constellation by id:__ /api/v1/constellation/<<int:constellation_id>>/stars
<details>
<summary>Example</summary>

```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars'
```
</details>

7. __GET one single star by id from a constellation:__ /api/v1/constellation/<<int:constellation_id>>/stars/<<int:star_id>>
<details>
<summary>Example</summary>

```
curl --location 'http://127.0.0.1:5000/api/v1/constellation/1/stars/1'
```
</details>

### Unit Testing
```bash
# Run all unit test
pytest -vv 
# Run unit test by folder
pytest -vv test/routes/ 
# Run unit test by file
pytest -vv test/routes/test_constellations.py 
# Run unit test by class
pytest -vv test/routes/test_constellations.py::TestConstellation
# Run unit test by class method
pytest -vv test/routes/test_constellations.py::TestConstellation::test_get_all_constellations_ok
```

### Setup local DB.
For this project is used a sqlite data base. To create de DB we use flask_migrate, run:
```
    flask db init
    flask db migrate
    flask db upgrade
```