import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("This is my very first code for logging")
logging.warning("This will try to load a warning message")
logging.error("This is a error message from system")

l = [1,2,3,4,5,6,7,8,9,10,11]

for i in l:
    if i == 2 :
        logging.info(i)
        logging.warning("This is warning for a user that they have found out 2 in list")

logging.shutdown()
