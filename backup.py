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
    matches = (fnmatch(name, pat) for pat in EXCLUDE)
    for pattern in EXCLUDE_PATTERNS:
        if fnmatch(name, pattern):
            print('Skiping ' + name)
            return
        
    print('Adding ' + tarinfo.name)
    return tarinfo


def make_tgz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar: 
        tar.add(
                source_dir,
                arcname=os.path.basename(source_dir),
                filter=exclude
                )

make_tgz('qpython.tgz', '/sdcard/qpython')