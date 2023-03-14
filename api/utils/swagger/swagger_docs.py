import yaml
from pathlib import Path

HOME_DOCS = yaml.safe_load(Path('api/utils/swagger/home.yaml').read_text())
HOME_GET_DOCS = HOME_DOCS['home_get']

HEALTH_CHECK = yaml.safe_load(Path('api/utils/swagger/health_check.yaml').read_text())
HEALTH_CHECK_GET_DOCS = HEALTH_CHECK['health_check_get']

CONSTELLATIONS_LIST_DOCS = yaml.safe_load(Path('api/utils/swagger/constellations_list.yaml').read_text())
CONSTELLATIONS_LIST_GET_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_get']
CONSTELLATIONS_LIST_POST_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_post']

CONSTELLATION_DOCS = yaml.safe_load(Path('api/utils/swagger/constellation.yaml').read_text())
CONSTELLATION_GET_DOCS = CONSTELLATION_DOCS['constellation_get']
CONSTELLATION_PUT_DOCS = CONSTELLATION_DOCS['constellation_put']
CONSTELLATION_DELETE_DOCS = CONSTELLATION_DOCS['constellation_delete']

STARS_DOCS = yaml.safe_load(Path('api/utils/swagger/stars.yaml').read_text())
STAR_LIST_GET_DOCS = STARS_DOCS['star_list_get']
STAR_GET_DOCS = STARS_DOCS['star_get']
