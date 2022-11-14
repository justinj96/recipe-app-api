from django.test import SimpleTestCase

from app import calc


class Calctests(SimpleTestCase):
    """Test Calc Module"""

    def test_add_numbers(self):
        """Test adding nums together"""

        res = calc.add(5, 6)
        self.assertEquals(res, 11)
