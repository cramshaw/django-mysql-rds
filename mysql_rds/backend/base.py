from django.db.backends.mysql import base

from .client import DatabaseClient
from .creation import DatabaseCreation


class DatabaseWrapper(base.DatabaseWrapper):

    client_class = DatabaseClient
    creation_class = DatabaseCreation

    def get_connection_params(self):
        kwargs = super().get_connection_params()
        if callable(kwargs['passwd']):
            kwargs['passwd'] = kwargs['passwd']()
        return kwargs
