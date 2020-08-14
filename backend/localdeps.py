import os.path

from typing import List
from collections import OrderedDict


def read_requirements(filename: str):
    """Reads the contents of the specified requirements.txt file and recurses
    into dependent requirements file, thus returning a flat list of
    dependencies.

    This also fixes a problem with editable dependencies which Pip
    usually resolves relative to the current directory instead of
    relative to the requirements file in which it was declared.
    """

    directory = os.path.dirname(os.path.abspath(filename))

    with open(filename, 'r') as fp:
        entries = fp.readlines()

    packages: List[str] = []

    for entry in entries:
        # ignore comments and blank lines
        entry = entry.strip()
        if not entry or entry.startswith('#'):
            continue

        packages.append(entry)

    return packages
