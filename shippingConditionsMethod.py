import random
from selenium.webdriver.support.select import Select
from randomHelper import RandomHelper


randomHelper = RandomHelper()

def shippingConditions(driver, dropDownXpathWithFullList, movMinimum, movMaximum, shipCostField,
                       freeShippingFromField, pricePerItemField, flatFeeField, pricePerItemFieldSecond, flatFeeSecondXpath):
    selectRandomValue = Select(driver.find_element_by_xpath(dropDownXpathWithFullList))
    a = [o.get_attribute('text') for o in selectRandomValue.options]
    randomValue = (random.choice(a))
    selectRandomValue.select_by_visible_text(randomValue)
    if randomValue == 'Minimum order value':

        intMin = range(0, 100)
        varForMovMinimum = random.choice(intMin)
        driver.find_element_by_xpath(movMinimum).send_keys(varForMovMinimum)
        intMax = range(101, 200)
        varForMaxValue = random.choice(intMax)
        driver.find_element_by_xpath(movMaximum).send_keys(varForMaxValue)
        intShipCosts = range(200, 400)
        varFoxShipCosts = random.choice(intShipCosts)
        driver.find_element_by_xpath(shipCostField).send_keys(varFoxShipCosts)
        intFreeFrom = range(100, 300)
        varForFreeFrom = random.choice(intFreeFrom)
        driver.find_element_by_xpath(freeShippingFromField).send_keys(varForFreeFrom)

    elif randomValue == 'Item based shipping (price per item)':
        intPerItem = range(100, 200)
        pricePerItem = random.choice(intPerItem)
        driver.find_element_by_xpath(pricePerItemField).send_keys(pricePerItem)

    elif randomValue == 'Flat fee per order':
        intFlatFeePerOrder = range(10, 100)
        flatFee = random.choice(intFlatFeePerOrder)
        driver.find_element_by_xpath(flatFeeField).send_keys(flatFee)

    elif randomValue == 'Item based shipping and flat fee per order':
        intPerItemSecond = range(10, 200)
        pricePerItemSecond = random.choice(intPerItemSecond)
        driver.find_element_by_xpath(pricePerItemFieldSecond).send_keys(pricePerItemSecond)
        intFlatFeeSecond = range(50, 100)
        flatFeeSecond = random.choice(intFlatFeeSecond)
        driver.find_element_by_xpath(flatFeeSecondXpath).send_keys(flatFeeSecond)