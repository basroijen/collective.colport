from setuptools import setup, find_packages

version = '0.2'

setup(name='collective.colport',
      version=version,
      description="Export a collection as CSV",
      long_description=open("README.txt").read() + "\n\n" +
                        open('docs/HISTORY.txt').read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone collection csv',
      author='Bas Roijen',
      author_email='bas.roijen@cofely-gdfsuez.nl',
      url='http://cofely-experts.info',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
