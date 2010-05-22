from setuptools import setup, find_packages

version = '0.9.9'

setup(name='holland.lib.lvm',
      version=version,
      description="LVM support",
      long_description="""\
      """,
      keywords='holland lib lvm',
      author='Rackspace',
      author_email='holland-devel@googlegroups.com',
      url='http://www.hollandbackup.org/',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=True,
      namespace_packages=['holland','holland.lib']
)