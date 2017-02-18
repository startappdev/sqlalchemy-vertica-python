from __future__ import absolute_import
from .base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass, PyClassHasNoInit
class VerticaDialect(BaseVerticaDialect):
    driver = 'vertica_python'

    @classmethod
    def dbapi(cls):
        vertica_python = __import__('vertica_python')
        dbapi_errors = ['Warning', 'Error', 'InterfaceError', 'DatabaseError', 'DataError',
                        'OperationalError', 'IntegrityError', 'InternalError', 'ProgrammingError',
                        'NotSupportedError']
        for error in dbapi_errors:
            if not hasattr(vertica_python, error):
                setattr(vertica_python, error, getattr(vertica_python.errors, error))

        return vertica_python
