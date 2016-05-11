

# branch 20894


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from randomHelper import RandomHelper
import createCustomerData
import unittest
import helpFunctionsInfo
import shippingConditionsMethod


randomHelper = RandomHelper()


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(createCustomerData.URL)


    def tearDown(self):
        self.driver.close()


class TestCreateCustomer(BaseTestCase, RandomHelper):

    def test_CreateCustomer(self):
        driver = self.driver

        #log in action
        helpFunctionsInfo.logIn(driver)

        # fill First Name field
        customerFirstName = helpFunctionsInfo.customerNameFill(driver, 'Customer ', createCustomerData.customerNameField)

        # Open full Contact Info Grid
        WebDriverWait(driver, 1).until(lambda driver : driver.find_element_by_xpath(createCustomerData.downArrow)).click()

        # click on Active Status
        driver.find_element_by_class_name(createCustomerData.statusCheckBoxClass).click()

        # Fill Bill Address Line
        helpFunctionsInfo.addressFill(driver, createCustomerData.billAddressLine)
        driver.implicitly_wait(3)

        # Select random country
        helpFunctionsInfo.select2DDRandomly(driver, createCustomerData.billCountrySelect2, createCustomerData.billCountrySelect2AllList,
                                        createCustomerData.billCountyFieldForFillClass)

        # Fill City
        helpFunctionsInfo.cityFill(driver, createCustomerData.billCityField)

        # Fill Bill Postal Code
        helpFunctionsInfo.postalCode(driver, createCustomerData.billPostalCode)

        # Select shipping addresses
        helpFunctionsInfo.selectAddresses(driver, createCustomerData.addressesDropDown, createCustomerData.shippingAddressesXPath)

        # Fill Shipping Address Line
        helpFunctionsInfo.addressFill(driver, createCustomerData.shippingAddressLine)

        # Fill Shipping City
        helpFunctionsInfo.cityFill(driver, createCustomerData.shippingCityLine)
        driver.implicitly_wait(3)

        # Select random Shipping country
        helpFunctionsInfo.select2DDRandomly(driver, createCustomerData.shipCountrySelect2, createCustomerData.shipCountrySelect2AllList,
                                            createCustomerData.shipCountryFieldForFillClass)

        # Fill Shipping postal code
        helpFunctionsInfo.postalCode(driver, createCustomerData.shippingPostalCode)

        # Select Other addresses
        helpFunctionsInfo.selectAddresses(driver, createCustomerData.addressesDropDown, createCustomerData.otherAddressesXPath)
        driver.implicitly_wait(10)

        # Fill Other Address line
        helpFunctionsInfo.addressFill(driver, createCustomerData.otherAddressLine)
        driver.implicitly_wait(3)

        # Select random Other country
        helpFunctionsInfo.select2DDRandomly(driver, createCustomerData.otherCountrySelect2, createCustomerData.otherCountrySelect2AllList,
                                            createCustomerData.otherCountyFieldForFillClass)

        # Fill Other City
        helpFunctionsInfo.cityFill(driver, createCustomerData.otherCityLine)

        # Fill Other postal code
        helpFunctionsInfo.postalCode(driver, createCustomerData.otherPostalCode)

        # Select random Customer Type
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.customerTypeDD)

        # Select random language
        selectLanguage = helpFunctionsInfo.selectDDRandomlyLanguage(driver, createCustomerData.defaultLanguageDD)

        # Fill Remarks field
        helpFunctionsInfo.fillRemarks(driver, createCustomerData.remarksField)

        # Select random Shipping method and make required actions
        shippingConditionsMethod.shippingConditions(driver, createCustomerData.shipCondDropDown, createCustomerData.movMinimumField,
                                           createCustomerData.movMaximumField, createCustomerData.shippingCostsField,
                                           createCustomerData.freeShippingFromField, createCustomerData.pricePerItemField,
                                           createCustomerData.flatFeeField, createCustomerData.pricePerItemSecond,
                                                    createCustomerData.flatFeeSecond)

        # Fill Bonus Name field
        helpFunctionsInfo.bonusName(driver, createCustomerData.bonusNameField)

        # Fill Bonus Percentage field
        helpFunctionsInfo.bonusPercentage(driver, createCustomerData.bonusPercentAgeField)

        # Select Time Period
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.timePeriodDD)

        # Fill Contact Name
        helpFunctionsInfo.customerNameFill(driver, 'Test contact name ', createCustomerData.contactName)

        # Select random Contact Type
        driver.implicitly_wait(5)
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.contactTypeDD)

        # Fill Contact Phone
        helpFunctionsInfo.postalCode(driver, createCustomerData.contactPhone)

        # Fill Contact Email
        customerEmail = helpFunctionsInfo.contactSomeField(driver, 'test.mail.', createCustomerData.contactEmail, '@gmail.com')

        # Fill Contact Website
        helpFunctionsInfo.contactSomeField(driver, 'testsite', createCustomerData.contactWebSite, '.com')

        # Fill Vat ID
        vatID = helpFunctionsInfo.postalCode(driver, createCustomerData.vatIDField)

        # Select random Payment terms
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.paymentTermsDD)

        # Select random Currency
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.currencyDD)

        # Select random Price Model
        helpFunctionsInfo.selectDDRandomly(driver, createCustomerData.priceModelDD)

        # Click on Create Customer button
        helpFunctionsInfo.clickOnSaveCustomerButton(driver, createCustomerData.createCustomerButton)

        # Check main page is displayed
        driver.implicitly_wait(20)
        helpFunctionsInfo.checkCustomerManagementPage(driver, createCustomerData.customerManagementTitle)

        # Check Notification
        helpFunctionsInfo.checkJSNotification(driver, createCustomerData.notificationClass)

        # Check Customer name is displayed
        helpFunctionsInfo.checkAfterCreate(driver, createCustomerData.customerNamePath, customerFirstName)

        # Check Customer language is displayed
        helpFunctionsInfo.checkAfterCreate(driver, createCustomerData.customerLanguagePath, selectLanguage)

        # Check Email is displayed
        helpFunctionsInfo.checkAfterCreate(driver, createCustomerData.contactEmailPath, customerEmail)

        # Check Vat ID is displayed
        helpFunctionsInfo.checkAfterCreate(driver, createCustomerData.vatIDPath, vatID)


if __name__ == '__main__':
    unittest.main()
