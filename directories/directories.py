import json
import re
from glob import glob


def get_directories():
    """Get the directories that contain files that match the pattern specified"""
    versions = glob('./**/versions.tf', recursive=True)
    providers =  glob('./**/providers.tf', recursive=True)
    patterns = versions + providers

    return json.dumps([x.replace('/versions.tf', '') for x in patterns if not re.match(r'^.+/_', x) and 'wrapper' not in x])


if __name__ == '__main__':
    print(get_directories())
