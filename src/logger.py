import logging

# Configure logging
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Create console handler and set formatter
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(ch)

    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger('example_logger')
    logger.info('Logger is set up!')