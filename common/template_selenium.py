import json
import random
import time
import logging
from selenium import webdriver
import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options




def webdriver_standard(headless_choice):
    global browser

    APP_NAME = "INITIALIZING SOLO WEBDRIVER"
    log = logging.getLogger(APP_NAME)
    info = log.info
    start = time.time()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.StreamHandler(sys.stdout)])

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    options = Options()
    BLACK_LIST_FILENAME = "bots/bot_ATENDE_NET/config/BAD_PROXY_LIST.txt"

    options.headless = headless_choice
    browser = webdriver.Firefox( options=options,
                                capabilities=firefox_capabilities)  # starta driver
    return browser





