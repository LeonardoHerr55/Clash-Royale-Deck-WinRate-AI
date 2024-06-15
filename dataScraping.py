import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://statsroyale.com/decks/top200")

seenPlayers = {}

def searchPlayerBattles(link):
    link = f"{link}/battles"
    driver.get(link)

    for battle in driver.find_elements(By.CLASS_NAME, "replays__replay"):
        continue #FINISH THIS


for element in driver.find_elements(By.CLASS_NAME, "recentWinners__cell"):
    id = element.find_element(By.XPATH, ".//*[contains(@class, 'ui__headerExtraSmall ui__link')]")
    id = id.get_attribute("href")
    
    if id in seenPlayers:
        continue
    else:
        seenPlayers[id] = 1

    


    print(id)