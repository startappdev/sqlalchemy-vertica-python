from base import VerticaDialect as BaseVerticaDialect


# noinspection PyAbstractClass,PyClassHasNoInit
class VerticaDialect(BaseVerticaDialect):
    driver = 'vertica_python'

    @classmethod
    def dbapi(cls):
        vp_module = __import__('vertica_python')
        vp_module.Error = vp_module.errors.Error  # sqlalchemy expects to find here the base Error
        return vp_module
