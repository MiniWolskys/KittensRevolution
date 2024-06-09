import discord
from discord.ext import commands

from src.discord_helper import findUserAssociatedWithId


async def sendCannotGiveToYourselfMessage(ctx: commands.Context):
    await ctx.send(f"You cannot give yourself points {ctx.author.name} !")


async def sendInvalidNumberOfPointMessage(ctx: commands.Context):
    await ctx.send(f"User {ctx.author.name} does not have enough point to give, or number of points is negative.")


async def sendInvalidUserMessage(ctx: commands.Context, user: discord.User):
    await ctx.send(f"User {user} is invalid or not on the server."
                   f"Please make sure user is valid by mentioning them."
                   f"And make sure they are present on the discord server.")


def formatLeaderboard(leaderboard: dict[int, int]) -> str:
    leaders_as_a_list = list(leaderboard.items())
    leaders_as_a_list = sorted(leaders_as_a_list, key=lambda parameter: parameter[1], reverse=True)
    result = ''
    for leader in leaders_as_a_list:
        result += findUserAssociatedWithId(leader[0]).name + ": " + str(leader[1]) + '\n'
    return result
