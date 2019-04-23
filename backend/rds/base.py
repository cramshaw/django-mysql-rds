from django.db.backends.mysql import base


class CursorWrapper(base.CursorWrapper):
    pass


class DatabaseWrapper(base.DatabaseWrapper):
    def get_connection_params(self):
        kwargs = super().get_connection_params()
        if callable(kwargs['passwd']):
            kwargs['passwd'] = kwargs['passwd']()
        return kwargs
