from aiogram import Bot
from aiogram.dispatcher import Dispatcher



class Handler():
    def __init__(self, bot: Bot, dp: Dispatcher) -> None:
        self.bot = bot
        self.dp = dp
    
    @property
    def start_command(self):
        #start_command = StartCommand(self.bot, self.dp, BotCommand.START_COMMAND)
        #start_command.action
        pass

    @property
    def check_user_subscription(self):
        pass