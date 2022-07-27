from django.test import TestCase
from django.contrib.auth import get_user_model
from Managers.models import schedule,managerreport,passengerfiless,news
class UsersWorkersTests(TestCase):

    def test_create_user(self):
        Order = schedule
        order = Order.objects.create(workername='workername', date1='2022-12-12')
        self.assertEqual(order.worker, 'workername')
        self.assertTrue(order.workername)
        
        try:
           
            self.assertIsNotNone(order.workername)
        except AttributeError:
            raise "worker is missed"
        



class WorkersOrdersTestCase(TestCase):
    def setup(self):
        order=managerreport.objects.create()
        managerreport.objects.create(count='20',workername='workername',text='text')
        self.assertEqual(order.count, '20')
        self.assertTrue(order.count)
        #self.assertFalse(order.is_staff)
        try:
           
            self.assertIsNone(order.workername)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            managerreport.objects.create_user()
        with self.assertRaises(TypeError):
            managerreport.objects.create_user(worker='')
        with self.assertRaises(ValueError):
            managerreport.objects.create_user(workername='',text="fff")



class UsersReportsTests(TestCase):

    def test_create_user(self):
        Report = passengerfiless
        reports = passengerfiless.objects.create(passenger_name='passenger_name', passenger_id='000000000')
        self.assertEqual(reports.passenger_name, 'passenger_name')
        self.assertNotEqual(reports.count,'20')
        self.assertTrue(reports.passenger_name)
        
        try:
           
            self.assertIsNotNone(reports.id)
        except AttributeError:
            raise "Field should not be null"

        # try:
        #     self.assertEqual(reports.name)
        # except:
        #     raise "worker not found"
