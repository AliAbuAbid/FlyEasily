from django.test import TestCase
from django.contrib.auth import get_user_model

from Passengers.models import Passengerorders, passengers, ratings
from Passengers.views import rating
# Create your tests here.

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = passengers
        user = User.objects.create(id='000000000', password1='foo123456')
        self.assertEqual(user.id, '000000000')
        
        try:
            
            self.assertIsNotNone(user.id)
        except AttributeError:
            pass
   
        

    
        try:
           
            self.assertIsNotNone(user.id)
        except AttributeError:
            raise "user is missed"
        
        try:
           
            self.assertIsNotNone(user.age)
        except AttributeError:
            raise "user is missed"


class UsersOrdersTests(TestCase):

    def test_create_user(self):
        Order = Passengerorders
        order = Order.objects.create(chair='100', other='foo1234')
        self.assertEqual(order.chair, '')
        self.assertTrue(order.chair)
        
        try:
           
            self.assertIsNotNone(order.chair)
        except AttributeError:
            raise "worker is missed"


class UsersRatingTests(TestCase):
    def test_create_rating(self):
        rating=ratings
        rate=rating.objects.create(name='nam',id='worker')
        self.assertEqual(rate.name,'name')
        self.assertTrue(rate.name)

        try:
            self.assertIsNotNone(rate.name)
        except AttributeError:
                raise "name not found"


