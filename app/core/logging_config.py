"""
logging_config.py
-----------------
Centralized and professional logging configuration for the Raspberry API application.

- Defines handlers for console and rotating file output.
- Uses a LOGGING_CONFIG dictionary compatible with logging.config.dictConfig.
- Allows you to modify format, levels, rotation, and log destinations in one place.
- The main 'raspberry-api' logger is ready to be imported and used throughout the project.
"""

import os
import logging.config

# Directory and log file (can be set via environment variable)
LOG_DIR = os.getenv('LOG_DIR', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'raspberry-api.log')

# Logging configuration dictionary
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,  # Allows other loggers to keep working
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        # Handler for console output
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
        # Handler for rotating file output
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': LOG_FILE,
            'when': 'midnight',           # Rotate at midnight
            'backupCount': 5,             # Keep up to 5 backup files
            'level': 'INFO',
            'encoding': 'utf-8',
            'utc': False
        },
    },
    # Root logger configuration
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    # Application-specific logger
    'loggers': {
        'raspberry-api': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,  # Prevents duplicate logs by not propagating to root
        },
    },
}

def setup_logging():
    """
    Apply the logging configuration defined in LOGGING_CONFIG
    and return the main application logger.
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger('raspberry-api')

# Initialize the main logger when this module is imported
logger = setup_logging()
