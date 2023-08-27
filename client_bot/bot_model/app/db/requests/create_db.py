from bot_model.app.db.requests.client_db import db_storage
from exceptions.db_exceptions import CreateDBException, SettingUpDBException

def create_db():
    try:
        db_storage.create_tables
    except CreateDBException:
        pass

    try:
        db_storage.setting_up_all_tables()
    except SettingUpDBException:
        pass