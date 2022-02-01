from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
    
    def tearDown(self):
        self.browser.refresh() #To avoid ConnectionResetError
        self.browser.close()
    
    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            'Sorry, you don\'t have any projects, yet.')

    def test_no_projects_alery_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        add_url = self.live_server_url + reverse('add')
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url, 
            add_url
            )
        
    def test_user_sees_project_list(self):
        project1 = Project.objects.create(
            name='project1',
            budget=10000
        )
        self.browser.get(self.live_server_url)

        # The user sees the project on the screen
        self.assertEquals(
            self.browser.find_element_by_tag_name('h5').text, 
            'project1')
    
    def test_user_is_redirected_to_project_detail(self):
        project1 = Project.objects.create(
            name='project1',
            budget=10000
        )
        self.browser.get(self.live_server_url)

        # The user sees the project on the screen. He clicks the 'VISIT' link
        # and is redirected to the detail page
        detail_url = self.live_server_url + reverse('detail', args=[project1.slug])
        self.browser.find_element_by_link_text('VISIT').click()
        self.assertEquals(
            self.browser.current_url,
            detail_url)