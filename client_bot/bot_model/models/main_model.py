from typing import Any
from bot_model.models.base_model import BaseBotModel
from bot_model.app.handlers.handler_models.handler_model import Handler

class MainBotModel(BaseBotModel):
    def __init__(self, bot_token: str, bot_url: str, bot_name: str, bot_tg_link: str) -> None:
        super().__init__(bot_token, bot_url, bot_name, bot_tg_link)
    
    @property
    def action(self):
        ClientBot = Handler(self.bot, self.dp)
        #ClientBot.start_command