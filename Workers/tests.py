from django.test import TestCase
from django.contrib.auth import get_user_model
from Workers.views import report,Workersorders, reports

class UsersWorkersTests(TestCase):

    def test_create_user(self):
        Order = Workersorders
        order = Order.objects.create(worker='worker', other='foo1234')
        self.assertEqual(order.worker, 'worker')
        self.assertTrue(order.worker)
        
        try:
           
            self.assertIsNotNone(order.worker)
        except AttributeError:
            raise "worker is missed"
        



class WorkersOrdersTestCase(TestCase):
    def setup(self):
        order=Workersorders.objects.create()
        Workersorders.objects.create(cold="water",worker="worker",dood="breakefast",other="nothing")
        Workersorders.objects.create(cold="water",hot="tea",food="breakefast",other="nothing")



        self.assertEqual(order.other, 'nothing')
        self.assertTrue(order.is_active)
        self.assertFalse(order.is_staff)
        try:
           
            self.assertIsNone(order.worker)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            Workersorders.objects.create_user()
        with self.assertRaises(TypeError):
            Workersorders.objects.create_user(worker='')
        with self.assertRaises(ValueError):
            Workersorders.objects.create_user(worker='',password="fff")



class UsersReportsTests(TestCase):

    def test_create_user(self):
        Report = report
        reports = Report.objects.create(name='name', count='1')
        self.assertEqual(reports.name, 'name')
        self.assertNotEqual(reports.count,'text')
        self.assertTrue(reports.name)
        
        try:
           
            self.assertIsNotNone(reports.text)
        except AttributeError:
            raise "Field should not be null"

        # try:
        #     self.assertEqual(reports.name)
        # except:
        #     raise "worker not found"
