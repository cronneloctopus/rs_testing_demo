from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# --- functional tests --- #
class FormsTest(LiveServerTestCase):
    """
    Test project form.
    """

    # load fixtures
    fixtures = ['animals.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_vote(self):
        # set url for page
        self.browser.get(
            self.live_server_url + '/'
        )
        time.sleep(3)
        # get body
        body = self.browser.find_element_by_tag_name('body')
        # check for text in body
        self.assertIn("Animal Voting Form", body.text)

        # select an animal
        self.browser.find_element_by_xpath(
            '//*[@id="id_choose_animal"]/option[text()="Panda"]'
        ).click()
        time.sleep(3)

        # find submit button and submit form
        self.browser.find_element_by_xpath(
            '/html/body/div/div/form/input'
        ).click()

        # check for success text in body
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("You registered a vote for Panda!", body.text)
        time.sleep(3)

    def test_add(self):
        # set url for page
        self.browser.get(
            self.live_server_url + '/'
        )
        time.sleep(3)

        # lets add an animal
        add_animal = self.browser.find_element_by_xpath(
            '//*[@id="id_add_animal"]'
        )
        add_animal.send_keys('Moose')
        time.sleep(3)

        # find submit button and submit form
        self.browser.find_element_by_xpath(
            '/html/body/div/div/form/input'
        ).click()

        # check for success text in body
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("You registered a vote for Moose!", body.text)
        time.sleep(3)
