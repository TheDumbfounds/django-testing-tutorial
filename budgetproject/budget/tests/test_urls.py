from django.urls import reverse, resolve
from django.test import TestCase

class TestUrls(TestCase):

    def test_list_url(self):
        path = reverse('list')
        assert resolve(path).view_name == 'list'

    def test_add_url(self):
        path = reverse('add')
        assert resolve(path).view_name == 'add'

    def test_detail_url(self):
        path = reverse('detail', kwargs={'project_slug':'project1'})
        assert resolve(path).view_name == 'detail'
