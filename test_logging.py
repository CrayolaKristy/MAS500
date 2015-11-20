import logging
 
# add filemode="w" to overwrite
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG) #logging.X USE CAPITAL LETTERS!!

 
#logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")  # logging.x use lowercase letters.
logging.info("Informational message")
logging.error("An error has happened!")


logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')