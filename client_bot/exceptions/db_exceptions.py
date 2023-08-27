from exceptions.general_exceptions import ClientBotException


class BaseDBException(ClientBotException):
    pass

class CreateDBException(BaseDBException):
    pass

class SettingUpDBException(BaseDBException):
    pass