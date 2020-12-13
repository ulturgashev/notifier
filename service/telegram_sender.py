import logging

from aiogram import Bot, types
from aiogram.utils.markdown import text, bold, italic, code, pre

from service.config import Config
from service.models import Message, Event

logger = logging.getLogger(__name__)


def build_markdown(message: Message):
    entries = message.prepare_markdown()
    messages = [
        '{}: {}'.format(italic(entry[0]), bold(entry[1])) for entry in entries
    ]
    return text(*messages, sep='\n')


class TelegramSender:
    def __init__(self, token, loop, config: Config):
        self.config = config
        self.bot = Bot(token=token)

    async def send_message(self, message: Message):
        await self.bot.send_message(
            self.config.CHAT_ID, build_markdown(message),
            parse_mode=types.ParseMode.MARKDOWN
        )
