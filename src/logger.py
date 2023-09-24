"""
This module provides configuration settings for logging in the JokeBot application.
It sets up a logger named 'JokeBot_Log' with an INFO log level and configures a console handler to display log messages on the console.

Author: Raigon Augustin
Date: 24.09.2023
"""

import logging

logger = logging.getLogger('JokeBot_Log')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logging_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(logging_format)

logger.addHandler(console_handler)

