import logging
#logging setting
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%M-%D %H:%M:%S',
                    handlers=[logging.FileHandler('app1.log'),logging.StreamHandler()]
                    )

logger=logging.getLogger('maths')
def add(a,b):
    logger.debug(f"adding {a} + {b} ={a+b}")
    return a+b
def mul(a,b):
    logger.debug(f"multiply {a} * {b}={a*b}")
    return a*b
def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} / {b}={a/b}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero")
        return None
    

add(10,15)
mul(10,20)
divide(20,0)