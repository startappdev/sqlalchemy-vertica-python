from setuptools import setup

with open("README.rst", "r") as f:
    description = f.read()

version_info = (0, 0, 2)
version = '.'.join(map(str, version_info))

setup(
    name='sqlalchemy-vertica',
    version=version,
    description='Vertica dialect for sqlalchemy',
    long_description=description,
    license='MIT',
    url='https://github.com/lv10/sqlalchemy-vertica',
    download_url='https://github.com/lv10/sqlalchemy-vertica/tarball/%s' % (version,),
    author='Luis Villamarin',
    author_email='luis@lv10.me',
    packages=(
        'sqlalchemy_vertica',
    ),
    install_requires=(
        'six >= 1.10.0',
        'sqlalchemy >= 1.1.11',
    ),
    extras_require={
        'pyodbc': [
            'pyodbc>=4.0.16',
        ],
        'vertica-python': [
            'psycopg2>=2.7.1',
            'vertica-python>=0.7.3',
        ],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'vertica.pyodbc = '
            'sqlalchemy_vertica.dialect_pyodbc:VerticaDialect [pyodbc]',
            'vertica.vertica_python = '
            'sqlalchemy_vertica.dialect_vertica_python:VerticaDialect [vertica-python]',
        ]
    }
)
