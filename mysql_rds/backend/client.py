from django.db.backends.mysql.client import DatabaseClient as MySQLClient


class DatabaseClient(MySQLClient):

    @classmethod
    def settings_to_cmd_args(cls, settings_dict):

        if callable(settings_dict['PASSWORD']):
            settings_dict['PASSWORD'] = settings_dict['PASSWORD']()
        return super().settings_to_cmd_args(settings_dict)
