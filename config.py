from dataclasses import dataclass
from typing import Optional
from environs import Env
import logging


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int = 5432

    def construct_sqlalchemy_url(self, driver="asyncpg", host=None, port=None) -> str:
        """
        SQLAlchemy uchun URL yaratadi.
        """
        try:
            from sqlalchemy.engine.url import URL
            if not host:
                host = self.host
            if not port:
                port = self.port
            uri = URL.create(
                drivername=f"postgresql+{driver}",
                username=self.user,
                password=self.password,
                host=host,
                port=port,
                database=self.database,
            )
            return uri.render_as_string(hide_password=False)
        except ImportError:
            logging.error("SQLAlchemy moduli topilmadi!")
            raise
        except Exception as e:
            logging.error(f"SQLAlchemy URL yaratishda xato: {e}")
            raise

    @staticmethod
    def from_env(env: Env):
        """
        .env fayldan DbConfig obyektini yaratadi.
        """
        try:
            host = env.str("DB_HOST", default="localhost")
            password = env.str("POSTGRES_PASSWORD", default="")
            user = env.str("POSTGRES_USER", default="postgres")
            database = env.str("POSTGRES_DB", default="mydb")
            port = env.int("DB_PORT", default=5432)
            return DbConfig(
                host=host, password=password, user=user, database=database, port=port
            )
        except Exception as e:
            logging.error(f"Ma'lumotlar bazasi sozlamalarini yuklashda xato: {e}")
            raise


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool

    @staticmethod
    def from_env(env: Env):
        """
        .env fayldan TgBot obyektini yaratadi.
        """
        try:
            token = env.str("BOT_TOKEN")
            if not token:
                raise ValueError("BOT_TOKEN .env faylda topilmadi!")
            admin_ids = env.list("ADMINS", subcast=int, default=[])
            use_redis = env.bool("USE_REDIS", default=False)
            return TgBot(token=token, admin_ids=admin_ids, use_redis=use_redis)
        except Exception as e:
            logging.error(f"Bot sozlamalarini yuklashda xato: {e}")
            raise


@dataclass
class RedisConfig:
    redis_pass: Optional[str]
    redis_port: Optional[int]
    redis_host: Optional[str]

    def dsn(self) -> str:
        """
        Redis DSN (Data Source Name) yaratadi.
        """
        try:
            if not self.redis_host or not self.redis_port:
                raise ValueError("Redis host yoki port topilmadi!")
            if self.redis_pass:
                return f"redis://:{self.redis_pass}@{self.redis_host}:{self.redis_port}/0"
            return f"redis://{self.redis_host}:{self.redis_port}/0"
        except Exception as e:
            logging.error(f"Redis DSN yaratishda xato: {e}")
            raise

    @staticmethod
    def from_env(env: Env):
        """
        .env fayldan RedisConfig obyektini yaratadi.
        """
        try:
            redis_pass = env.str("REDIS_PASSWORD", default=None)
            redis_port = env.int("REDIS_PORT", default=6379)
            redis_host = env.str("REDIS_HOST", default="localhost")
            return RedisConfig(
                redis_pass=redis_pass, redis_port=redis_port, redis_host=redis_host
            )
        except Exception as e:
            logging.error(f"Redis sozlamalarini yuklashda xato: {e}")
            raise


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous
    db: Optional[DbConfig] = None
    redis: Optional[RedisConfig] = None


def load_config(path: str = None) -> Config:
    """
    .env fayldan barcha konfiguratsiyalarni yuklaydi.

    :param path: .env fayl manzili (ixtiyoriy).
    :return: Config obyekti.
    """
    try:
        env = Env()
        env.read_env(path)
        config = Config(
            tg_bot=TgBot.from_env(env),
            misc=Miscellaneous(),
            # db=DbConfig.from_env(env),  # Agar ma'lumotlar bazasi ishlatilsa
            # redis=RedisConfig.from_env(env),  # Agar Redis ishlatilsa
        )
        logging.info("Konfiguratsiya muvaffaqiyatli yuklandi")
        return config
    except Exception as e:
        logging.error(f"Konfiguratsiya yuklashda xato: {e}")
        raise