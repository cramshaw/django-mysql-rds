from unittest import TestCase
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

from mysql_rds.backend.base import DatabaseWrapper

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


class DatabaseWrapperTest(TestCase):

    def test_get_callable_connection_params(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = generate_pw
        rds_params = DatabaseWrapper(conn_settings).get_connection_params()
        self.assertEqual(rds_params['passwd'], CALLABLE_PASSWORD)

    def test_get_connection_params_strings(self):
        conn_settings = SETTINGS_DICT
        conn_settings['PASSWORD'] = STRING_PASSWORD
        rds_params = DatabaseWrapper(conn_settings).get_connection_params()
        mysql_params = MySQLDatabaseWrapper(
            conn_settings).get_connection_params()
        self.assertEqual(rds_params, mysql_params)
        self.assertEqual(rds_params['passwd'], STRING_PASSWORD)
