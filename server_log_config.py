import logging
import logging.handlers
from logging.handlers import RotatingFileHandler

LOG_FILENAME = "app.srv.log"
logging.basicConfig(
    format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
    filename=LOG_FILENAME,
    level=logging.ERROR
)
handler: RotatingFileHandler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20, backupCount=5)
