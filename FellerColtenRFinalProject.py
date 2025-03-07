"""
Author: Colten Feller
Date Written: January 30, 2025
Assignment: SDEV 140 M08 Final Project
Short Desc: This is a GUI application that allows you to search the weather of mulitple cities
"""

# import ruequired modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

# plug API key into url
config = ConfigParser()
apiKey = "b93bcbaf71ee4f58eb3a54b48fbe6b71"  # API key for the list of cities and their weather conditions
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# Function for weather details (city name and key)
def getWeather(city):
    result = requests.get(url.format(city, apiKey))

    if result:
        json = result.json()
        city = json["name"]
        country = json["sys"]["country"]
        tempKelvin = json["main"]["temp"]
        tempCelsius = tempKelvin - 273.15
        tempFahrenheit = (tempCelsius * 9 / 5) + 32
        weather1 = json["weather"][0]["main"]
        return [city, country, tempKelvin, tempCelsius, tempFahrenheit, weather1]
    
    else:
        return None

# Function to allow user to search a city
def search():
    city = cityText.get()
    weather = getWeather(city)
    if weather:
        locationLabel.config(text="{}, {}".format(weather[0], weather[1]))
        temperatureLabel.config(text="{:.2f}°C".format(weather[3]))
        temperatureLabel2.config(text="{:.2f}°F".format(weather[4]))
        weatherLabel.config(text="Weather: {}".format(weather[5]))
    else:
        messagebox.showerror("Error", "Cannot find {}".format(city))

# Function to open a new window and search new city to compare weather conditions
def openNewWindow():
    #create the new window that will open
    newWindow = Toplevel(app)
    # set the title of new window
    newWindow.title("Compare Weather")
    # set the size of the new window
    newWindow.geometry("350x250")
    # label for prompt for the user to type in the city name
    Label(newWindow, text="Enter city name:", font=("Arial", 12)).pack()

    # labels for the new window
    cityText2 = StringVar()
    cityEntry2 = Entry(newWindow, textvariable=cityText2)
    cityEntry2.pack() # entry for typing in a new city in the toplevel window
    locationLabel2 = Label(newWindow, text="Location: ", font=("Arial", 12, "bold"))
    locationLabel2.pack() # label for location (city and country)
    temperatureLabelC2 = Label(newWindow, text="Temperature (°C): ", font=("Arial", 12))
    temperatureLabelC2.pack() # label for temperature in degrees celsius
    temperatureLabelF2 = Label(newWindow, text="Temperature (°F): ", font=("Arial", 12))
    temperatureLabelF2.pack() # label for temperature in degrees fahrenheit
    weatherLabel2 = Label(newWindow, text="Weather: ", font=("Arial", 12))
    weatherLabel2.pack() # label for the weather label (ex. clouds or sunny)

    # Function to make new window labels
    def searchNewWindow():
        city = cityText2.get()
        weather = getWeather(city)
        if weather:
            locationLabel2.config(text="{}, {}".format(weather[0], weather[1]))
            temperatureLabelC2.config(text="Temperature (°C): {:.2f}".format(weather[3]))
            temperatureLabelF2.config(text="Temperature (°F): {:.2f}".format(weather[4]))
            weatherLabel2.config(text="Weather: {}".format(weather[5]))
        else:
            messagebox.showerror("Error", "Cannot find {}".format(city))

    # button for new window
    searchButton2 = Button(newWindow, text="Search", width=12, command=searchNewWindow)
    searchButton2.pack()
    exitButton2 = Button (newWindow, text="Exit", width=12, command=app.destroy)
    exitButton2.pack()

# Create main app window
app = Tk()
# add title
app.title("Weather App")
# add window size
app.geometry("350x450")

# Main window elements
cityText = StringVar()
Label(app, text="Enter city name:", font=("Arial", 12)).pack()
cityEntry = Entry(app, textvariable=cityText) # creates entry prompt for typing in city to search the weather of
cityEntry.pack() 
searchButton = Button(app, text="Search", width=12, command=search) # creates button to search city
searchButton.pack()
newWindowButton = Button(app, text="Open New City Entry", width=25, command=openNewWindow) # creates button that opens new window
newWindowButton.pack()
locationLabel = Label(app, text="Location", font=("Arial", 14, "bold")) # creates labelto show location (city and country)
locationLabel.pack()
temperatureLabel = Label(app, text="Temperature (°C): ", font=("Arial", 12)) # creates label to show degrees in celsius
temperatureLabel.pack()
temperatureLabel2 = Label(app, text="Temperature (°F): ", font=("Arial", 12)) # creates label to show degrees in fahrenheit
temperatureLabel2.pack()
weatherLabel = Label(app, text="Weather: ", font=("Arial", 12)) # creates label to show weather (ex. sunny or clouds)
weatherLabel.pack()
exitButton = Button (app, text="Exit", width=12, command=app.destroy)
exitButton.pack()

# run application
app.mainloop()
