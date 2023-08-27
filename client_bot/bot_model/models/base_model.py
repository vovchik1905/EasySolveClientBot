from typing import Any
import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from exceptions.general_exceptions import StartBotException, StopBotException

class BaseBotModel:
    
    def __init__(self, bot_token: str, bot_url: str, bot_name: str, bot_tg_link: str) -> None:
        self.storage = MemoryStorage()
        self.bot_token = bot_token
        self.bot_url = bot_url
        self.bot_name = bot_name
        self.bot_tg_link = bot_tg_link
        self.bot = Bot(token = bot_token)
        self.dp = Dispatcher(self.bot, storage = self.storage)

        self.logger = logging.getLogger("BOT_LOGGER")
        self.logger.setLevel(logging.DEBUG)
        logger_handler = logging.FileHandler('...\logs\logs.log', mode='a')
        logger_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s") 
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    
    @property
    def start(self) -> None:
        try:
            executor.start_polling(self.dp, skip_updates=False)
        
        except StartBotException:
            self.logger.critical("START ERROR")


    @property
    def stop(self) -> None:
        pass