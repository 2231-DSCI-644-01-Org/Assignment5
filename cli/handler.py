## This file is the handler for the CLI. It is responsible for parsing the command line arguments and calling the appropriate functions from the scraper and issue_parser modules. It is also responsible for printing the output to the console.
'''
This file is the handler for the CLI. 
It is responsible for parsing the command line arguments and calling the appropriate functions from the scraper and issue_parser modules. 
It is also responsible for printing the output to the console.
'''

import argparse
import sys
import os
import click
from scraper import Scraper

class CLIHandler