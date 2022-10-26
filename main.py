import logging
import logging.config
import datetime
import core

from pathlib import Path

from utils.log_formatter import LogFormatter

def setup_logger():
    formatter = LogFormatter()
    s = datetime.datetime.utcnow()
    path = Path('./logs')
    file = f'{path.absolute()}/papa-flea-bot_{s.year}-{s.month}-{s.day}-{s.hour}:{s.minute}:{s.second}.log'

    if not path.exists():
        path.mkdir()

    logging.basicConfig(filename=file, format=formatter.log_fmt, level=logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(LogFormatter())
    logging.getLogger('').addHandler(console)

    logging.getLogger('discord.client').setLevel(logging.INFO)
    logging.getLogger('discord.gateway').setLevel(logging.INFO)

    if not core.config.debug:
        logging.getLogger('discord').setLevel(logging.INFO)


setup_logger()

import sys
import discord
import time

from commands import fun
from core import config
from core.papa_flea_bot import PapaFleaBot

logger = logging.getLogger(__name__)
logger.info("Logger initialized.")


def main():
    bot = PapaFleaBot(intents=discord.Intents.all())

    fun.setup(bot)

    try:
        bot.run(config.token)
    except discord.LoginFailure:
        logger.critical('=== LoginFailure: Failed to launch PapaFleaBot ===')
        sys.exit(1)


if __name__ == '__main__':
    main()
