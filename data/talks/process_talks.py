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


def to_yaml(talk_data):
    pass


def load_talks(json_data):
    import ipdb; ipdb.set_trace()


def old_code():
    for talk_id in TALK_IDS:
        # Hopefully, means it's a papercall ID
        needed_details = None
        for talk_details in JSON_DATA:
            if talk_details['title'] == talk_title:
                needed_details = talk_details
                break  # break only inner loop?
        if not needed_details:
            print(('Cannot find details for talk [' + talk_id + '] = ' + talk_title))
            continue
        # print('details found,')
        # print(needed_details)

        # Step 6: Fill data in YAML file
        filename = str(talk_id) + '.yaml'
        talk_tags = needed_details.get('tags', [])
        for tag in BANNED_TAGS:
            try:
                talk_tags.remove(tag)
            except ValueError:
                pass  # if not found, don't worry
        FULL_TAG_LIST.extend(talk_tags)

        context = {
            'name': needed_details.get('name', '').replace('"', "'"),
            'title': needed_details.get('title', '').replace('"', "'"),
            'abstract': needed_details.get('abstract', '').replace('"', "'"),
            'details': needed_details.get('description', '').replace('"', "'"),
            'talk_tags': talk_tags,
        }
        with open(Path(current_folder, filename), 'w') as text_file:
            text_file.write(template.render(context))
        print(('Auto-filled [{}]'.format(filename)))


    print('script over')
    all_tags = set(FULL_TAG_LIST)
    print(('tags = ' + str(all_tags)))
    quit()


if __name__ == "__main__":

    load_talks(JSON_DATA)