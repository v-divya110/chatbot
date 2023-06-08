import logging

def get_logger(name):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s]---> %(message)s")
    syslog = logging.StreamHandler()
    syslog.setFormatter(formatter)
    log.addHandler(syslog)
    return log
    
