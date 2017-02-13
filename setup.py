from setuptools import setup

with open("README.rst", "r") as f:
    description = f.read()

VERSION = '0.2.0'

setup(
    name='sqlalchemy-vertica',
    version=VERSION,
    description='Vertica dialect for sqlalchemy using vertica_python',
    long_description=description,
    license="MIT",
    url='https://github.com/startappdev/sqlalchemy-vertica',
    download_url='https://github.com/startappdev/sqlalchemy-vertica/tarball/%s' % (VERSION,),
    author='StartApp Inc.',
    author_email='ben.feinstein@startapp.com',
    packages=[
        'sqlalchemy_vertica',
    ],
    install_requires=[
        'psycopg2 >= 2.6.2',
        'sqlalchemy >= 1.1.5',
        'vertica-python >= 0.6.13',
    ],
    entry_points="""
    [sqlalchemy.dialects]
    vertica.vertica_python = sqlalchemy_vertica.base:VerticaDialect
    """,
)
