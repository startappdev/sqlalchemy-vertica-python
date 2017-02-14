from setuptools import setup

with open("README.rst", "r") as f:
    description = f.read()

VERSION = '0.2.1'

setup(
    name='sqlalchemy-vertica',
    version=VERSION,
    description='Vertica dialect for sqlalchemy',
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
        'sqlalchemy >= 1.1.5',
        'psycopg2 >= 2.6.2',
        'pyodbc >= 3.0.10',
        'vertica-python >= 0.6.13',
    ],
    entry_points="""
    [sqlalchemy.dialects]
    vertica.pyodbc = sqlalchemy_vertica.odbc:VerticaDialect
    vertica.vertica_python = sqlalchemy_vertica.vp:VerticaDialect
    """,
)
