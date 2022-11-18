from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.actions.key_actions import KeyActions as KA
from selenium.webdriver.common.actions.pointer_actions import PointerActions as PA
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support import expected_conditions as EC
import os


class seb_web():
	def current_url():
		return self.driver.current_url

	def title_contains(title):
		return self.driver.title == title
			
		


