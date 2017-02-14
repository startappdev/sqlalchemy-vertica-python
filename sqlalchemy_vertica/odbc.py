from sqlalchemy.connectors.pyodbc import PyODBCConnector

from base import VerticaDialect as BaseVerticaDialect


class VerticaDialect(PyODBCConnector, BaseVerticaDialect):
    driver = 'pyodbc'
