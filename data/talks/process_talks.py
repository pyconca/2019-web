# Download/Format talk information.
# warning this is a python-2 only script.

import json
from pathlib import Path
from jinja2 import FileSystemLoader
from jinja2 import Environment
from talk_ids import TALK_IDS


# Template setup
current_folder = Path(__file__).resolve().parent
jinja_env = Environment(
    loader=FileSystemLoader(str(current_folder)),
)
template = jinja_env.get_template('talk_skeleton.j2')

FULL_TAG_LIST = []

BANNED_TAGS = [
    'fa'
]

# import talk data
JSON_DATA = json.loads(open('../speakers-details.json').read())


def to_yaml(needed_details):
    return {
        'name': needed_details.get('name', '').replace('"', "'"),
        'title': needed_details.get('title', '').replace('"', "'"),
        'abstract': needed_details.get('abstract', '').replace('"', "'"),
        'details': needed_details.get('description', '').replace('"', "'"),
        'talk_tags': ''
    }


def write_template(talk_desc):
    filename = f'{talk_desc["ID"]}.yaml'
    context = to_yaml(talk_desc)
    with open(Path(current_folder, filename), 'w') as text_file:
            text_file.write(template.render(context))
    print(('Auto-filled [{}]'.format(filename)))


if __name__ == "__main__":

    for talk_entry in JSON_DATA:
        write_template(talk_entry)
