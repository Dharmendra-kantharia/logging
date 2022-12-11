import logging
logging.basicConfig(filename="test4.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
# Will get the logging out in log file based on the hierarchy as mention below. If you select logging level Debug it will show you result after debug like Info,warning,Error and critical
# If you select Warning logging then it will show result below logging like Error and Critical
# 1. Debug - 10
# 2. Info - 20
# 3. Warning -30
# 4. Error - 40
# 5. Critical - 50

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