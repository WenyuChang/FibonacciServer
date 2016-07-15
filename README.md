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
args=('/Users/Wenyu/Desktop/fib.log', 'w')

[formatter_simpleFormatter]
format=%(levelname)s %(asctime)s   %(name)s - %(message)s
datefmt=
```
