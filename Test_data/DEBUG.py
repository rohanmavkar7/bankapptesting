from logger_class.logger_class import logger_class

# Get the logger instance
logger = logger_class.log_gen_method()

# Print logger handlers
print(logger.handlers)  # This will display attached handlers

# Log a test message
logger.info("This is a test log message.")
