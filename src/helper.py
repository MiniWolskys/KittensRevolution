import random
from datetime import datetime

import discord

from src.discord_helper import findUserAssociatedWithId


def getUserNumberOfPoints(user_id: int) -> int:
    return Data.get_leaderboard_for_user(user_id)


def getNumberOfPoints(author: discord.User, user: discord.User) -> int:
    value = random.randint(1, 10)
    if author.id is not user.id:
        return value
    streak = get_user_streak_data(user.id)
    is_good = random.randint(1, 20) > streak
    return value if is_good else -value


def get_user_streak_data(userId: int) -> int:
    data = Data.get_users_data()
    if userId not in data:
        data[userId] = [0, 0]
    already_in_last_minute: bool = checkInLastMinute(data[userId][0])
    if already_in_last_minute:
        data[userId][1] += 1
    else:
        data[userId][1] = 0
    data[userId][0] = getCurrentTimestamp()
    Data.update_user_data(data[userId][0])
    return data[userId][1]


def getCurrentTimestamp() -> int:
    return int(datetime.timestamp(datetime.now()))


def checkInLastMinute(last_message_timestamp: int) -> bool:
    return (getCurrentTimestamp() - last_message_timestamp) < 60


def assignPointsToUser(user: discord.User, points: int):
    user_score = Data.get_leaderboard_for_user(user.id)
    score = (user_score if user_score is not None else 0) + points
    Data.update_leaderboard(user.id, score)
    return score
