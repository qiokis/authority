import tomllib
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DBConfig:
    host: str
    port: int
    name: str
    user: str
    passw: str

class Config:
    _shared_dict = {}
    _initialized = False

    def __init__(self, config_path: Path = "authority.toml") -> None:
        if self._initialized is False:
            with open(config_path, "rb") as f:
                config = tomllib.load(f)
                self.db = DBConfig(
                    host=config["database"]["host"],
                    port=config["database"]["port"],
                    name=config["database"]["name"],
                    user=config["database"]["user"],
                    passw=config["database"]["passw"],
                )
            self._shared_dict = self.__dict__
        else:
            self.__dict__ = self._shared_dict

    def __str__(self) -> str:
        return f"{self._db_config}"

Config()
