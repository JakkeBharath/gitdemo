import time
import pytest
from PageObjects.HomePage import ShopItems
from PageObjects.PaymentPage import PaymentPage
from TestData.HomePageData import HomePageData
from Tests.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end2end(self,getdata):

        log= self.getlogger()
        home_page= ShopItems(self.driver)
        home_page.Name_Page().send_keys(getdata["FirstName"])
        log.info("gettingUsername")
        time.sleep(3)
        home_page.Email_Page().send_keys(getdata["E-Mail ID"])
        log.info("getting Emailid")
        time.sleep(3)
        home_page.Password_Page().send_keys(getdata["Password"])
        log.info("gettingPassword")
        time.sleep(3)
        home_page.CheckBox_Page().click()
        time.sleep(3)
        self.SelectOptionByText(home_page.Gender_Page(),getdata["Gender"])
        time.sleep(3)
        home_page.RadioButton_Page().click()
        time.sleep(3)
        home_page.Button_Page().click()
        d= home_page.alert_Page().text
        log.info("text received from appllication"+d)
        print(d)
        assert "submitted successfully!" in d
        self.driver.get_screenshot_as_file("screen.png")
        shopitems = home_page.ShopItem_Page()
        c = shopitems.Title_Page()
        print(len(c))
        a = -1
        for i in c:
            a = a + 1
            cart = i.text
            print(cart)
            log.info(cart)
            if cart == "Blackberry":
                shopitems.AddButton_Page()[a].click()
        checkoutpage = shopitems.AddCart_Page()
        checkoutpage.checkoutButton_Page().click()
        payment_page = PaymentPage(self.driver)
        log.info("getting Country")
        payment_page.country_Page().send_keys("ind")
        self.verification("India")
        payment_page.CountryOptions_Page().click()
        payment_page.Checkbox_Page().click()
        payment_page.button_Page().click()
        c = payment_page.alert_Page().text
        log.info("text received from appllication is " + c)
        print(c)
        assert "Success!" in c
        self.driver.get_screenshot_as_file("screen1.png")

    @pytest.fixture(params=HomePageData.getTestData("TC3"))
    def getdata(self,request):
        return request.param