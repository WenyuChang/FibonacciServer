__author__ = 'Wenyu'

import logging
import argparse
from argparse import RawTextHelpFormatter

from handlers.basehttphandler import FibHttpHandler
from utils.config import parse_config, config
from utils.log import parse_log
from utils.simple_http_server import SimpleHttpServer


def _fibonacci_server(args):
    # Prepare basic information
    parse_config(args)
    parse_log(args)
    logger = logging.getLogger(__name__)

    # Getting http server information
    logger.info("Starting Fibonacci Server with Args: %s" % args)
    host = args.host[0] if args.host is not None else config.get('http_server', 'broadcast_address')
    port = int(args.port[0]) if args.port is not None else int(config.get('http_server', 'broadcast_port'))
    logger.debug("Fibonacci Server Host Address: %s" % host)
    logger.debug("Fibonacci Server Host Port: %s" % port)

    # Start HTTP server
    print "Serving HTTP on %s:%s..." % (host, port)
    server = SimpleHttpServer(host, port, FibHttpHandler)
    server.start()
    server.waitForThread()

def parser_creation():
    parser = argparse.ArgumentParser(description='Fibonacci Simple HTTP Server:', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-version', action='version', version='%(prog)s 0.9', help='Version of %(prog)s')
    subparsers = parser.add_subparsers(help='Sub-Command help')

    helpStr = 'This command is for a simple HTTP Server which will host an simple Fibonacci query function.'
    parser_fib = subparsers.add_parser('fibonacci', help=helpStr, formatter_class=RawTextHelpFormatter)
    parser_fib.set_defaults(func=_fibonacci_server)

    parser_fib.add_argument('-c', '--config', nargs=1, help='[Required] Config File Path for Simple HTTP Server', required=True)
    parser_fib.add_argument('-p', '--port', nargs=1, help='Broadcast Host Port of Simple HTTP Server', required=False)
    parser_fib.add_argument('-ha', '--host', nargs=1, help='Broadcast Host Address of Simple HTTP Server',
                            required=False)

    return parser


if __name__ == '__main__':
    parser = parser_creation()
    args = parser.parse_args()
    args.func(args)
