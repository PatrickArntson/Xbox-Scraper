# Xbox-Scraper

This bot works by scraping BestBuy and GameStop to see if they have Xbox Series X in stock. If they are in stock, you will recieve a text message.

In order for you the get the notification, set the 'user' variable at the top of the script to your phone number in string format. 
Immediately following your phone number, attach the appropriate suffix to the end of your phone number according to your mobile carrier. 

Here are a list of the different carrierer's suffixes:

AT&T: phonenumber@txt.att.net

T-Mobile: phonenumber@tmomail.net

Sprint: phonenumber@messaging.sprintpcs.com

Verizon: phonenumber@vtext.com or phonenumber@vzwpix.com

Virgin Mobile: phonenumber@vmobl.com

For example, if you use Verizon your number would look like: user = '5030005555@vzwpix.com'
