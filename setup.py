from setuptools import setup, find_packages
import sys, os

version = '1.0.5'

setup(name="holland",
      version=version,
      description="Holland Core Plugins",
      long_description="""\
      These are the plugins required for basic Holland functionality.
      """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords="",
      author="Rackspace",
      author_email="holland-devel@googlegroups.com",
      url='http://www.hollandbackup.org/',
      license="3-Clause BSD",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=True,
      test_suite='tests',
      install_requires=[
        # 'configobj' # currently this is bundled internally
      ],
      namespace_packages=['holland', 'holland.backup', 'holland.lib',
                          'holland.commands', 'holland.cli'],
      )
