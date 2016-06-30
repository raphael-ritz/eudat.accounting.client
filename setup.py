# -*- coding: utf-8 -*-
"""\
=======================
eudat.accounting.client
=======================

Upload accounting records to an eudat accounting server
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup, find_packages
import os, sys

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),('CHANGES.rst',))]
    )
dev_require = []
if sys.version_info < (2, 7):
    dev_require += ['unittest2']


setup(name='eudat.accounting.client',
      version=version,
      description="Upload accounting records to an eudat accounting server",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
          ],
      keywords='',  # FIXME: Add whatefer fits
      author='Raphael Ritz',
      author_email='raphael.ritz@gmail.com',
      url='http://pypi.python.org/pypi/eudat.accounting.client',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['eudat', 'eudat.accounting'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools',
          'requests',
          ],
      entry_points={
          'console_scripts': ['addRecord=eudat.accounting.client.__main__:main']
          },
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      })
