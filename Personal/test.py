'''
Created on Feb 6, 2018

@author: blackmamba
'''
#Test chromium webdriver
import time
from selenium import webdriver


def main():
    driver = webdriver.Chrome(r'C:\Users\blackmamba\AppData\Local\Programs\Python\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/xhtml');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    driver.quit()

if __name__ == '__main__':
    main()