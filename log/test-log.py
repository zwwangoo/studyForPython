import sys
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add(sys.stderr, level="ERROR", format=fmt)

# Only write messages from "a" logger
logger.start("a.log", filter=lambda record: record["extra"].get("name") == "a")
# Only write messages from "b" logger
logger.start("b.log", filter=lambda record: record["extra"].get("name") == "b")

logger_a = logger.bind(name="a")
logger_b = logger.bind(name="b")

logger_a.info("Message A")
logger_b.info("Message B")
logger_b.error('debug')
