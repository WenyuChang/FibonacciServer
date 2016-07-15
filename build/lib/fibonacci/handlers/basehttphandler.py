__author__ = 'Wenyu'
import urlparse
import logging
import time

from BaseHTTPServer import BaseHTTPRequestHandler
from fibonacci.utils.config import config


def _query_fib(n):
    out = [0, 1]
    if n < 2:
        return out[:n]

    for i in range(2, n):
        next = out[-1] + out[-2]
        out.append(next)

    return out


class FibHttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.do_GET()

    def do_GET(self):
        logger = logging.getLogger(__name__)
        logger.info("Got and starting to process request: %s" % self.path)
        print self.path
        if self.path.startswith('favicon.ico') or self.path.startswith('/json'):
            # Ignore requests for favicon icon
            return

        if self.path.startswith(config.get('http_server', 'fib_query_prefix')):
            try:
                parsed = urlparse.urlparse(self.path)
                parsed = urlparse.parse_qs(parsed.query)
                if 'n' not in parsed:
                    self._generate_error_response(400, 'N NOT Passed in...', logger)
                n = int(parsed['n'][0])
                if n < 0:
                    self._generate_error_response(400, 'Negative N...', logger)
                    return

                logger.info("Got Fibonacci Query Request with N=%s" % n)
                start_time = time.time()
                out = _query_fib(n)
                end_time = time.time()
                logger.info("After Processing Fibonacci Query Request, and it takes %s second(s) to generate fibonacci list." % (
                end_time - start_time))

                logger.info("Start Processing Response...")
                start_time = time.time()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(out)
                end_time = time.time()
                logger.info("End Processing Response...It takes %s second(s) to generate response." % (
                end_time - start_time))
            except Exception, ex:
                self._generate_error_response(500, 'Failed when processing request: %s' % ex.message, logger)
        else:
            self._generate_error_response(404, 'Page Not Found', logger)

        logger.info("End Processing Request...")

    def _generate_error_response(self, code, message, logger):
        logger.error(
            "Got Exception When Processing Request. Error code is %s and error message is %s" % (code, message))
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write('Failed when processing request: %s' % message)
