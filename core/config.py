import logging
import os
from configparser import ConfigParser
from dotenv import load_dotenv
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class Config:
    token: str
    debug: bool

def path_valid(p):
    return p != '' and Path(p).exists()

def get_or_create_config():
    config_path = Path('./config.ini')

    logger.info(f'Searching for config file at {config_path.absolute()}...')

    config = ConfigParser()

    bot_key = 'BOT_CONFIG'
    load_dotenv()

    if not config_path.exists():
        logger.info('Config file not found, creating one...')
        config[bot_key] = {
                'token': os.getenv('DISCORD_TOKEN'),
                'debug': False
        }

        with open(config_path.absolute(), 'w') as conf:
            config.write(conf)
        logger.info(f'Created a new config file at {config_path.absolute()}.')

    logger.info(f'Config file found.')
    config.read(config_path.absolute())
    bot_data = config[bot_key]

    return Config(bot_data['token'], bot_data['debug'] == 'True')
