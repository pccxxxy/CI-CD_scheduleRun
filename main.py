import datetime 
import logging
import os
import logging.handlers


F = open(r'.\result\status.log', 'a')

F.write(f'{datetime.datetime.now()} - The script started running \n')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    ".\result\status1.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f'{datetime.datetime.now()} - main program triggered')

    logger.info(f"Token value: {SOME_SECRET}")

    logger.info(f'{datetime.datetime.now()} - token logged \n')
    

F.write(f'{datetime.datetime.now()} - The script finished running \n')
