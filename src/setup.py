from config.config import KittenConfig
import os


def createFileIfNeeded(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass


def setup() -> KittenConfig:
    config = KittenConfig()
    createFileIfNeeded(config.get("DatabaseFile"))
    return config
