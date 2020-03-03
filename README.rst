sqlalchemy-vertica
==================

Vertica dialect for sqlalchemy.

Forked from the `sqlalchemy-vertica repository <https://github.com/startappdev/sqlalchemy-vertica>`.
Unfortunately, sqlalchemy-vertica was removed from pypi. As of Sept 28, 2018 this version supports
querying views. This is version is not a state of the art, nor does it follow the principles
outlinedb by SQLAlchemy at:https://github.com/zzzeek/sqlalchemy/blob/master/README.dialects.rst.
However, I will slowly start upgrading the code base to meet standards and submit so that it
becomes an external dialect in SQLAlchemy. Anyone interested in helping is welcome to contribute
and/or submit issues/ideas.


.. code-block:: python

    import sqlalchemy as sa
    import urllib
    # for pyodbc connection
    sa.create_engine('vertica+pyodbc:///?odbc_connect=%s' % (urllib.quote('DSN=dsn'),))

    # for turbodbc connection
    sa.create_engine('vertica+turbodbc:///?DSN=dsn')

    # for vertica-python connection
    sa.create_engine('vertica+vertica_python://user:pwd@host:port/database')

Installation
------------

From PyPI: ::

     pip install sqlalchemy-vertica[pyodbc,turbodbc,vertica-python]  # choose the relevant engines

From git: ::

     git clone https://github.com/startappdev/sqlalchemy-vertica
     cd sqlalchemy-vertica
     pip install pyodbc turbodbc vertica-python  # choose the relevant engines
     python setup.py install

