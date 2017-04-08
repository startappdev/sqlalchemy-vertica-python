from __future__ import absolute_import, print_function, division

from .base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass, PyClassHasNoInit
class VerticaDialect(BaseVerticaDialect):
    driver = 'hpe_vertica'

    @classmethod
    def dbapi(cls):
        hp_vertica_client = __import__('hp_vertica_client')

        return hp_vertica_client
