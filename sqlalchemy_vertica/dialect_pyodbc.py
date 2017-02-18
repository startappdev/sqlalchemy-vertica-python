from __future__ import absolute_import

from sqlalchemy.connectors.pyodbc import PyODBCConnector

from .base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass, PyClassHasNoInit
class VerticaDialect(PyODBCConnector, BaseVerticaDialect):
    pass
