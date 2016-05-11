URL = 'http://dev:q1w2e3r4@erp.bintime.com:81/users/createcustomer'
testURL = 'http://dev:q1w2e3r4@testing.bintime.com/users/createcustomer'
loginField = '//*[@id="UserLogin_username"]'
loginData = 'admin'
passwordField = '//*[@id="UserLogin_password"]'
passwordData = 'admin'
loginButton = '//*[@id="login-form"]//div[6]/input'



# Create Customer Page
customerNameField = '//*[@id="Customer_customer_name"]'

statusCheckBoxClass = 'mark'

billAddressLine = '//*[@id="Customer_bill_address_line"]'
billCountrySelect2 = '//*[@id="select2-Customer_bill_country-container"]'
billCountrySelect2AllList = '//*[@id="select2-Customer_bill_country-results"]' #'select2-results__options'  #
billCountyFieldForFillClass = 'select2-search__field'
billCityField = '//*[@id="Customer_bill_city"]'
billPostalCode = '//*[@id="Customer_bill_postalcode"]'

addressesDropDown = '//*[@id="Customer_addresses"]'
shippingAddressesXPath = '//*[@id="Customer_addresses"]//option[2]'
shippingAddressLine = '//*[@id="Customer_shipping_addresses_address_line"]'
shippingCityLine = '//*[@id="Customer_shipping_addresses_city"]'

shipCountrySelect2 = '//*[@id="select2-Customer_shipping_addresses_shipping_country-container"]'
shipCountrySelect2AllList = '//*[@id="select2-Customer_shipping_addresses_shipping_country-results"]'  #'select2-results__options'
shipCountryFieldForFillClass = 'select2-search__field'

shippingPostalCode = '//*[@id="Customer_shipping_addresses_postalcode"]'

otherAddressesXPath = '//*[@id="Customer_addresses"]//option[3]'
otherAddressLine = '//*[@id="Customer_other_address_line"]'

otherCountrySelect2 = '//*[@id="select2-Customer_other_country-container"]'
otherCountrySelect2AllList = '//*[@id="select2-Customer_other_country-results"]'  #'select2-results__options'
otherCountyFieldForFillClass = 'select2-search__field'

otherCityLine = '//*[@id="Customer_other_city"]'

otherPostalCode = '//*[@id="Customer_other_postalcode"]'

customerTypeDD = '//*[@id="Customer_customer_type"]'
defaultLanguageDD = '//*[@id="Customer_selected_language_id"]'

remarksField = '//*[@id="Customer_remarks"]'




#Shipping Conditions data
shipCondDropDown = '//*[@id="Customer_shipping_conditions"]'
shipCondTitle = '//*[@id="yw2"]/div[2]/div[1]/label'

movMinimumField = '//*[@id="Customer_mov_min"]'
movMaximumField = '//*[@id="Customer_mov_max"]'
shippingCostsField = '//*[@id="Customer_mov_shipping_costs"]'
freeShippingFromField = '//*[@id="Customer_free_shipping"]'

pricePerItemField = '//*[@id="Customer_price_per_item"]'

flatFeeField = '//*[@id="Customer_flat_fee"]'

pricePerItemSecond = '//*[@id="Customer_price_per_item"]'
flatFeeSecond = '//*[@id="Customer_flat_fee"]'



# Other Info data
bonusNameField = '//*[@id="Customer_other_info_bonus_name"]'
bonusPercentAgeField = '//*[@id="Customer_other_info_bonus_percentage"]'
timePeriodDD = '//*[@id="Customer_other_info_time_period"]'



# Contact Info data
contactName = '//*[@id="Customer_contacts_contact_name"]'
downArrow = '//*[@id="yw4"]//div[2]/div/div[1]'
contactTypeDD = '//*[@id="Customer_contacts_contact_type"]'
contactPhone = '//*[@id="Customer_contacts_contact_phone"]'
contactEmail = '//*[@id="Customer_contacts_contact_email"]'
contactWebSite = '//*[@id="Customer_contacts_contact_website"]'



# Purchase Info
vatIDField = '//*[@id="Customer_vat_id"]'
paymentTermsDD = '//*[@id="Customer_payment_terms"]'
currencyDD = '//*[@id="Customer_currency"]'
priceModelDD = '//*[@id="Customer_price_model"]'



createCustomerButton = '//*[@id="yw0"]//button[1]'



customerManagementTitle = '//*[@id="customer-list"]//h3'
customerNamePath = '//*[@id="customer-grid"]//table[2]//tr[1]/td[2]/a'
notificationClass = 'noty_text'
customerLanguagePath = '//*[@id="customer-grid"]//table[2]//tr[1]/td[3]/a'
contactEmailPath = '//*[@id="customer-grid"]//table[2]//tr[1]/td[4]'
vatIDPath = '//*[@id="customer-grid"]//table[2]//tr[1]/td[5]'