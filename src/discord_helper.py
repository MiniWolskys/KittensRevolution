import discord
from discord.ext import commands


def findUserAssociatedWithId(userId: int) -> discord.User:
    return bot.get_user(userId)


def checkUserExistsAndIsInGuild(ctx: commands.Context, user: discord.User) -> bool:
    return ctx.guild.get_member(user.id) is not None
