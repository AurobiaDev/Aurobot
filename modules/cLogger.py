import logging
import logging.handlers

def new_log(filename="discord.log"):
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    logging.getLogger("discord.http").setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename=filename,
        encoding="utf-8",
        maxBytes=32*1024*1024,
        backupCount=5
    )

    dt_fmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter("[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
