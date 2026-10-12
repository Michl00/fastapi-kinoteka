from dataclasses import dataclass

from environs import Env


@dataclass
class Logger:
    format: str
    level: str

@dataclass
class DBConfig:
    host: str
    port: int
    password: str

@dataclass
class Config:
    log: Logger
    db: DBConfig

def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)

    return Config(
        log=Logger(
            format=env("LOG_FORMAT"),
            level=env("LOG_LEVEL"),
        ),
        db=DBConfig(
            host=env("DB_HOST"),
            port=env.int("DB_PORT"),
            password=env("DB_PASS"),
        ),
    )