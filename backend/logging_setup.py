import logging
import os


def setup_logger(name, log_file='server.log', level=logging.DEBUG):
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Full path for the log file
    log_path = os.path.join(log_dir, log_file)

    # Create custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
