# File: Chamala_week10_web_services.py
# Author: Swetha Chamala
# Date: 11/04/19
# Course: DSC510 - Introduction to programming
# Description: Accepting user input and displaying Chuck Norris jokes
import requests
more_jokes = input("Would you like a Chuck Norris joke?: Y/N\n").lower()
while True:
    if more_jokes == 'y':
        response = requests.get("https://api.chucknorris.io/jokes/random").json()
        joke = (response.get("value"))
        print("Here is the random Chuck Norris joke for you:\n", joke)
        more_jokes = input("\nWould you like another Chuck Norris joke?: Y/N\n").lower()
    elif more_jokes == 'n':
        print("End of Chuck Norris jokes")
        break
    else:
        print("Please enter a valid input")
        more_jokes = input("\nWould you like a Chuck Norris joke?: Y/N\n").lower()
