from src.api import start_bot
from src.data import Data
from src.setup import setup

if __name__ == '__main__':
    config = setup()
    data = Data(config)
    start_bot(config, data)
