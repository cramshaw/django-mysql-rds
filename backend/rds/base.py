from django.db.backends.mysql import base

from .client import DatabaseClient


class DatabaseWrapper(base.DatabaseWrapper):

    client_class = DatabaseClient

    def get_connection_params(self):
        kwargs = super().get_connection_params()
        if callable(kwargs['passwd']):
            kwargs['passwd'] = kwargs['passwd']()
        return kwargs
