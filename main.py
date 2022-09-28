from selenium import webdriver
import time
from bs4 import BeautifulSoup
from time import sleep
from twilio.rest import Client
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import subprocess



def sendSMS():
    # enter all the details
    # get app_key and app_secret by registering
    # a app on sinchSMS
    account_sid = 'insert sid'
    auth_token = 'insert token'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    me = client.messages.create(
        from_='number from',
        body='what you want to tell',
        to='to who'
    )

    print(me.sid)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        s = Service("where to run selenium from")
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options, service=s)

        # get source code
        browser.get("insert page")
        html = browser.page_source
        time.sleep(10)

        web_html = BeautifulSoup(html, 'html5lib')
        grey_banner = web_html.find_all(text="what you want to search")
        text_is_empty = web_html.find_all(text="same")
        if grey_banner:
            try:
                grey_parent = grey_banner[0].parent
            except:
                continue
            else:
                # grey1_parent = grey1[0].parent
                # grey1_parent_class = grey1_parent['class']
                # print(grey_parent['class'])
                # print(grey1_parent_class)
                grey_parent_class = grey_parent['class']
                print(grey_parent_class + text_is_empty)
                if 'gray' not in grey_parent_class or not text_is_empty:
                    sendSMS()
        else:
            '''need to kill all the process - added bat file to run at the end'''
            browser.close()
            browser.quit()
            subprocess.call([r'bat file to close chrome processes '])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
