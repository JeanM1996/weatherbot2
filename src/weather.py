"""
Name   : Loren Davies
Project: WeatherBot2
Date   : November 28th, 2017
"""

# Imports
from datetime import datetime
import forecastio
from twython import Twython


def london():
    # Local constants
    city = "london"

    # Local variables

    # ******** start london() ******** #
    inst = createTwitter(city)
    twitter = inst[0]
    weather = inst[1]

    msg = getTweet(weather, city)
    msg += "#London #LondonWeather"
    print(msg)
    twitter.update_status(status=msg)


def syracuse():
    # Local constants
    city = "syracuse"

    # Local variables

    # ******** start syracuse() ******** #
    inst = createTwitter(city)
    twitter = inst[0]
    weather = inst[1]

    msg = getTweet(weather, city)
    msg += "#Syracuse #SyracuseWeather"
    print(msg)
    twitter.update_status(status=msg)


def rochester():
    # Local constants
    city = "rochester"

    # Local variables

    # ******** start rochester() ******** #
    inst = createTwitter(city)
    twitter = inst[0]
    weather = inst[1]

    msg = getTweet(weather, city)
    msg += "#Rochester #RochesterWeather"
    print(msg)
    twitter.update_status(status=msg)


def buffalo():
    # Local constants
    city = "buffalo"

    # Local variables

    # ******** start buffalo() ******** #
    inst = createTwitter(city)
    twitter = inst[0]
    weather = inst[1]

    msg = getTweet(weather, city)
    msg += "#Buffalo #BuffaloWeather"
    print(msg)
    twitter.update_status(status=msg)


def createTwitter(city):
    # Local constants

    # Local variable
    consumerKey = ""    # Twitter
    consumerKeySecret = ""
    accessToken = ""
    accessTokenSecret = ""
    apiKey = ""  # ForecastIO
    lat = ""
    lng = ""
    count = 0
    ret = []

    # ******** start createTwitter() ******** #

    # Get keys from file
    f = open(city + "Keys.txt", "r")
    for line in f:
        line = line.strip()
        if line[0] == "#":
            continue
        if count == 0:
            consumerKey = line
        elif count == 1:
            consumerKeySecret = line
        elif count == 2:
            accessToken = line
        elif count == 3:
            accessTokenSecret = line
        elif count == 4:
            apiKey = line
        elif count == 5:
            lat = float(line)
        elif count == 6:
            lng = float(line)
        count += 1
    f.close()

    # Create an instance of Twython and ForecastIO
    twitter = Twython(consumerKey, consumerKeySecret, accessToken, accessTokenSecret)
    weather = forecastio.load_forecast(apiKey, lat, lng)

    ret.append(twitter)
    ret.append(weather)

    return ret


def getTweet(weather, city):
    # Local constants

    # Local variables

    # ******** start getTweet() ******** #

    time = getHour(city)
    current = weather.currently()
    summary = str(current.summary)
    temp = int(current.temperature)
    feels = int(current.apparentTemperature)
    summary = getSummary(summary)

    if city == "london":
        msg = str(time) + " - " + "It\'s " + str(temp) + "C out (feels like " + str(feels) + "C), "
    else:
        msg = str(time) + " - " + "It\'s " + str(temp) + "F out (feels like " + str(feels) + "F), "

    msg += summary

    return msg


