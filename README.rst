sqlalchemy-vertica-python
=========================

Vertica dialect for sqlalchemy. Forked from the `Vertica ODBC dialect <https://pypi.python.org/pypi/vertica-sqlalchemy>`_.

This module implements a Vertica dialect for SQLAlchemy using `vertica-python <https://github.com/uber/vertica-python>`_. Engine creation: 

.. code-block:: python

    import sqlalchemy as sa
    sa.create_engine('vertica+vertica_python://user:pwd@host:port/database')

Installation
------------

From PyPI: ::

     pip install sqlalchemy-vertica-python

From git: ::

     git clone https://github.com/LocusEnergy/vertica-sqlalchemy 
     cd vertica-sqlalchemy
     python setup.py install