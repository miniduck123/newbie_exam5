import pytest
import os
import time
import sys
#sys.path.append("./")
#sys.path.append("../")
from pytest_html_reporter import attach
import pandas
from multipledispatch import dispatch
from py_dotenv import read_dotenv
dotenv_path = os.path.join(os.path.dirname("../"), '.env')
read_dotenv(dotenv_path)
