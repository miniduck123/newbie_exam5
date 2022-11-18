from __init__ import *
from common.sub_web import *
from common.db_object import *
from common.api_object import *


page_url = os.getenv("DOMAIN")#test  stackoverflow search bar from https://stackoverflow.com/
test_text = db_object().get_texture(testing_input_text.sql)


@pytest.fixture(scope='module')
def driver():
	driver = sub_web(page_url)
	yield driver
	driver.close()

	
@pytest.fixture(scope='function',params = test_text)
def web_page():	
	driver.send_texture(request.param)
	driver.get(page_url)
	yield {'driver':driver,'test_text':request.param}
	
	

def searching_test(web_page):
	web_page.click_element_by_xpath('//input[@name='q']')
	assert 'https://stackoverflow.com/nocaptcha?s=' in driver.current_url()
	assert web_page.title_contains("Human verification")


	


		




