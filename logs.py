import os
from torch.utils.tensorboard import SummaryWriter
import logging

def getWriter(name):
    return SummaryWriter(log_dir=os.path.join("logs", name))

def getLogger(name, level=logging.INFO, loginFile=True):
    # logger
    logger = logging.getLogger(name)
    logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%m/%d/%Y %H:%M:%S',
                            level=level)
    # 是否写入文件
    if loginFile:
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        if not os.path.exists(os.path.join("logs", name)):
            os.makedirs(os.path.join("logs", name))
        logger_file = os.path.join("logs", name, name + ".log")
        fh = logging.FileHandler(logger_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

if __name__ == "__main__":
    logger = getLogger("test")
    logger.info("test")
    logger.error("error")
    logger.warning("warning")
    logger.debug("debug")
    writer = getWriter("test")
    writer.add_text("test", "test")
    writer.close()