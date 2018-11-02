from django.test import TestCase

'''
#Currently not working


from selenium import webdriver
import random, string
from django.contrib.auth.models import User
from accounts.models import PlayerInventory

class ClickButtonTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1:8000')
        self.random_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        self.create_user = User.objects.create_user(username=self.random_username, password='test1234')
        self.current_user = User.objects.get(username=self.random_username)
        self.create_inventory = PlayerInventory.objects.create(id=1, name=self.current_user, total_clicks=0, equipped_button_id=1, equipped_background_id=1)
        self.inventory = PlayerInventory.objects.get(id=1)

        #print(User.objects.get(id=1).username, '\n')
        #print(self.inventory.total_clicks, '\n')
        #print(self.current_user.is_authenticated(), '\n\n\n')
        #print('Random username : ',self.random_username)

        #created user always logged in?
        #when logging in doesn't accept the password that was assigned when creating user

        #self.login_button = self.driver.find_element_by_id('login-button')
        #self.login_button.click()
        #self.username = self.driver.find_element_by_name('username')
        #self.username.send_keys(self.random_username)
        #self.password = self.driver.find_element_by_name('password')
        #self.password.send_keys('test1234')
        #self.submit_login = self.driver.find_element_by_name('submit-login')
        #self.submit_login.click()

        #self.current_username = self.driver.find_element_by_id('username').text

    def test_clickbutton(self):
        driver = self.driver
        current_user = self.current_user

        current_user_id = current_user.id
        current_clicks = PlayerInventory.objects.get(name=current_user_id).total_clicks  #because name field is a foreign key to user's id field
        expected_clicks = current_clicks + 1

        start_playing = driver.find_element_by_id('start-playing')
        start_playing.click()
        click_button = driver.find_element_by_id('click-button')
        click_button.click()
        new_clicks = PlayerInventory.objects.get(name=current_user_id).total_clicks
        self.assertEqual(expected_clicks, new_clicks)

    #def tearDown(self):
    #    self.driver.quit()

'''