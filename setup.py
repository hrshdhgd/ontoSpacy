from setuptools import setup, find_packages

NAME = 'ontoSpacy'
URL = 'https://github.com/hrshdhgd/ontoSpacy'
AUTHOR = 'Harshad Hegde'
EMAIL = 'hhegde@lbl.gov'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.0.1'
LICENSE = 'BSD'

#with open("requirements.txt", "r") as FH:
#    REQUIREMENTS = FH.readlines()

EXTRAS = {}

setup(

    name=NAME,
    author=AUTHOR,
    version=VERSION,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=LICENSE,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    #install_requires=[r for r in REQUIREMENTS if not r.startswith("#")],
    extras_require=EXTRAS,
    include_package_data=True,
    # add package dependencies
    install_requires=[
        'spacy'
    ],
)