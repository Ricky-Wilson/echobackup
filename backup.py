import tarfile

from os.path import basename
from fnmatch import fnmatch


EXCLUDE = [
    '*.zip',
    '*.tgz',
    '*.pyc',
    '*.txt',
    '*.sh',
    '.last_tmp.py',
    '*__pycache__*',
    '*snippets3*'
]


def exclude(path):
    return any(fnmatch(basename(path), p) for p in EXCLUDE)


def make_tgz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar: 
        tar.add(
            source_dir,
            arcname=basename(source_dir),
            filter=exclude
        )