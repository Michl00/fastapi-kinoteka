from dataclasses import dataclass

from environs import Env


@dataclass
class Logger:
    format: str
    level: str

@dataclass
class Config:
    log: Logger

def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Config(
        log = Logger(format = env("LOG_FORMAT"),
                     level = env("LOG_LEVEL"),),
    )