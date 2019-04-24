from django.test import TestCase
from django.urls import resolve, reverse
from budget.views import project_list, project_detail, ProjectCreateView


class TestUrl(TestCase):

    def test_list_url_is_resloved(self):
         url = reverse('list')
         #print(resolve(url))
         self.assertEqual(resolve(url).func, project_list)

    def test_add_url_is_resloved(self):
         url = reverse('add')
         #print(resolve(url))
         self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_is_resloved(self):
         url = reverse('detail', args=['some'])
         #print(resolve(url))
         self.assertEqual(resolve(url).func, project_detail)

