import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import createCustomerData
from randomHelper import RandomHelper
from selenium.webdriver.support import expected_conditions as EC


randomHelper = RandomHelper()

def logIn(driver):
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(createCustomerData.loginField).send_keys(createCustomerData.loginData)
    driver.find_element_by_xpath(createCustomerData.passwordField).send_keys(createCustomerData.passwordData)
    driver.find_element_by_xpath(createCustomerData.loginButton).click()
    driver.implicitly_wait(10)



def customerNameFill(driver, requiredStrData, nameField):
    driver.implicitly_wait(3)
    customerNameHelp = randomHelper.random_string_generator()
    secondName = customerNameHelp[:-6]
    capitalSecondName = secondName.upper()
    customerName = requiredStrData + capitalSecondName
    driver.find_element_by_xpath(nameField).send_keys(customerName)
    return customerName



def addressFill(driver, addressLinePath):
    streetNameHelp = randomHelper.random_string_generator()
    streetName = streetNameHelp[:-6]
    capitalStreetName = streetName.upper()
    streetHelpNumber = randomHelper.random_int_generator()
    streetNumber = streetHelpNumber[:2]
    streetFullName = 'Test street ' + capitalStreetName + ' ' + streetNumber
    driver.find_element_by_xpath(addressLinePath).send_keys(streetFullName)



def select2DDRandomly(driver, ddXpath, allListXpath, select2Field):
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(ddXpath).click()
    driver.implicitly_wait(10)
    textList = driver.find_element_by_xpath(allListXpath).text
    textList = str(textList)
    newArray = textList.split('\n')
    randomVar = random.choice(newArray)
    driver.find_element_by_class_name(select2Field).send_keys(randomVar)
    driver.find_element_by_class_name(select2Field).send_keys(Keys.ENTER)



def cityFill(driver, cityField):
    helpCityName = randomHelper.random_string_generator()
    strCityName = helpCityName[:4]
    strCityName = strCityName.upper()
    cityName = 'Test City ' + strCityName
    driver.find_element_by_xpath(cityField).send_keys(cityName)
    driver.implicitly_wait(10)



def postalCode(driver, postalCodePath):
    postalCodeInt = randomHelper.random_int_generator()
    driver.find_element_by_xpath(postalCodePath).send_keys(postalCodeInt)
    return postalCodeInt



def selectDDRandomly(driver, dropDownXpathWithFullList):
    selectRandomValue = Select(driver.find_element_by_xpath(dropDownXpathWithFullList))
    a = [o.get_attribute('text') for o in selectRandomValue.options]
    randomText = (random.choice(a))
    selectRandomValue.select_by_visible_text(randomText)
    time.sleep(1)



def selectAddresses(driver, ddPath, requiredValueInList):
    driver.find_element_by_xpath(ddPath).click()
    driver.find_element_by_xpath(requiredValueInList).click()



def selectDDRandomlyLanguage(driver, dropDownXpathWithFullList):
    selectRandomValue = Select(driver.find_element_by_xpath(dropDownXpathWithFullList))
    b = [o.get_attribute('value') for o in selectRandomValue.options]
    randomTextValue = (random.choice(b))
    selectRandomValue.select_by_value(randomTextValue)
    return randomTextValue



def fillRemarks(driver, fillField):
    strRemark = randomHelper.random_string_generator()
    intRemark = randomHelper.random_int_generator()
    remarkFull = strRemark + ' ' + intRemark
    driver.find_element_by_xpath(fillField).send_keys(remarkFull)



def bonusName(driver, bNameField):
    bName = randomHelper.random_string_generator()
    bName = bName[:8]
    fullBonusName = 'Test b_name ' + bName
    driver.find_element_by_xpath(bNameField).send_keys(fullBonusName)



def bonusPercentage(driver, bPercentagePath):
    bPercentage = randomHelper.intForSmallValues()
    driver.find_element_by_xpath(bPercentagePath).send_keys(bPercentage)



def contactSomeField(driver, beforeData, contactEmailPath, afterData):
    forSomeField = randomHelper.random_string_generator()
    forSomeField = forSomeField[:7]
    someData = beforeData + forSomeField + afterData
    driver.find_element_by_xpath(contactEmailPath).send_keys(someData)
    return someData



def clickOnSaveCustomerButton(driver, scButton):
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, scButton)))
    element.click()



def checkCustomerManagementPage(driver, customerManagementTitle):
    driver.implicitly_wait(20)
    titleCustomerManagement = driver.find_element_by_xpath(customerManagementTitle).text
    assert 'Customers Management' in titleCustomerManagement



def checkJSNotification(driver, notificationClass):
    notifJS = driver.find_element_by_class_name(notificationClass).text
    assert 'Customer was successfully saved.' in notifJS



def checkAfterCreate(driver, pathInCustomerGrid, cusCheckingPath):
    checkingField = driver.find_element_by_xpath(pathInCustomerGrid).text
    assert cusCheckingPath in checkingField


