import logging

logging.basicConfig(
    filename="app.clnt.log",
    format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
    level=logging.ERROR
)
