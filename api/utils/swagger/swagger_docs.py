import yaml
from pathlib import Path

HOME_DOCS = yaml.safe_load(Path('api/utils/swagger/home.yaml').read_text())

HOME_GET_DOCS = HOME_DOCS['home_get']

CONSTELLATIONS_LIST_DOCS = yaml.safe_load(Path('api/utils/swagger/constellations_list.yaml').read_text())

CONSTELLATIONS_LIST_GET_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_get']
CONSTELLATIONS_LIST_POST_DOCS = CONSTELLATIONS_LIST_DOCS['constellations_list_post']
