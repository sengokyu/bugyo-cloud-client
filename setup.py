from os import name, path
from codecs import open
from distutils.core import setup

package_name = 'bugyo-cloud-client'

root_dir = path.abspath(path.dirname(__file__))


def _readfile(filename):
    return [name.rstrip() for name in open(filename).readlines()]


def _requirements():
    return _readfile(path.join(root_dir, 'requirements.txt'))


def _test_requirements():
    return _readfile(path.join(root_dir, 'test-requirements.txt'))
