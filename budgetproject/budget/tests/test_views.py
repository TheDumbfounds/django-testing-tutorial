from django.test import TestCase,Client
from django.urls import resolve, reverse
from budget.models import Project, Category, Expense
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project_1'])

        self.project_one  = Project.objects.create(
            name ='project_1',
            budget = 10000
        )
        
    #This is the test for the index page to view a list of projects
    def test_project_list_view(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "budget/project-list.html")

    #This is the test for the project_detailed page 
    def test_project_detail_view_get_request(self):     
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "budget/project-detail.html")

    #This is the test for a post request to add new expense to the project 
    def test_project_detail_view_post_request(self): 
        Category.objects.create(
            project = self.project_one,
            name = 'development'
        )
        expense = {
            "title":"expense_one",
            "amount":"100",
            "category": "development"
        }    
        response = self.client.post(self.detail_url, expense)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project_one.expenses.first().title, 'expense_one')


    #This is the test for a post request has no data 
    def test_project_detail_post_request_no_data(self): 
        response = self.client.post(self.detail_url)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.project_one.expenses.count(), 0)


        
    #This is the test for a request to delete an expense
    def test_project_detail_delete_request(self): 

        self.category = Category.objects.create(
            project = self.project_one,
            name = 'development'
        )

        Expense.objects.create(         
                project = self.project_one,
                title = "expense_one",
                amount = 100,
                category = self.category
        )

        response = self.client.delete(self.detail_url, json.dumps({
            'id': 1
            }))

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.project_one.expenses.count(), 0)

    #This is the test for create_project_view 
    def test_project_create_view(self):
        url = reverse('add')

        project_two = {
            "name" : "project_two",
            "budget" : "10000",
            "categoriesString" : "development,materials"
        }

        response = self.client.post(url, project_two)

        project2 = Project.objects.get(id=2)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(project2.name, 'project_two')

        first_category = Category.objects.get(id=1)
        self.assertEqual(first_category.name, 'development')

        second_category = Category.objects.get(id=2)
        self.assertEqual(second_category.name, 'materials')

       




