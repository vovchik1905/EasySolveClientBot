class ClientBotException(Exception):
    pass

class BaseModelException(ClientBotException):
    pass

class StartBotException(BaseModelException):
    pass

class StopBotException(BaseModelException):
    pass