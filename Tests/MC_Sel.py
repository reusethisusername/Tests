'''
Created on Feb 6, 2018
'''

from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    browser.get('https://primoco.me/app/booking')


if __name__ == '__main__':
    main()
