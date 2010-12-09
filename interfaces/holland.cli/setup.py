from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='holland.cli',
    version='0.1',
    description='Holland CLI interface',
    classifiers=[], 
    keywords='',
    author='Rackspace',
    author_email='holland-coredev@lists.launchpad.net',
    url='http://hollandbackup.org',
    license='GNU GPLv2',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "configobj",
        # remove if not using genshi templating
        "genshi",
        "cement >=0.8.12, <0.9",
        "holland >= 1.0.5",
        ],
    setup_requires=[
        # uncomment for nose testing
        # "nose",
        ],
    test_suite='nose.collector',
    entry_points="""
    [console_scripts]
    holland = holland.cli.core.appmain:main
    """,
    namespace_packages=[
        'holland',
        'holland.cli', 
        'holland.cli.lib', 
        'holland.cli.bootstrap',
        'holland.cli.controllers',
        'holland.cli.model',
        'holland.cli.helpers',
        'holland.cli.templates',
        ],
    )
