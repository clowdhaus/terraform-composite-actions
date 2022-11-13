import json
import mmap
import os
import re
from glob import glob


def get_directories():
    """
    Return all Terraform (*.tf) files that contain the `required_version`
      string, but does not contain `wrapper` in the path.
    """

    terraform_files = glob('./**/*.tf', recursive=True)
    directories = []

    for file in terraform_files:
        file_size = os.stat(file)

        if file_size.st_size > 0:
            with open(file, 'rb', 0) as rfile:
                contents = mmap.mmap(rfile.fileno(), 0, access=mmap.ACCESS_READ)
                if contents.find(b'required_version') != -1 and 'wrapper' not in file:
                    directories.append(file)

    return json.dumps([x.replace('/versions.tf', '') for x in directories if not re.match(r'^.+/_', x)])


if __name__ == '__main__':
    print(get_directories())
