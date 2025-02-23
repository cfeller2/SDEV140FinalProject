"""
Author: Colten Feller
Date Written: January 30, 2025
Assignment: Final Project
Short Description: This program will open a GUI that will provide the weather when you input the city/country.
"""

# import ruequired modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key form configuration file
configFile = "config.ini"
config = ConfigParser()
config.read(configFile)
apiKey = "b93bcbaf71ee4f58eb3a54b48fbe6b71"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# function for weather details (city name and key)
def getWeather(city):
    result = requests.get(url.format(city, apiKey))

    if result:
        json = result.json()
        city = json["name"]
        country = json["sys"]
        tempKelvin = json["main"]["temp"]
        tempCelsius = tempKelvin-273.15
        tempFahrenheit = (tempCelsius*9/5) + 32
        weather1 = json["weather"][0]["main"]
        final = [city, country, tempKelvin, tempCelsius, tempFahrenheit, weather1]
        return final
    else:
        print("Error Finding Weather")

# function to search city
def search():
    city = cityText.get()
    weather = getWeather(city)
    if weather:
        locationLabel["text"] = "{} ,{}".format(weather[0], weather[1])
        temperatureLabel["text"] = str(weather[3])+"  Degree Celsius"
        weatherLabel["text"] = weather[4]
    else:
        messagebox.showerror("Error, Cannot find {}".format(city))

# create object
app = Tk()

# add title
app.title("Weather App")

# create window size
app.geometry("250x350")

# add labels, buttons, and text
cityText = StringVar()
cityEntry = Entry(app, textvariable=cityText)
cityEntry.pack()
searchButton = Button(app, text="Search Weather",
                      width=12, command=search)
searchButton.pack()
locationLabel = Label(app, text="Location",
                      font={"bold", 20})
locationLabel.pack()
temperatureLabel = Label(app, text="")
temperatureLabel.pack()
weatherLabel = Label(app, text="")
weatherLabel.pack()

app.mainloop()
