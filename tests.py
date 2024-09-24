"""
 Юнит-тесты: Предоставлены тесты для проверки корректности вычисления площади круга
 и треугольника, а также для проверки возможности построения треугольника и определения,
 является ли он прямоугольным
"""
import area_library
import unittest

class TestFigure(unittest.TestCase):
    def test_circle(self):
        circle = area_library.Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=2)

    def test_triangle(self):
        triangle = area_library.Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6.0)

        with self.assertRaises(ValueError):
            area_library.Triangle(1, 2, 5)  # Невозможный треугольник

    def test_is_right_triangle(self):
        triangle = area_library.Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = area_library.Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area(self):
        circle = area_library.Circle(5)
        self.assertAlmostEqual(area_library.calculate_area(circle), 78.53981633974483, places=2)

        triangle = area_library.Triangle(3, 4, 5)
        self.assertEqual(area_library.calculate_area(triangle), 6.0)

if __name__ == '__main__':
   unittest.main()
