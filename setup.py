import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mysql-rds',
    version='0.3.1',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='Mozilla Public License 2.0 (MPL 2.0)',
    description='',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/cramshaw/django-mysql-rds',
    author='Chris Ramshaw',
    author_email='chris.ramshaw@nanoporetech.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
)
