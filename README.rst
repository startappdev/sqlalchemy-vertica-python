sqlalchemy-vertica
==================

Vertica dialect for sqlalchemy.

Forked from the `Vertica dialect for sqlalchemy using vertica-python <https://pypi.python
.org/pypi/sqlalchemy-vertica-python>`_.

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

