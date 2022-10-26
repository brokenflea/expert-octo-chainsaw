import logging
from datetime import datetime

import discord
from discord import ApplicationContext, DiscordException
from discord.ext import tasks
from discord.ext.commands import AutoShardedBot

logger = logging.getLogger(__name__)


class PapaFleaBotContext(ApplicationContext):
    async def check(self):
        return True

class PapaFleaBot(AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get_application_context(self, interaction, cls=PapaFleaBotContext):
        return await super().get_application_context(interaction, cls=cls)

    async def on_ready(self):
        logger.info('Welcome to PapaFleaBot!')
