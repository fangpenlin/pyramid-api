import os

from setuptools import find_packages
from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm>=1.1.1,<2.0',
    'transaction>=2.0,<2.1',
    'SQLAlchemy',
    'zope.sqlalchemy',
    'waitress',
    'base58',
    'pytz',
    'requests',
    'click',
    'ipython',
    'psycopg2',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'psycopg2',
]

setup(
    name='pyramid_api',
    version='0.0.0',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'tests': tests_require,
    },
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = pyramid_api:main
    [console_scripts]
    pyramid_api = pyramid_api.scripts.__main__:main

    """,
)
