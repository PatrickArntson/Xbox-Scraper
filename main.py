import os
import requests
import bs4
import smtplib
from email.message import EmailMessage
import time
from dotenv import load_dotenv
start_time = time.time()
load_dotenv()

# Alert message
alert = 'XBOX SERIES X IN STOCK AT: '

# Users (can add as many users as you wish)
user = 'YOUR NUMBER WITH CORRESPONDING SUFFIX HERE'

# Email and password for sending the SMS alerts
email = 'YOUR EMAIL HERE'
password = 'YOUR PASSWORD HERE'


# Settings for Best Buy
bestbuy_url = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
bestbuy_container = "div"
bestbuy_key = {"class":"fulfillment-add-to-cart-button"}
bestbuy_in_stock = 'data-button-state="ADD_TO_CART"'
bestbuy_out_of_stock = 'data-button-state="SOLD_OUT"'


# Settings for GameStop
gamestop_url = 'https://www.gamestop.com/products/microsoft-xbox-series-x/224744.html'
gamestop_container = "button"
gamestop_key = {"id":"add-to-cart"}
gamestop_in_stock = 'Add to Cart'
gamestop_out_of_stock = 'Unavailable'


class ConnectError(Exception):
    pass


def extract_source(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    source = requests.get(url, headers=agent).text
    return source


def extract_data(source, container, key, in_stock):
    soup = bs4.BeautifulSoup(source, 'lxml')
    cart = soup.find(container, key)
    if in_stock in str(cart.contents[0]):
        return True
    return False


def send_alert(message, recipient, url):
    body = message + url
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = 'ALERT'
    msg['from'] = email
    msg['to'] = recipient

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)

    server.quit()


def run():
    run_count = 0
    while True:

        # prints message to console once every minute
        if run_count % 4 == 0:
            print('Running for ' + str(int(run_count/4)) + ' minutes: Still Scraping...')

        # max get request timeout
        if run_count % 450 == 0:
            time.sleep(120)

        try:
            bestbuy = extract_data(extract_source(bestbuy_url), bestbuy_container, bestbuy_key, bestbuy_in_stock)
            if bestbuy:
                # If there are multiple users, call this function for every user you desire with their names in the 'user' variable
                send_alert(alert, user, bestbuy_url)

            gamestop = extract_data(extract_source(gamestop_url), gamestop_container, gamestop_key, gamestop_in_stock)
            if gamestop:
                # If there are multiple users, call this function for every user you desire with their names in the 'user' variable
                send_alert(alert, user, gamestop_url)

            # wait 15 seconds to check websites again
            time.sleep(15)
            run_count += 1

        except ConnectError:
            err = 'Connection Error has occurred after ' + str(run_count/4) + ' minutes.'
            send_alert(err, user, None)
            print("Problem Establishing Connection")
            continue


if __name__ == "__main__":
    run()

