'''
Created on Feb 6, 2018
'''

from selenium import webdriver
import csv


def parseFile(fname):
    # assumption the csv file is in the same folder
    with open(fname, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        for line in csv_reader:
            print(line)


def openSite(url):
    '''open site here and do stuff'''
    # url='https://primoco.me/app/booking'
    # browser = webdriver.Chrome()
    # browser.get(url)


def main():
    openSite('http')
    parseFile('sample.csv')


if __name__ == '__main__':
    main()
