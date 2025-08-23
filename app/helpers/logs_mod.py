import logging
import os

def setup_logger(name):
    """
    Sets up a logger instance with console handler and appropriate level.
    The logging level is determined by the DEBUG_MODE environment variable.
    
    Args:
        name (str): The name of the logger, typically __name__.

    Returns:
        logging.Logger: A configured logger object.
    """
    # Get a logger instance
    logger = logging.getLogger(name)

    # Prevent duplicate handlers if the function is called multiple times
    if not logger.handlers:
        # Create a handler to write to the console
        handler = logging.StreamHandler()
        
        # Define the log message format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(handler)

    # Set the logging level based on the environment variable
    # We check for 'true', '1', or 't' to be case-insensitive and flexible
    debug_mode = os.getenv('DEBUG_MODE', 'False').lower() in ('true', '1', 't')
    if debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    
    return logger
