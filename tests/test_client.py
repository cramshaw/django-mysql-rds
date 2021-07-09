from unittest import TestCase
from django.db.backends.mysql.client import DatabaseClient as MySQLDatabaseClient

from mysql_rds.backend.base import DatabaseClient

CALLABLE_PASSWORD = 'generated'
STRING_PASSWORD = 'fish'

SETTINGS_DICT = {
    'ENGINE': 'django_mysql_rds.backend.rds',
    'NAME': 'test_user_db',
    'USER': 'docker',
    'PASSWORD': '',
    'HOST': 'db',
    'PORT': '3306',
    'ATOMIC_REQUESTS': False,
    'AUTOCOMMIT': True,
    'CONN_MAX_AGE': 0,
    'OPTIONS': {},
    'TIME_ZONE': None,
    'TEST':
        {'CHARSET': None,
         'COLLATION': None,
         'NAME': None,
         'MIRROR': None
         }
}


def generate_pw():
    return CALLABLE_PASSWORD


class DatabaseClientTest(TestCase):
    @staticmethod
    def client_settings_to_cmd_args_env_wrapper(
        *args,
        client=DatabaseClient
    ) -> tuple:
        """
        Wraps client class method to work with Django 3.5 and below.
        Passes args.
        Needed because of a signature and return type change in:
            https://github.com/django/django/commit/bbe6fbb87
        """
        fallback_method_name = 'settings_to_cmd_args'
        new_method_name = f'{fallback_method_name}_env'
        method = getattr(client, new_method_name, fallback_method_name)
        output = method(*args)
        if type(output) is not tuple:
            output = output, None
        return output

    def test_get_callable_cmd_args(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = generate_pw
        rds_args, env = self.client_settings_to_cmd_args_env_wrapper(
            conn_settings, []
        )

        if env:
            self.assertEqual(env['MYSQL_PWD'], CALLABLE_PASSWORD)
        else:
            self.assertEqual(rds_args[2], f'--password={CALLABLE_PASSWORD}')

    def test_get_cmd_args_strings(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = STRING_PASSWORD
        rds_args, rds_env = self.client_settings_to_cmd_args_env_wrapper(
            conn_settings, []
        )

        if rds_env:
            self.assertEqual(rds_env['MYSQL_PWD'], STRING_PASSWORD)
        else:
            self.assertEqual(rds_args[2], f'--password={STRING_PASSWORD}')

        mysql_args, mysql_env = self.client_settings_to_cmd_args_env_wrapper(
            conn_settings,
            [],
            client=MySQLDatabaseClient
        )
        self.assertEqual(rds_args, mysql_args)
        self.assertEqual(rds_env, mysql_env)
