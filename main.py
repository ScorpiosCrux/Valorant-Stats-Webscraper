# Written by Tyler Chen
# Webscraper that scrapes data from tracker.gg
# Refer to README.md for more information
# Feel free to copy this code, used personally.
# Be careful with rate limits if you have more than 5 accounts!

from ast import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

#CONVERT USERNAMES TO HTML ENCODED. This means # are converted to %23.
#https://www.w3schools.com/tags/ref_urlencode.asp 
usernames = [
    'VividEradicator%23NA1',
    'anotherUsername%23numbers',
]

#URLS for each game type
urls = {
    "comp": "https://tracker.gg/valorant/profile/riot/{}/overview?season=all",
    "dm": "https://tracker.gg/valorant/profile/riot/{}/overview?playlist=deathmatch&season=all",
    "unrated": "https://tracker.gg/valorant/profile/riot/{}/overview?playlist=unrated&season=all",
    "spike": "https://tracker.gg/valorant/profile/riot/{}/overview?playlist=spikerush&season=all",
    "escalation": "https://tracker.gg/valorant/profile/riot/{}/overview?playlist=escalation&season=all",
    "replication": "https://tracker.gg/valorant/profile/riot/{}/overview?playlist=replication&season=all"
}

#Get the URL, you can add exception handling here or even assertions
def getURL(url):
    driver.get(url)

#Input username encoded
def getPlayTime(username):
    elems = {}
    for gameType in urls:
        currentURL = urls.get(gameType).format(username)
        getURL(currentURL)
        try:
            elem = driver.find_element(By.CLASS_NAME, 'playtime')
            elems[gameType] = (elem.text)
        except NoSuchElementException as e:
            print("playtime class does not exist. Please check classname, url and username!")
    return elems

# Parses the strings returned from getPlayTime()
# Returns total num of hours played as int
def parsePlayTime(elems):
    totalHours = 0
    for gameType in elems:
        try:
            playTimeRaw = elems.get(gameType)
            playTimeSplit = playTimeRaw.split('h')  #split on h 
            totalHours += int(playTimeSplit[0])     #grab first element
        except:
            print("error parsing. Play time data: " + elems.get(gameType))      #if you have played less than an hour, we don't add
    return totalHours


# Main: 
totalHoursPlayed = 0
for username in usernames:
    elems = getPlayTime(username)
    totalHoursPlayed += parsePlayTime(elems)
    print(username + " Total Hours Played: " + str(totalHoursPlayed) + " hours.")

print("Done!")
driver.close() # Closes the window