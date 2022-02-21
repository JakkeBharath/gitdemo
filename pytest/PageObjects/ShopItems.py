from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class ShopItem:
    shop_button = (By.XPATH, "//*[@class='navbar-nav'] /li[2]/a")
    Title = (By.CSS_SELECTOR,".card-title a")
    AddButton = (By.CSS_SELECTOR,".card-footer button")
    AddCart = (By.CSS_SELECTOR,"a[class*='btn-primary']")


    def __init__(self,driver):
        self.driver = driver

    def shop_button_page(self):
        return self.driver.find_element(*ShopItem.shop_button)

    def Title_Page(self):
        return self.driver.find_elements(*ShopItem.Title)

    def AddButton_Page(self):
        return self.driver.find_elements(*ShopItem.AddButton)

    def AddCart_Page(self):
        self.driver.find_element(*ShopItem.AddCart).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage