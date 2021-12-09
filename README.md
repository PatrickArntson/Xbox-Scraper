# Xbox-Scraper

This bot works by scraping BestBuy and GameStop to see if they have Xbox Series X in stock. If they are in stock, you will recieve a text message.

In order for you the get the notification, set the 'user' variable at the top of the script to your phone number in string format. 
Immediately following your phone number, attach the appropriate suffix to the end of your phone number according to your mobile carrier. 

Here are a list of the different carrierer's suffixes:

AT&T: @txt.att.net

T-Mobile: @tmomail.net

Sprint: @messaging.sprintpcs.com

Verizon: @vtext.com or @vzwpix.com

Virgin Mobile: @vmobl.com

For example, if you use Verizon your number would look like: user = '5030005555@vzwpix.com'


After Specifying the users, you must give an email that will send the alerts. To do this, set the 'email' and 'password' variables in the sendequal to your email with its corresponding password. 
*NOTE: If you're not using a gmail, you will also have to modify the SMTP setting (in the send_alert function) to your email service provider. 


With your phone number, email, and password specified you are ready to go! Just run the script and you will be notified if Xbox Series X's are in stock!
