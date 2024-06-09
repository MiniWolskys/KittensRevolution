from configparser import ConfigParser

CONFIG_FILE = "./config.ini"


class KittenConfig:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_FILE)
        self.keys = {
            "CommandPrefix": self.config["DISCORD"]["CommandPrefix"],
            "BotToken": self.config["DISCORD"]["BotToken"],
            "Type": self.config["DATABASE"]["Type"],
            "DatabaseFile": self.config["DATABASE"]["DatabaseFile"],
        }

    def get(self, key: str) -> str | None:
        return self.keys.get(key)
