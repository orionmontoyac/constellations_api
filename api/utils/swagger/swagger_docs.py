import yaml
from os.path import join, dirname


BASE_DIRECTORY = dirname(__file__)

with open(join(BASE_DIRECTORY, 'home.yaml'), 'r') as file:
    # Load the YAML data
    HOME_DOCS = yaml.safe_load(file)

HOME_GET_DOCS = HOME_DOCS['home_get']

with open(join(BASE_DIRECTORY, 'health_check.yaml'), 'r') as file:
    # Load the YAML data
    HEALTH_CHECK = yaml.safe_load(file)

HEALTH_CHECK_GET_DOCS = HEALTH_CHECK['health_check_get']

with open(join(BASE_DIRECTORY, 'constellations_list.yaml'), 'r') as file:
    # Load the YAML data
    CONSTELLATIONS_LIST_DOCS = yaml.safe_load(file)

CONSTELLATIONS_LIST_GET_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_get']
CONSTELLATIONS_LIST_POST_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_post']

with open(join(BASE_DIRECTORY, 'constellation.yaml'), 'r') as file:
    # Load the YAML data
    CONSTELLATION_DOCS = yaml.safe_load(file)

CONSTELLATION_GET_DOCS = CONSTELLATION_DOCS['constellation_get']
CONSTELLATION_PUT_DOCS = CONSTELLATION_DOCS['constellation_put']
CONSTELLATION_DELETE_DOCS = CONSTELLATION_DOCS['constellation_delete']

with open(join(BASE_DIRECTORY, 'stars.yaml'), 'r') as file:
    # Load the YAML data
    STARS_DOCS = yaml.safe_load(file)

STAR_LIST_GET_DOCS = STARS_DOCS['star_list_get']
STAR_GET_DOCS = STARS_DOCS['star_get']
