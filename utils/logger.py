

import logging


def setup_logger(debug=False):
    """
    Setup global logger
    """
    level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    return logging.getLogger("UploadHunter")
