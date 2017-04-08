from __future__ import absolute_import, print_function, division

from .base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass, PyClassHasNoInit
class VerticaDialect(BaseVerticaDialect):
    driver = 'vertica_python'

    @classmethod
    def dbapi(cls):
        vertica_python = __import__('vertica_python')
        return vertica_python
