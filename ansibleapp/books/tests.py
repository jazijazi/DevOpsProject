import email
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book , Review

class BookTests(TestCase):

    def setUp(self):
        #create user
        self.user = get_user_model().objects.create_user(
            username = 'testreviewuser' ,
            email = 'testreviewuser@test.test',
            password = 'jazi123456'
        )
        #create book
        self.book = Book.objects.create(
            title = 'testbook' ,
            author = 'jazi' , 
            price = '25.01'
        )
        #create review for book with this user
        self.review = Review.objects.create(
            book = self.book , 
            author = self.user ,
            review = 'good review' , 
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}' , 'testbook')
        self.assertEqual(f'{self.book.author}' , 'jazi')
        self.assertEqual(f'{self.book.price}' , '25.01')

    def test_book_list_view(self):
        self.client.login(username='testreviewuser' , email='testreviewuser@test.test', password='jazi123456') #login user
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code , 200)
        self.assertContains(response , 'testbook')
        self.assertTemplateUsed(response , 'book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code , 302)