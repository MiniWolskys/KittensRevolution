from config.config import KittenConfig


class Data:
    def __init__(self, config: KittenConfig):
        self.data_file_path = config.get("DatabaseFile")

    def get_users_data(self) -> dict[int, dict[str, int]]:
        users_data = {}
        with open(self.data_file_path, "r") as file:
            for line in file:
                user_data = line.split(';')
                users_data[int(user_data[0])] = {
                    "score": int(user_data[1]),
                    "last_revolution_timestamp": int(user_data[2]),
                    "current_revolution_streak": int(user_data[3]),
                }
        return users_data

    def get_user_data(self, user_id: int) -> dict[str, int] | None:
        return self.get_users_data().get(user_id)

    def get_leaderboard(self) -> dict[int, int]:
        users_data = {}
        with open(self.data_file_path, "r") as file:
            for line in file:
                user_data = line.split(';')
                users_data[int(user_data[0])] = int(user_data[1])
        return users_data

    def get_leaderboard_for_user(self, user_id: int) -> int | None:
        return self.get_leaderboard().get(user_id)

    def update_user_data(self, user_id: int, score: int, last_revolution: int, streak: int):
        new_line = f"{user_id};{score};{last_revolution};{streak}\n"
        final_file = ""
        with open(self.data_file_path, "r+") as file:
            for line in file:
                if line.split(';')[0] is user_id:
                    final_file += new_line
                else:
                    final_file = line + "\n"
            file.write(final_file)

    def update_leaderboard(self, user_id: int, score: int):
        user_data = self.get_user_data(user_id)
        if user_data is None:
            return
        last_revolution = user_data.get("last_revolution_timestamp")
        streak = user_data.get("current_revolution_streak")
        self.update_user_data(user_id, score, last_revolution, streak)
