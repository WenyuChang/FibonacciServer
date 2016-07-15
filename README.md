# Fibonacci Server Summary

## Deployment Steps
* Download this project from: `https://github.com/WenyuChang/FibonacciServer.git`
* Make sure having the proper permission to install package
* Go to the path where package is downloaded
* Run `sudo python FibonacciServer/setup.py install`
* You will see below notes after installation complete
   ```
##############################
##############################
Prepare before Start:
1. Copy configuation file from /Users/Wenyu/Desktop/FibonacciServer/fibonacci/templates/fibonacci.conf.template
2. Change configuration, such as HTTP server host/port and logging path.

Example Usage:
Start Usage: /Users/Wenyu/Desktop/fibstarter -c ./fib.conf
Help Usage: /Users/Wenyu/Desktop/fibstarter -h
Query Link: http://127.0.0.1:8889/fib?n=100
Curl Link: curl -X GET http://127.0.0.1:8889/fib?n=-1
ATTENTION: Please be attention to use big N for the query, as it might take a while to return the result.
##############################
##############################
   ```
* Copy the configuration from `<download_path>/FibonacciServer/fibonacci/templates/fibonacci.conf.template` to the right place
* Change configurations
* Looking into the command usage by `<download_path>/fibstarter -h`

## Configuration
```
[http_server]
broadcast_address = 127.0.0.1
broadcast_port = 8889
fib_query_prefix = /fib

[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('fibonacci.log', 'w')

[formatter_simpleFormatter]
format=%(levelname)s %(asctime)s   %(name)s - %(message)s
datefmt=
```

## Logging
Default logging path will be `<download_path>/FibonacciServer/fibonacci.log`

Here is a sample log file's content:
```
DEBUG 2016-07-15 16:02:48,800   __main__ - Fibonacci Server Host Address: 127.0.0.1
DEBUG 2016-07-15 16:02:48,800   __main__ - Fibonacci Server Host Port: 8889
INFO 2016-07-15 16:02:54,607   fibonacci.handlers.basehttphandler - Got and starting to process request: /fib?n=1
INFO 2016-07-15 16:02:54,607   fibonacci.handlers.basehttphandler - Got Fibonacci Query Request with N=1
INFO 2016-07-15 16:02:54,607   fibonacci.handlers.basehttphandler - After Processing Fibonacci Query Request, and it takes 0.4 second(s) to generate fibonacci list.
INFO 2016-07-15 16:02:54,607   fibonacci.handlers.basehttphandler - Start Processing Response...
INFO 2016-07-15 16:02:54,608   fibonacci.handlers.basehttphandler - End Processing Response...It takes 0.000747919082642 second(s) to generate response.
INFO 2016-07-15 16:02:54,608   fibonacci.handlers.basehttphandler - End Processing Request...
INFO 2016-07-15 16:03:46,098   fibonacci.handlers.basehttphandler - Got and starting to process request: /fib?n=2
INFO 2016-07-15 16:03:46,098   fibonacci.handlers.basehttphandler - Got Fibonacci Query Request with N=2
INFO 2016-07-15 16:03:46,098   fibonacci.handlers.basehttphandler - After Processing Fibonacci Query Request, and it takes 3.09944152832e-06 second(s) to generate fibonacci list.
INFO 2016-07-15 16:03:46,098   fibonacci.handlers.basehttphandler - Start Processing Response...
INFO 2016-07-15 16:03:46,099   fibonacci.handlers.basehttphandler - End Processing Response...It takes 0.000212907791138 second(s) to generate response.
INFO 2016-07-15 16:03:46,099   fibonacci.handlers.basehttphandler - End Processing Request...
```

## Positive Test Cases
* URL: `http://127.0.0.1:8889/fib?n=1` / Output: `[0]`
* URL: `http://127.0.0.1:8889/fib?n=2` / Output: `[0, 1]`
* URL: `http://127.0.0.1:8889/fib?n=3` / Output: `[0, 1, 1]`
* URL: `http://127.0.0.1:8889/fib?n=10` / Output: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

## Negative Test Cases
* URL: `http://127.0.0.1:8889/fib?n=-1` / Output: `Failed when processing request: Negative N...`
* URL: `http://127.0.0.1:8889/fib` / Output: `Failed when processing request: N NOT Passed in...`
* URL: `http://127.0.0.1:8889/ffib?n=3` / Output: `Failed when processing request: Page Not Found`

## Unit Test Usage
`python <download_path>/FibonacciServer/test/fib_unittest.py`
