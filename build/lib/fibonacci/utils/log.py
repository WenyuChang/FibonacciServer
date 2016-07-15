__author__ = 'Wenyu'

import os
import logging.config

def parse_log(args):
    config_path = args.config[0] if args.config is not None else None
    if config_path is not None and os.path.exists(config_path):
        try:
            logging.config.fileConfig(config_path)
            logging.raiseExceptions = 1
        except:
            # TODO raise exception
            raise

