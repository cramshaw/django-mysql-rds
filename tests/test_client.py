from unittest import TestCase
from django.db.backends.mysql.client import DatabaseClient as MySQLDatabaseClient

from backend.rds.client import DatabaseClient

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
    def test_get_callable_cmd_args(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = generate_pw
        rds_args = DatabaseClient.settings_to_cmd_args(conn_settings)
        self.assertEqual(rds_args[2], f'--password={CALLABLE_PASSWORD}')

    def test_get_cmd_args_strings(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = STRING_PASSWORD
        rds_args = DatabaseClient.settings_to_cmd_args(conn_settings)
        mysql_args = MySQLDatabaseClient.settings_to_cmd_args(conn_settings)
        self.assertEqual(rds_args, mysql_args)
        self.assertEqual(rds_args[2], f'--password={STRING_PASSWORD}')
