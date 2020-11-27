import urllib.request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from bs4 import BeautifulSoup

# NOTE: Edit executable path for your specific computer.
driver = driver = webdriver.Chrome(executable_path='/home/zhouaea/Documents/ChromeDriver/chromedriver')

# NOTE: Lower is id=21, Carney is id=23, Stuart is id=28
url = "https://www.bc.edu/bc-web/offices/auxiliary-services/sites/dining/locations/dining-menus.html?id=0"
html = urllib.request.urlopen(url).read()
driver.implicitly_wait(10)
driver.get(url)

""" Fill out form with restaraunt and date """
# Find drop down items.
dropdown = driver.find_element_by_id('dining-area-options')
# Select Items from Dropdown
item = driver.find_element_by_xpath('//*[@id="dining-area-options"]/option[2]')
item.click()

# Click Submit Button
submit_btn = '//*[@id="menu-refresh-button"]'
driver.find_element_by_xpath(submit_btn).click()

# Gather lunch, breakfast, dinner tabs.
breakfeast = driver.find_element_by_xpath('//*[@id="session-tab-ul"]/li[1]')
lunch = driver.find_element_by_xpath('//*[@id="session-tab-ul"]/li[2]')
dinner = driver.find_element_by_xpath('//*[@id="session-tab-ul"]/li[3]')
mealSessions = []
mealSessions.append(breakfeast)
mealSessions.append(lunch)
mealSessions.append(dinner)

# Store an array of dictionaries, where each dictionary has the nutrition facts for an item.
food = []

for meal in mealSessions:
    # Select breakfast, lunch, or dinner time period
    meal.click()
    # Refresh page
    pageSource = driver.page_source
    # Store page.
    soup = BeautifulSoup(pageSource, 'lxml')

    # Gather food links.
    # recipeList = driver.find_elements_by_xpath("//class[contains(text(), 'recipe-button')]")
    recipeList = driver.find_elements_by_class_name("recipe-button")
    print("Recipe List:", recipeList)
    print(type(recipeList))

    # TODO: This logic does not work properly. It will obtain all breakfast items but when the lunch tab is clicked it will try to access the invisible breakfast items again and break early.
    for recipe in recipeList:
        # Click food link.
        time.sleep(2)
        try:
            recipe.click()
        except:
            break
        # Refresh page
        pageSource = driver.page_source
        # Store page.
        soup = BeautifulSoup(pageSource, 'lxml')

        # Extract all span tags from webpage, which will contain nutrition facts for a single item.
        spans = soup.findAll("span", id=lambda x: x and x.startswith('nutrition'))

        # Clear nutrition facts dictionary.
        nutritionfacts = {}

        # Add nutrition facts to a dictionary
        for span in spans:
            if span['id'] == "nutrition-Serving-Size":
                nutritionfacts["Serving Size"] = span.string
            if span['id'] == "nutrition-Servings_Per_Container":
                nutritionfacts["Servings per container"] = span.string

            if span['id'] == "nutrition-Calories":
                nutritionfacts["Calories"] = span.string

            if span['id'] == "nutrition-Total_Carb":
                nutritionfacts["Total Carbs"] = span.string

            if span['id'] == "nutrition-Total_Fat":
                nutritionfacts["Total Fat"] = span.string
            if span['id'] == "nutrition-Sat_Fat":
                nutritionfacts["Saturated Fat"] = span.string
            if span['id'] == "nutrition-Servings_Per_Container":
                nutritionfacts["Polyunsaturated Fat"] = span.string
            if span['id'] == "nutrition-Servings_Per_Container":
                nutritionfacts["Monosaturated Fat"] = span.string
            if span['id'] == "nutrition-Trans_Fat":
                nutritionfacts["Trans Fat"] = span.string

            if span['id'] == "nutrition-Dietary_Fiber":
                nutritionfacts["Dietary Fiber"] = span.string

            if span['id'] == "nutrition-Sugars":
                nutritionfacts["Sugars"] = span.string

            if span['id'] == "nutrition-Protein":
                nutritionfacts["Protein"] = span.string

            if span['id'] == "nutrition-Potassium":
                nutritionfacts["Potassium"] = span.string

            if span['id'] == "nutrition-Sodium":
                nutritionfacts["Sodium"] = span.string

            if span['id'] == "nutrition-Cholesterol":
                nutritionfacts["Cholesterol"] = span.string

            nutritionfacts["Vitamin A "] = "N/A"

            if span['id'] == "nutrition-Calcium":
                nutritionfacts["Calcium"] = span.string

            nutritionfacts["Vitamin C"] = "N/A"

            if span['id'] == "nutrition-Iron":
                nutritionfacts["Iron"] = span.string

        print("Nutrition facts: ", nutritionfacts)

        # Add food nutrition facts to list of food items.
        food.append(nutritionfacts)
        exit_btn = '//*[@id="nutritional-pop-upContent"]/div[1]/button'
        driver.find_element_by_xpath(exit_btn).click()

print("Food list:", food)
