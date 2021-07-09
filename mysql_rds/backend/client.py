from django.db.backends.mysql.client import DatabaseClient as MySQLClient


class DatabaseClient(MySQLClient):

    @classmethod
    def settings_to_cmd_args_env(cls, settings_dict, parameters):

        if callable(settings_dict['PASSWORD']):
            settings_dict['PASSWORD'] = settings_dict['PASSWORD']()
        return super().settings_to_cmd_args_env(settings_dict, parameters)

    settings_to_cmd_args = settings_to_cmd_args_env
