from sqlalchemy.connectors.pyodbc import PyODBCConnector

from base import VerticaDialect as BaseVerticaDialect


class TURBODBCConnector(PyODBCConnector):
    driver = 'turbodbc'

    @classmethod
    def dbapi(cls):
        turbodbc = __import__('turbodbc')
        dbapi_errors = ['DataError', 'OperationalError', 'IntegrityError', 'InternalError',
                        'ProgrammingError', 'NotSupportedError']
        for error in dbapi_errors:
            if not hasattr(turbodbc, error):
                setattr(turbodbc, error, turbodbc.DatabaseError)

        return turbodbc

    def _dbapi_version(self):
        return ()


# noinspection PyAbstractClass
class VerticaDialect(TURBODBCConnector, BaseVerticaDialect):
    pass
