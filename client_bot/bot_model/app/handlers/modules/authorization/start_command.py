from __future__ import annotations
from typing import Any
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from bot_model.app.view.modules.authorization.start_command import view_start_command
from bot_model.app.logic.modules.authorization.start_command import logic_start_command
from bot_model.app.db.modules.authorization.start_command import db_start_command


def start_command():
    pass