from django.db.backends.mysql import base

from .client import DatabaseClient
from .creation import DatabaseCreation


class DatabaseWrapper(base.DatabaseWrapper):

    client_class = DatabaseClient
    creation_class = DatabaseCreation

    def get_connection_params(self):
        kwargs = super().get_connection_params()
        possible_password_kwargs = (
            'password',
            'passwd',
        )

        def get_value(value):
            return value() if callable(value) else value

        password_kwargs = {
            k: get_value(v)
            for k, v in kwargs.items() if k in possible_password_kwargs
        }
        kwargs.update(password_kwargs)
        return kwargs
