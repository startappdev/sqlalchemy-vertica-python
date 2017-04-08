from __future__ import absolute_import, print_function, division

from .base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass, PyClassHasNoInit
class VerticaDialect(BaseVerticaDialect):
    driver = 'pypyodbc'

    @classmethod
    def dbapi(cls):
        pypyodbc = __import__('pypyodbc')
        return pypyodbc
