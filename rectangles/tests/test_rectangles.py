import unittest
from rectangles.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 5, 2, 2)

    def test_right_bottom_intersection(self):
        other = Rectangle(6, 6, 2, 2)
        intersected = self.rectangle.intersects(other)
        self.assertTrue(intersected)

    def test_left_bottom_intersection(self):
        other = Rectangle(4, 6, 2, 2)
        intersected = self.rectangle.intersects(other)
        self.assertTrue(intersected)

    def test_left_upper_intersection(self):
        other = Rectangle(4, 4, 2, 2)
        intersected = self.rectangle.intersects(other)
        self.assertTrue(intersected)

    def test_right_upper_intersection(self):
        other = Rectangle(6, 4, 2, 2)
        intersected = self.rectangle.intersects(other)
        self.assertTrue(intersected)

    def test_no_intersection(self):
        other = Rectangle(10, 10, 2, 2)
        intersected = self.rectangle.intersects(other)
        self.assertFalse(intersected)

    def test_full_intersection(self):
        other = Rectangle(0, 0, 10, 10)
        intersected = self.rectangle.intersects(other)
        self.assertTrue(intersected)

    def test_commutative_property(self):
        other = Rectangle(0, 0, 10, 10)
        self.assertEqual(self.rectangle.intersects(other), other.intersects(self.rectangle))

if __name__ == '__main__':
    unittest.main()