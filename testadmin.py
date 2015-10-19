# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
 

class MainAdmin(unittest.TestCase):
    """ Author: Dusty Stokes (dustys@motiga.com) """

    def setUp(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_HomePage(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """      
        driver = self.driver 
        driver.get("http://rx-dal-platform3.motiga.net:83/0.0/login")

    def test_LoginSuccess(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """      
        driver = self.driver 
        driver.get("http://rx-dal-platform3.motiga.net:83/0.0/login")
        email = driver.find_element_by_xpath(".//*[@id='signin-form']/input[1]")
        email.send_keys("dustys@motiga.com")
        password = driver.find_element_by_xpath(".//*[@id='signin-form']/input[2]")
        password.send_keys("Spokane1")
        password.send_keys(Keys.RETURN)
        time.sleep(2) 


    def test_Login(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_HomePage()
        email = driver.find_element_by_xpath(".//*[@id='signin-form']/input[1]")
        email.send_keys("test")
        email.send_keys(Keys.RETURN)
        #verify failure notif
        password = driver.find_element_by_xpath(".//*[@id='signin-form']/input[2]")
        password.send_keys("failure")
        password.send_keys(Keys.RETURN)
        #verify failure notif
        email.clear()
        password.clear()
        email.send_keys("dustys@motiga.com")
        password.send_keys("Spokane1")
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        assert 'nomination_search' in driver.current_url

    def test_Nominations(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        email = driver.find_element_by_id("email-search")
        email.send_keys("dustys")
        driver.find_element_by_xpath(".//*[@id='nom-table']/thead[2]/tr/th[11]/div/button[1]").click()
        time.sleep(2)
        searchresult = driver.find_element_by_xpath(".//*[@id='nom-table']/tbody/tr[1]/td[2]")
        firstresult = searchresult.text
        assert 'dustys' in firstresult
        email.clear()
        email.send_keys("j453rsfsef")
        driver.find_element_by_xpath(".//*[@id='nom-table']/thead[2]/tr/th[11]/div/button[1]").click()
        time.sleep(2)
        searchresult = driver.find_element_by_xpath(".//*[@id='nom-table']/tbody/tr/td")
        noresult = searchresult.text
        assert 'No data available in table' in noresult

    def test_Players(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Players").click()
        time.sleep(2)
        email = driver.find_element_by_xpath(".//*[@id='email-search']")
        email.send_keys("dustys")
        driver.find_element_by_xpath(".//*[@id='player-table']/thead[2]/tr/th[6]/div/button[1]").click()
        time.sleep(2)
        result = driver.find_element_by_xpath(".//*[@id='player-table']/tbody/tr[1]/td[3]")
        firstresult = result.text
        assert 'dustys' in firstresult
        email.clear()
        email.send_keys("jfwaeifaoewifj")
        driver.find_element_by_xpath(".//*[@id='player-table']/thead[2]/tr/th[6]/div/button[1]").click()
        time.sleep(2)
        searchresult = driver.find_element_by_xpath(".//*[@id='player-table']/tbody/tr/td")
        noresult = searchresult.text
        assert 'No data available in table' in noresult

    def test_PlayerPage(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Players").click()
        time.sleep(1)
        username = driver.find_element_by_id("username-search")
        username.send_keys("MO_DustimusPrime")
        username.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='player-table']/tbody/tr/td[6]/a").click()
        user = driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div/h1")
        confirmuser = user.text
        assert 'MO_DustimusPrime' in confirmuser
        driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div/h1/a").click()
        driver.find_element_by_xpath(".//*[@id='changeUsernameModal']/div/div/div/a").click()            

    def test_Shop(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_xpath(".//*[@id='user-drop']").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[3]/ul/li[1]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/div[1]")
        text = widget.text
        assert 'Catalog' in text

    def test_Manage(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_xpath(".//*[@id='user-drop']").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[3]/ul/li[2]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='catalogs']/div/div[1]/h3")
        text = widget.text
        assert 'Catalogs' in text

    def test_AccountInventory(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_xpath(".//*[@id='user-drop']").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[3]/ul/li[3]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div/div[1]/h1")
        text = widget.text
        assert 'Inventory' in text

    def test_OrderTracking(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_xpath(".//*[@id='user-drop']").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[3]/ul/li[4]/a").click()
        driver.find_element_by_xpath(".//*[@id='accordion']/div[1]/div[1]/h4/div")

    def test_CardSettings(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[1]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/div[1]/h3")
        text = widget.text
        assert 'Card Settings' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div[1]/h3")
        text2 = widget2.text
        assert 'Card List' in text2
        widget3 = driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div/div[1]/h3")
        text3 = widget3.text
        assert 'Decks' in text3

    def test_Cards(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[2]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div/div[1]/h3")
        info = widget.text
        assert 'Info' in info
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[1]/h3")
        active = widget2.text
        assert 'Active Cards' in active
        widget3 = driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[2]/div/div[1]")
        current = widget3.text
        assert 'Current Fortune' in current
        widget4 = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div/div[1]/h3")
        history = widget4.text
        assert 'Card History' in history

    def test_ProgressionSettings(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[3]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/div[1]/div/div[1]/h3")
        rank = widget.text
        assert 'Account Rank' in rank
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div[1]/div[2]/div/div[1]/h3")
        endofmatch = widget2.text
        assert 'End Of Match' in endofmatch
        widget3 = driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[1]/h3")
        badges = widget3.text
        assert 'Badges' in badges
        widget4 = driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[2]/div/div[1]/h3")
        medals = widget4.text
        assert 'Medals' in medals     
       
    def test_Progression(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[4]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/div[1]/h3")
        rank = widget.text
        assert 'Account Rank' in rank
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div[1]/h3")
        badges = widget2.text
        assert 'Badges' in badges
        widget3 = driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div/div[1]/h3")
        medals = widget3.text
        assert 'Medals' in medals

    def test_EndOfMatchReports(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[5]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/div[1]")
        reports = widget.text
        assert 'End of Match Reports' in reports

    def test_InventorySettings(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Progression").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[4]/ul/li[6]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[1]/h3")
        settings = widget.text
        assert 'Inventory Settings' in settings

    def test_GameData(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Game Data").click()
        widget = driver.find_element_by_xpath(".//*[@id='data-versions-panel']/div/div[1]")
        versions = widget.text
        assert 'Game Data Versions' in versions

    def test_Maps(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Maps").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/h2")
        maps = widget.text
        assert 'Maps' in maps
        widget2 = driver.find_element_by_xpath(".//*[@id='other']/table/thead/tr/th[1]")
        name = widget2.text
        assert 'Name' in name

    def test_Lobby(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Lobby").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h3")
        mapsettings = widget.text
        assert 'Map Settings' in mapsettings
        popup = driver.find_element_by_xpath(".//*[@id='alert-div']/div")
        xmpperr = popup.text
        assert 'Xmpp is not up or xmlrpc module is not loaded' not in xmpperr

    def test_Database(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Status").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[8]/ul/li[1]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h2")
        header = widget.text
        assert 'Postgres Query Stats' in header
        widget2 = driver.find_element_by_xpath(".//*[@id='pgdata']/thead/tr/th[1]")
        key = widget2.text
        assert 'Key' in key

    def test_Machines(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Status").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[8]/ul/li[2]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h2")
        header = widget.text
        assert 'Dashboard' in header

    def test_Servers(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Status").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[8]/ul/li[3]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='servers_in_use']/table/thead/tr/th[2]")
        text = widget.text
        assert 'Name' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h3")
        inuse = widget2.text
        assert 'Servers in use' in inuse
        widget3 = driver.find_element_by_xpath(".//*[@id='content']/div[2]/h3")
        servers = widget3.text
        assert 'Servers' in servers

    def test_Services(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Status").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[8]/ul/li[4]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/h2")
        text = widget.text
        assert 'Service Status' in text
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[1]/span/h2").click()
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[2]/span/h2").click()
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[3]/span/h2").click()
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[4]/span/h2").click()
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[5]/span/h2").click()
        driver.find_element_by_xpath(".//*[@id='service_statuses']/div[6]/span/h2").click()

    def test_Versions(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Status").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[8]/ul/li[5]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/h2")
        text = widget.text
        assert 'Versions of Motiga Software' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/table/thead/tr/th[1]")
        appname = widget2.text
        assert 'App name' in appname

    def test_AccessRestrictions(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[1]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/h2")
        text = widget.text
        assert 'Access Restrictions' in text

    def test_Announcements(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[2]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/h2[1]")
        text = widget.text
        assert 'Most Recent Announcement' in text

    def test_AuthToken(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[3]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div/div[1]/h3")
        text = widget.text
        assert 'Create Auth Token' in text

    def test_BouncedEmails(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[4]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='bounced-emails-table']/thead[1]/tr/th[2]")
        text = widget.text
        assert 'Email Address' in text

    def test_BuildDeployment(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[5]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/h3[1]")
        text = widget.text
        assert 'Current build info' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/h3[2]")
        text2 = widget2.text
        assert 'Builds' in text2

    def test_BulkCurrency(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[6]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[1]/h3")
        text = widget.text
        assert 'Bulk Currency Updates' in text

    def test_DefaultSettings(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[7]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[1]/div[1]")
        text = widget.text
        assert 'Default Settings' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div[1]/h3")
        text2 = widget2.text
        assert 'Example Settings' in text2

    def test_Emails(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[8]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h2")
        text = widget.text
        assert 'Emails' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='emailForm']/div/div/div[1]/label")
        text2 = widget2.text
        assert 'Context JSON' in text2                                                                                                                                                                                  

    def test_Eula(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[9]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/h2")
        text = widget.text
        assert 'Eulas' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/h3[1]")
        text2 = widget2.text
        assert 'Current Eula' in text2

    def test_Flags(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[10]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/h2")
        text = widget.text
        assert 'Access Management Group' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/table/thead/tr/th[1]")
        text2 = widget2.text
        assert 'Flag' in text2

    def test_LogRequests(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[11]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/h2")
        text = widget.text
        assert 'Log Requests' in text

    def test_ManageUsers(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[12]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div[1]/nav/div[1]/a")
        text = widget.text
        assert 'User Search' in text
        search = driver.find_element_by_xpath(".//*[@id='search']/input")
        search.send_keys("MO_DustimusPrime")
        search.send_keys(Keys.RETURN)
        results = driver.find_element_by_xpath(".//*[@id='content']/table/tbody/tr/td[2]")
        user = results.text
        assert 'dustys@motiga.com' in user
        driver.find_element_by_xpath(".//*[@id='content']/table/tbody/tr/td[1]/a").click()
        userpage = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[1]/h1")
        userpagename = userpage.text
        assert 'MO_DustimusPrime' in userpagename
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[12]/a").click()
        search2 = driver.find_element_by_xpath(".//*[@id='search']/input")
        search2.send_keys("fwefkjwefwe")
        search2.send_keys(Keys.RETURN)
        noresults = driver.find_element_by_xpath(".//*[@id='content']/div[3]")
        errormessage = noresults.text
        assert 'Sorry! No Results' in errormessage

    def test_Matchmaking(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[13]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/div/div[1]/h3")
        text = widget.text
        assert 'Matchmaking Settings' in text    
        
    def test_TitleStorage(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("Utility").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[1]/li[9]/ul/li[14]/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='content']/div/div/h2")
        text = widget.text
        assert 'Title Storage' in text
        widget2 = driver.find_element_by_xpath(".//*[@id='content']/div/table/thead/tr/th[1]")
        text2 = widget2.text
        assert 'Version' in text2

    def test_Logout(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """
        driver = self.driver
        self.test_LoginSuccess()
        driver.find_element_by_link_text("dustys@motiga.com").click()
        driver.find_element_by_xpath(".//*[@id='navbar_div']/ul[2]/li/ul/li/a").click()
        widget = driver.find_element_by_xpath(".//*[@id='signin-form']/h2")
        text = widget.text
        assert 'Please sign in' in text                    

    def tearDown(self):
        """ Author: Dusty Stokes (dustys@motiga.com) """         
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MainAdmin)
    unittest.TextTestRunner(verbosity=2).run(suite)    