from sqlalchemy.connectors.pyodbc import PyODBCConnector

from base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass
class VerticaDialect(PyODBCConnector, BaseVerticaDialect):
    driver = 'pyodbc'
