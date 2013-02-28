from django.test import TestCase
from animals.models import Animals


class SimpleTest(TestCase):
    def setUp(self):
        """
        This is run prior to each test.
        """
        self.animal1 = Animals.objects.create(
            name='Bear',
        )

    def test_animal_created(self):
        """
        Test if setup executed correctly.
        If test passes then animal objects
        can be instantiated correctly
        """
        self.assertEquals(self.animal1.name, 'Bear')
