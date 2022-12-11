import logging
logging.basicConfig(filename="test5.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')

try:
    logging.info('I am trying to read a file')
    with open("Dharmendra.txt","r"):
        logging.info("Successfully it has been read the file")
except Exception as e:
    logging.critical("This is a situation for us")
    logging.error(e)
    logging.exception(e)
