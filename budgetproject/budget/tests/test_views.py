from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project1'])
        Project.objects.create(
            name='project1',
            budget=10000
        )

    def test_project_list_GET(self):
        # client = Client()
        response = self.client.get(self.list_url)
        

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')
    
    def test_project_detail_GET(self):
        
        response = self.client.get(self.detail_url)
        

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')



