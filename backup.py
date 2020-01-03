#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import tarfile
import os
from fnmatch import fnmatch

#os.chdir('/sdcard')

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
'


def basename(source):
    return os.path.basename(source)

def exclude(tarinfo):
    name = basename(tarinfo.name)
    if [fnmatch(name, pat) for pat in EXCLUDE]:
        print('Skiping {}'.format(name))
        return None
    else:
        print('Adding ' + tarinfo.name)
        return tarinfo


def make_tgz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar: 
        tar.add(
                source_dir,
                arcname=os.path.basename(source_dir),
                filter=exclude
                )

