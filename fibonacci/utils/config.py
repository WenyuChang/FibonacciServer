__author__ = 'Wenyu'

import os
from ConfigParser import SafeConfigParser

config = SafeConfigParser(
    defaults={'broadcast_address': '127.0.0.1',
              'broadcast_port': 8888,
              })


def parse_config(args):
    config_path = args.config[0] if args.config is not None else None
    if config_path is not None and os.path.exists(config_path):
        try:
            config.read(config_path)
        except:
            # TODO raise exception
            raise
