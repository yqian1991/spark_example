import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = open(os.path.join(here, 'requirements.txt')).readlines()
requires_test = open(os.path.join(here, 'requirements-test.txt')).readlines()

version = '0.1'

setup(name='python-datascience',
      version=version,
      description='data science',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools_git'],
      test_suite='python-datascience',
      install_requires=requires,
      tests_require=requires_test,
      )
