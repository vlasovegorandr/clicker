from django.test import TestCase
from selenium import webdriver
import string, random

class LoginTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http:127.0.0.1:8000')

    def test_login(self):
        driver = self.driver
        login_button = driver.find_element_by_id('login-button')
        login_button.click()
        username = driver.find_element_by_name('username')
        username.send_keys('egor')
        password = driver.find_element_by_name('password')
        password.send_keys('test1234')
        submit_login = driver.find_element_by_name('submit-login')
        submit_login.click()

        logged_in_username = driver.find_element_by_id('username')

        self.assertEqual(logged_in_username.text, 'egor')

    def tearDown(self):
        self.driver.quit()

class CreateUserTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http:127.0.0.1:8000')
        self.random_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


    def test_signup(self):
        driver = self.driver
        signup_button = driver.find_element_by_id('signup-button')
        signup_button.click()
        username = driver.find_element_by_name('username')
        username.send_keys(self.random_username)
        password1 = driver.find_element_by_name('password1')
        password1.send_keys(self.random_password)
        password2 = driver.find_element_by_name('password2')
        password2.send_keys(self.random_password)
        submit_login = driver.find_element_by_name('submit-signup')
        submit_login.click()

        logged_in_username = driver.find_element_by_id('username')

        self.assertEqual(logged_in_username.text, self.random_username)

    def tearDown(self):
        self.driver.quit()




# Create your tests here.
