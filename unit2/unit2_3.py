import logging

# Configure logging
logging.basicConfig(
    filename='error_log.log',   # Log file name
    level=logging.ERROR,        # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    a = 10
    b = 5

    # This will generate an arithmetic exception (division by zero)
    result = a / b

except ZeroDivisionError as e:
    logging.error("Arithmetic Exception occurred: %s", e)
    print("An arithmetic exception occurred. Check the log file for details.")