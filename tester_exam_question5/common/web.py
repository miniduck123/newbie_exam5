from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.actions.key_actions import KeyActions as KA
from selenium.webdriver.common.actions.pointer_actions import PointerActions as PA
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support import expected_conditions as EC
from pytest_html_reporter import attach

class web(object):
	"""docstring for ClassName"""
	def __init__(self,url):				
		self.driver = webdriver.Chrome()
		self.driver.get(url)
		self.waiter  = WebDriverWait(self.driver, timeout=10, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

	def click_element_by_id(self,_id):
		try:
			element = self.waiter.until(EC.element_to_be_clickable((By.ID,_id)))	
			element.click()	
		except Exception as e:
			raise e		
		return element

	def click_element_by_class(self,_class):
		try:
			element = self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME,_class)))	
			element.click()	
		except Exception as e:
			raise e		
		return element
	def click_element_by_tag(self,_tag):
		try:
			element = self.waiter.until(EC.element_to_be_clickable((By.TAG_NAME,_tag)))	
			element.click()	
		except Exception as e:
			raise e		
		return element

	def click_element_by_xpath(self,path):
		try:
			element = self.waiter.until(EC.element_to_be_clickable((By.XPATH,path)))	
			element.click()	
		except Exception as e:
			raise e 

	def get_element_by_xpath(self,path):
		try:
			element = self.driver.find_element(By.XPATH,path)	
		except Exception as e:
			raise e
		return element

	def get_element_by_id(self,_id):
		try:
			element = self.driver.find_element(By.ID,_id)	
		except Exception as e:
			raise e
		return element
	def get_element_by_class(self,_class):
		try:
			element = self.driver.find_element(By.CLASS_NAME,_class)	
		except Exception as e:
			raise e
		return element
	def get_element_by_tag(self,_tag):
		try:
			element = self.driver.find_element(By.TAG_NAME,_tag)	
		except Exception as e:
			raise e
		return element	



	def get_elements_by_xpath(self,path):
		try:
			element = self.driver.find_elements(By.XPATH,path)	
		except Exception as e:
			raise e
		return element
	def get_elements_by_tag(self,_tag):
		try:
			element = self.driver.find_elements(By.TAG_NAME,_tag)	
		except Exception as e:
			raise e
		return element

		
	def send_texture(self,texture):		
		pass

	def maximize_window(self):
		self.driver.maximize_window()

	def get_screen_shot(self):
		attach(data=self.driver.get_screenshot_as_png())
	def clean_cookies(self):
		self.driver.delete_all_cookies()
	def refresh(self):
		self.driver.refresh()	
	def get(self,url):
		self.driver.get(url)
	def close(self):
		self.driver.quit()

