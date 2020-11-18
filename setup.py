from setuptools import setup, find_packages
from bugyocloudclient import __version__ as version

package_name = 'bugyocloudclient'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name=version.__title__,
    version=version.__version__,
    author=version.__author__,
    description=version.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=version.__url__,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    # test_suites='tests',
)
