from setuptools import setup

with open("README.rst", "r") as f:
    description = f.read()

version_info = (0, 2, 5)
version = '.'.join(map(str, version_info))

setup(
    name='sqlalchemy-vertica',
    version=version,
    description='Vertica dialect for sqlalchemy',
    long_description=description,
    license='MIT',
    url='https://github.com/startappdev/sqlalchemy-vertica',
    download_url='https://github.com/startappdev/sqlalchemy-vertica/tarball/%s' % (version,),
    author='StartApp Inc.',
    author_email='ben.feinstein@startapp.com',
    packages=(
        'sqlalchemy_vertica',
    ),
    install_requires=(
        'six >= 1.10.0',
        'sqlalchemy >= 2.4',
    ),
    extras_require={
        'pyodbc': [
            'pyodbc >= 3.0',
        ],
        'turbodbc': [
            'turbodbc >= 1.0',
            'numpy >= 1.12',
        ],
        'vertica-python': [
            'psycopg2 >= 2.6',
            'vertica-python >= 0.6.14',
        ],
        'pypyodbc': [
            'pypyodbc >= 1.3.4',
        ],
        'hpe-vertica': [
            'hp-vertica-client >= 7',
        ]
    },
    entry_points={
        'sqlalchemy.dialects': [
            'vertica.pyodbc = '
            'sqlalchemy_vertica.dialect_pyodbc:VerticaDialect [pyodbc]',
            'vertica.turbodbc = '
            'sqlalchemy_vertica.dialect_turbodbc:VerticaDialect [turbodbc]',
            'vertica.vertica_python = '
            'sqlalchemy_vertica.dialect_vertica_python:VerticaDialect [vertica-python]',
            'vertica.pypyodbc = '
            'sqlalchemy_vertica.dialect_pypyodbc:VerticaDialect [pypyodbc]',
            'vertica.hpe_vertica = '
            'sqlalchemy_vertica.dialect_hpe_vertica:VerticaDialect [hpe-vertica]',
        ]
    }
)
