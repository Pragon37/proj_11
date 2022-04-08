from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("http://127.0.0.1:5000")
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("kate@shelifts.co.uk")
button = driver.find_element(by=By.XPATH, value="/html/body/form/button")
button.click()
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)

pointsSymplyLift = driver.find_element(
    by=By.TAG_NAME, value="body > ul > li:nth-child(1)"
)
pointsAvailable = driver.find_element(by=By.TAG_NAME, value="body > ul:nth-child(3)")

print("Available", pointsAvailable.text)
numberOfPlaces = re.search((r"Number of Places: (\d+)"), pointsSymplyLift.text).group(1)
numberOfPoints = re.search((r"Points available: (\d+)"), pointsAvailable.text).group(1)
print("PLACES --", numberOfPlaces, "POINTS :", numberOfPoints)
buttonShowSummary = driver.find_element(by=By.XPATH, value="/html/body/form/button")
buttonShowSummary.click()
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)
pointsSymplyLift = driver.find_element(by=By.TAG_NAME, value="li:nth-child(1)")
print(pointsSymplyLift.text)
pointsIronTemple = driver.find_element(by=By.TAG_NAME, value="li:nth-child(3)")
print(pointsIronTemple.text)
pointsSheLifts = driver.find_element(by=By.TAG_NAME, value="li:nth-child(5)")
print(pointsSheLifts.text)

buttonPoints = driver.find_element(by=By.XPATH, value="/html/body/form/button")
buttonPoints.click()
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)

bookPlacesLinkText = driver.find_element(by=By.LINK_TEXT, value="Book Places")
bookPlacesLinkText.click()

places = driver.find_element(by=By.NAME, value="places")
places.send_keys(4)
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)
buttonBook = driver.find_element(by=By.XPATH, value="/html/body/form/button")
buttonBook.click()
print("TITLE : ", driver.title)
print("CURRENT_URL : ", driver.current_url)
# logoutLinkText = driver.find_element(by=By.LINK_TEXT, value="Logout")
# logoutLinkText.click()

pointsSymplyLift = driver.find_element(
    by=By.TAG_NAME, value="body > ul:nth-child(6) > li:nth-child(1)"
)
print(pointsSymplyLift.text)
if int(numberOfPoints) - 4 < 0:
    assert (
        pointsSymplyLift.text
        == f"Spring Festival\nDate: 2022-05-27 10:00:00\nNumber of Places: {int(numberOfPlaces)} Book Places"
    )
else:
    assert (
        pointsSymplyLift.text
        == f"Spring Festival\nDate: 2022-05-27 10:00:00\nNumber of Places: {int(numberOfPlaces) - 4} Book Places"
    )
logoutLinkText = driver.find_element(by=By.LINK_TEXT, value="Logout")
logoutLinkText.click()
driver.close()
