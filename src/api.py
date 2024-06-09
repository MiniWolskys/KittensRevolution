from config.config import KittenConfig
from discord.ext import commands
import discord

from src.data import Data
from src.discord_helper import checkUserExistsAndIsInGuild
import src.output as kitten_output
import src.helper as kitten_helper

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Revolution bot ready.")
    await bot.change_presence(activity=discord.Game(name='Revolution ! 🔥'))


@bot.command(name='revolution')
async def revolution(ctx: commands.Context, user: discord.User=None):
    print(f"Revolution command received.")
    if user is None:
        user = ctx.author
    if not checkUserExistsAndIsInGuild(ctx, user):
        await kitten_output.sendInvalidUserMessage(ctx, user)
        return
    new_points = kitten_helper.getNumberOfPoints(ctx.author, user)
    new_score = kitten_helper.assignPointsToUser(user, new_points)
    await ctx.send(f"{user.name} got {new_points} new points and is now at {new_score} !")


@bot.command(name='give')
async def give(ctx: commands.Context, target: discord.User, points: int=None):
    print(f'Give user {target.name} {points} points from user {ctx.author.name}')
    src = ctx.author
    if not checkUserExistsAndIsInGuild(ctx, target):
        await kitten_output.sendInvalidUserMessage(ctx, target)
        return
    if src.id is target.id:
        await kitten_output.sendCannotGiveToYourselfMessage(ctx)
        return
    if points is None:
        kitten_helper.getNumberOfPoints(ctx.author, ctx.author)
    if points < 0 or kitten_helper.getUserNumberOfPoints(src.id) < points:
        await kitten_output.sendInvalidNumberOfPointMessage(ctx)
        return
    kitten_helper.assignPointsToUser(target, points)
    kitten_helper.assignPointsToUser(src, -points)
    await ctx.send(f"{src.name} gave {target.name} {points} points !")


@bot.command(name='leaderboard')
async def leaderboard(ctx: commands.Context):
    await ctx.send(kitten_output.formatLeaderboard(get_leaderboard()))


@give.error
async def give_error(ctx: commands.Context, error):
    print(f"Give command received with error \"{error}\"")
    await ctx.send(error)


@revolution.error
async def revolution_error(ctx: commands.Context, error):
    print(f"Revolution command received with error \"{error}.\"")
    await ctx.send(error)


@leaderboard.error
async def leaderboard_error(ctx: commands.Context, error):
    print(f"Leaderboard command received with error \"{error}.\"")
    await ctx.send(error)


def start_bot(config: KittenConfig, data: Data):
    token = config.get("BotToken")
    bot.run(token)
