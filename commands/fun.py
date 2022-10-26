import logging
import discord

from core.papa_flea_bot import PapaFleaBotContext
from discord.commands import slash_command
from discord.ext import commands

logger = logging.getLogger(__name__)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx: PapaFleaBotContext):
        await ctx.respond(f'Pong! {ctx.bot.latency * 1000:.2f}ms')

def setup(bot):
    bot.add_cog(Fun(bot))
