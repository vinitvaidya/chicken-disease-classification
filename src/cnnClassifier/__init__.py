import os
import sys
import logging

# logging string contains the datetime, log level, module name and the message
logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir = "logs" #create a directory for logs
log_filepath = os.path.join(log_dir, "running_logs.log") #to create a log file in the logs directory
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    
    handlers = [
        logging.FileHandler(log_filepath), #to write logs to the log file
        logging.StreamHandler(sys.stdout) #to print logs to the console
    ]
)

logger = logging.getLogger("cnnClassifierLogger") #to get the logger object