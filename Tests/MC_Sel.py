'''
Created on Feb 6, 2018
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import csv
import getpass


def parseFile(fname):
    # assumption the csv file is in the same folder
    # header Date;Type;Amount;Currency;Category;Person;Account;Counter Account;Group;Note
    # with open(fname, 'r') as csv_file:
    #     csv_reader = csv.DictReader(csv_file, delimiter=";")

    #     for line in csv_reader:
    #         date = datetime.strptime(line['Date'], '%d/%m/%Y')
    #         #print(line['Date'] + "  " + str(date))

    #         amount = int(line['Amount'][:-3].replace(".", ""))  # strips the trailing 0s and removes the .
    #         #print(line['Amount'] + "  " + str(amount))
    #         print(line)
    pass


def openSite(url):
    '''open site here and do stuff'''
    # x = getpass.getpass('Password:')
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    # Log in
    u = browser.find_element_by_css_selector('#username')
    u.clear()
    u.send_keys('noname@bogusmail.com')
    p = browser.find_element_by_css_selector('#password')
    p.clear()
    p.send_keys('pass')  # or use getpass()
    b = browser.find_element_by_css_selector('#_submit')
    b.click()
    assert "Overview" in browser.title

    # go to Entries
    browser.find_element_by_css_selector('#app-menu-navbar-collapse > ul > li.app-menu-booking > a').click()
    assert "app_booking_list_page" in browser.page_source


def main():
    openSite('https://primoco.me/en/')
    # parseFile('sample.csv')


if __name__ == '__main__':
    main()
