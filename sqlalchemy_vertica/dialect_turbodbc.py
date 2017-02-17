from base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass
class VerticaDialect(BaseVerticaDialect):
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
