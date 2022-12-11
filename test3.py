import logging
logging.basicConfig(filename="test3.log",level=logging.INFO ,format ='%(levelname)s %(asctime)s %(name)s %(message)s')


def divide(a,b):
    logging.info("The number entered by user is %s and %s" , a,b)
    try:
        logging.info("We are into function")
        div = a/b
        logging.info("We have completed a division operation")
        logging.info("The result of code is %s", div)
        return div
    except Exception as e:
        logging.exception(e)

print((divide(3,9)))