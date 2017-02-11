"""
Name   : Loren Davies
Project: WeatherBot2 ~ Beta
Date   : February 11th, 2017
"""

# Imports
from datetime import datetime
import forecastio
from twython import Twython


def london():

    # Local constants
    city = "london"

    # Local variables
    consumerKey       = ""      # Twitter
    consumerKeySecret = ""
    accessToken       = ""
    accessTokenSecret = ""

    apiKey            = ""      # ForecastIO
    lat               = ""
    lng               = ""

    count = 0

    # ******** start london() ******** #

    # Get keys from file
    f = open(city + "Keys.txt", "r")

    for line in f:

        line = line.strip()

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

    # Create an instance of Twython and ForecastIO
    twitter = Twython(consumerKey, consumerKeySecret, accessToken, accessTokenSecret)
    weather = forecastio.load_forecast(apiKey, lat, lng)

    current = weather.currently()
    summary = str(current.summary)

    twitter.update_status(status=summary)


def main():

    # Local constants

    # Local variables

    # ******** start main() ******** #

    london()


if __name__ == "__main__": main()