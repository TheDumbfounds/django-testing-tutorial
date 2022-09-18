from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_resolved(self):
        url = reverse('')