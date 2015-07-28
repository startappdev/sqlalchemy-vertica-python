sqlalchemy-vertica-python
=========================

Vertica dialect for sqlalchemy.

This module implements a Vertica dialect for SQLAlchemy using `vertica-python <https://github.com/uber/vertica-python>`. Engine creation: 

.. code-block:: python

    import sqlalchemy as sa
    sa.create_engine('vertica+vertica_python://user:pwd@host:port/database')

Installation
------------

From git: ::

     git clone https://github.com/LocusEnergy/vertica-sqlalchemy 
     cd vertica-sqlalchemy
     python setup.py install
