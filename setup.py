from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='vct.core',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vct'],
      include_package_data=True,
      zip_safe=False,
      tests_require=['ZODB3', 'transaction'],
      extras_require={
        'zodb': ['ZODB3', 'transaction']
      },
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.interface',
          'colander',
          'deform',
          # -*- Extra requirements: -*-
      ],
      # -*- Entry points: -*-
      entry_points="""
      [console_scripts]
      start = vct.core.xmlrpc:start
      """
      )
