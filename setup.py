#!/usr/bin/env python


import sys, os
from subprocess import call
from setuptools.command.install import install
from setuptools import setup, find_packages

# PQ package information
PACKAGE_NAME = 'Fibonacci Server'
PACKAGE_VERSION = '0.9'
PACKAGE_DESCRIPTION = 'Restful Service for Fibonacci Query'
PACKAGE_MAINTAINER = 'Wenyu Chang'
PACKAGE_MAINTAINER_EMAIL = 'changewy_1987@hotmail.com'

class Installer(install):
    """
    Run the default setuptools install plus install correct bits in PQ home folder
    """

    def _create_bin(self):
        self.source_bin_config = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fibonacci', 'templates', 'fibstarter')
        self.target_bin_config = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fibstarter')

        with open(self.target_bin_config, "wb") as f_conf:
            f_conf.write(open(self.source_bin_config).read())
        os.system('chmod +x %s' % self.target_bin_config)

    def run(self):
        # Umcomment this line only if pip is installed properly
        # call(["pip install -r requirements.txt --no-clean"], shell=True)

        install.run(self)
        self._create_bin()

        print
        print '#'*30
        print '#'*30
        print 'Prepare before Start:'
        print '1. Copy configuation file from %s' % os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fibonacci', 'templates', 'fibonacci.conf.template')
        print '2. Change configuration, such as HTTP server host/port and logging path.'
        print
        print 'Example Usage:'
        print 'Start Usage: %s -c ./fib.conf' % self.target_bin_config
        print 'Help Usage: %s -h' % self.target_bin_config
        print 'Query Link: %s' % 'http://127.0.0.1:8889/fib?n=100'
        print 'Curl Link: %s' % 'curl -X GET http://127.0.0.1:8889/fib?n=-1'
        print 'ATTENTION: Please be attention to use big N for the query, as it might take a while to return the result.'
        print '#'*30
        print '#'*30
        print


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=PACKAGE_DESCRIPTION,
    maintainer=PACKAGE_MAINTAINER,
    maintainer_email=PACKAGE_MAINTAINER_EMAIL,
    packages=find_packages(),
    install_requires=[
        'argparse>=1.4.0',
    ],
    package_data={
        'fibonacci.templates' : ['*.template'],
    },
    cmdclass={
        'install': Installer,
    },
)

