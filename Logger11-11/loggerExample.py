import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w',
                    encoding='UTF-8',
                    format='%(levelname)s:%(asctime)s - %(message)s'
                    )

# logging.debug("Debug message Привіт")
# logging.info("Info message")
# logging.warning("Warning message !!!")
# logging.error("Error message !!!")
# logging.critical("Critical message !!!")

try:
    print(10/0)
except ZeroDivisionError as error:
    logging.exception(error)
