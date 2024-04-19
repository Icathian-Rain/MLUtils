import os
from torch.utils.tensorboard import SummaryWriter
import logging
from typing import Union

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

class Logs:
    def __init__(self, name, level=logging.INFO, loginFile=True):
        self.logger = getLogger(name, level, loginFile)
        self.writer = getWriter(name)
    
    # 添加数据到tensorboard
    def add_scalar(self, tag : Union[str, list], scalar_values: Union[int, float, list], global_step=None, walltime=None):
        if isinstance(scalar_values, (int, float)) and isinstance(tag, str):
            self.writer.add_scalar(tag, scalar_values, global_step, walltime)
            self.logger.info(f'global_step: {global_step}, {tag}: {scalar_values}')
        elif isinstance(scalar_values, list) and isinstance(tag, list) and len(scalar_values) == len(tag):
            msg = f'global_step: {global_step}, '
            for i, t in enumerate(tag):
                self.writer.add_scalar(t, scalar_values[i], global_step, walltime)
                msg += f'{t}: {scalar_values[i]}, '
            self.logger.info(msg)
        else:
            raise ValueError("tag and scalar_values should be the same type")
        

if __name__ == "__main__":
    logger = getLogger("test")
    logger.info("test")
    logger.error("error")
    logger.warning("warning")
    logger.debug("debug")
    writer = getWriter("test")
    writer.add_text("test", "test")
    writer.close()
    logs = Logs("test1")
    logs.add_scalar("val", 1, 1)
    logs.add_scalar(["val1", "val2"], [1, 2], 2)
    logs.add_scalar("val2", [1, 2], 1)