def getSummary(summary):
    # Local constants

    # Local varaibles

    # ******** start getCurrent() ******** #

    if summary == 'Overcast':
        summary = "and there\'s currently an overcast. "

    elif summary == 'Light Snow':
        summary = "and it\'s lightly snowing. "

    elif summary == 'Snow':
        summary = "and it\'s snowing. Drive carefully! "

    elif summary == 'Foggy':
        summary = "and it\'s foggy. *Fog horn* "

    elif summary == 'Drizzle':
        summary = "and it\'s drizzling. "

    elif summary == 'Light Rain':
        summary = "and it\'s lightly raining. "

    elif summary == 'Mostly Cloudy':
        summary = "and it\'s mostly cloudy. "

    elif summary == 'Flurries':
        summary = "with a few flurries. "

    elif summary == 'Partly Cloudy':
        summary = "and it\'s partly cloudy. "

    elif summary == 'Clear':
        summary = "and it\'s currently clear! "

    elif summary == 'Rain':
        summary = "and it\'s currently raining. "

    elif summary == 'Heavy Snow':
        summary = "and it\'s snowing heavily. "

    elif summary == 'Heavy Rain':
        summary = "and it\'s currently heavily raining. "

    elif summary == 'Humid and Overcast':
        summary = "and it\'s currently humid with an overcast. "

    elif summary == "Light Sleet":
        summary = "and it\'s lightly sleeting. "

    elif summary == "Breezy and Mostly Cloudy":
        summary = "and it\'s currently breezy and mostly cloudy. "

    elif summary == "Windy and Mostly Cloudy":
        summary = "and it\'s currently windy and mostly cloudy. "

    elif summary == "Possible Drizzle":
        summary = "and it\'s possibly drizzling. "

    elif summary == "Windy and Partly Cloudy":
        summary = "and it\'s currently windy and partly cloudy."

    elif summary == "Breezy and Partly Cloudy":
        summary = "and it\'s currently breezy and partly cloudy."

    elif summary == "Possible Light Rain":
        summary = "and there\'s a possible light rain."

    elif summary == "Windy":
        summary = "and it\'s currently windy."

    elif summary == "Breezy and Overcast":
        summary = "and it\'s currently breezy with an overcast."

    elif summary == "Sleet":
        summary = "and it\'s currently sleeting."

    elif summary == "Light Rain and Breezy":
        summary = "and it\'s currently lightly raining with a light breeze."

    elif summary == "Humid and Mostly Cloudy":
        summary = "and it\'s currently humid and mostly cloudy."

    elif summary == "Rain and Breezy":
        summary = "and it\'s currently raining and breezy."

    elif summary == "Heavy Rain and Breezy":
        summary = "and it\'s currently heavily raining and breezy."

    elif summary == "Breezy":
        summary = "and it\'s currently breezy."

    elif summary == "Drizzle and Breezy":
        summary = "and it\'s currently drizzling and breezy."

    elif summary == "Humid":
        summary = "and it\'s currently humid."

    elif summary == "Humid and Partly Cloudy":
        summary = "and it\'s currently humid and partly cloudy."

    elif summary == "Drizzle and Windy":
        summary = "and it\'s currently windy and drizzling."

    elif summary == "Light Rain and Windy":
        summary = "and it\'s currently windy and lightly raining."

    elif summary == "Possible Light Snow":
        summary = "and it\'s possibly lightly snowing."

    elif summary == "Light Snow and Breezy":
        summary = "and it\'s currently breezy and lightly snowing."

    elif summary == "Breezy and Foggy":
        summary = "and it\'s currently breezy and foggy."

    elif summary == "Drizzle and Windy":
        summary = "and it\'s currently windy and drizzling."

    elif summary == "Windy and Overcast":
        summary = "and it\'s currently windy with an overcast."

    elif summary == "Possible Flurries":
        summary = "and there\'s possible flurries."

    else:
        summary += " @trevordavies095 "

    return summary


def getHour(city):
    # Local constants

    # Local variables
    now = datetime.now()
    hour = now.hour

    # ******** start getHour() ******** #

    if city == "london":
        hour += 5
        if hour >= 24:
            hour -= 24
        return str(hour) + ":00"

    if hour == 0:
        hour = "12:00 AM"
    elif hour == 1:
        hour = "1:00 AM"
    elif hour == 2:
        hour = "2:00 AM"
    elif hour == 3:
        hour = "3:00 AM"
    elif hour == 4:
        hour = "4:00 AM"
    elif hour == 5:
        hour = "5:00 AM"
    elif hour == 6:
        hour = "6:00 AM"
    elif hour == 7:
        hour = "7:00 AM"
    elif hour == 8:
        hour = "8:00 AM"
    elif hour == 9:
        hour = "9:00 AM"
    elif hour == 10:
        hour = "10:00 AM"
    elif hour == 11:
        hour = "11:00 AM"
    elif hour == 12:
        hour = "12:00 PM"
    elif hour == 13:
        hour = "1:00 PM"
    elif hour == 14:
        hour = "2:00 PM"
    elif hour == 15:
        hour = "3:00 PM"
    elif hour == 16:
        hour = "4:00 PM"
    elif hour == 17:
        hour = "5:00 PM"
    elif hour == 18:
        hour = "6:00 PM"
    elif hour == 19:
        hour = "7:00 PM"
    elif hour == 20:
        hour = "8:00 PM"
    elif hour == 21:
        hour = "9:00 PM"
    elif hour == 22:
        hour = "10:00 PM"
    elif hour == 23:
        hour = "11:00 PM"

    return hour


def main():
    # Local constants

    # Local variables

    # ******** start main() ******** #

    syracuse()
    rochester()
    buffalo()
    london()


if __name__ == "__main__": main()
