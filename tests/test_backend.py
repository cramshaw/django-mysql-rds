from django.test import TestCase, override_settings
from django.conf import settings
from django.db import connection, DatabaseError
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

from django_mysql_rds.backend.rds.base import DatabaseWrapper

CALLABLE_PASSWORD = 'generated'
STRING_PASSWORD = 'fish'


def generate_pw():
    return CALLABLE_PASSWORD


class DatabaseWrapperTest(TestCase):

    def test_get_callable_connection_params(self):
        conn_settings = connection.settings_dict.copy()
        conn_settings['PASSWORD'] = generate_pw
        print(conn_settings)
        rds_params = DatabaseWrapper(conn_settings).get_connection_params()
        self.assertEqual(rds_params['passwd'], CALLABLE_PASSWORD)

    def test_get_connection_params_strings(self):
        conn_settings = connection.settings_dict.copy()
        conn_settings['PASSWORD'] = STRING_PASSWORD
        print(conn_settings)
        rds_params = DatabaseWrapper(conn_settings).get_connection_params()
        mysql_params = MySQLDatabaseWrapper(
            conn_settings).get_connection_params()
        self.assertEqual(rds_params, mysql_params)
        self.assertEqual(rds_params['passwd'], STRING_PASSWORD)
