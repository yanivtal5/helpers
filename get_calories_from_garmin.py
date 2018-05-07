#Example for fetching the calories, can be used for other metrics as well
#using twill 
#prerequisites - cssselect , twill
#tested on 07-05-2018 

import datetime
from twill.commands import *

now = datetime.datetime.now()
year = now.year
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
current_date = str(year) + "-" + str(month) + "-" + str(day)

go("https://sso.garmin.com/sso/login?service=http%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&webhost=olaxpw-connect04.garmin.com&source=http%3A%2F%2Fconnect.garmin.com%2Fen-US%2Fsignin&redirectAfterAccountLoginUrl=http%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&redirectAfterAccountCreationUrl=http%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.0-min.css&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&usernameShown=true&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false#")

#fill in the data below according to your credentials in garmin connect site
fv("2","username","<USERNAME_OR_EMAIL>")
fv("2","password","<PASSWORD>")

submit()

#fill in the USER_ID, you will see it once you log in using the browser in a semiliar URL as below, simply copy and paste. its possible to get other metrics then calories
go("https://connect.garmin.com/modern/daily-summary/<USER_ID>/" + current_date + "/calories")

#page now contains the html page with all the data
page=show() 

#parsing example to extract the "totalKiloCalories" from the page, probably can do a better html parsing
calories_index=page.find("totalKiloCalories")
cal_str = page[calories_index:calories_index+25]
i_1 = cal_str.find(":")
i_2 = cal_str.find(",")

#cal contained the totalKiloCalories number
cal = cal_str[i_1 + 1:i_2]
