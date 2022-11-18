import mysql.connector
import pandas
import os
from py_dotenv import read_dotenv
dotenv_path = os.path.join(os.path.dirname("../"), '.env')
read_dotenv(dotenv_path)
from multipledispatch import dispatch


class db_object(object):
	def __init__(self):
		self.db_name='faker'
        self.db_size='unlimit'
	def get_texture(self,sql):
		return pandas.read_sql(sql, self.MYDB).tolist()


	


