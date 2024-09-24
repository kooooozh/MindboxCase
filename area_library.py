"""
 Базовый класс `Figure`: Определяет общий интерфейс для вычисления площади фигуры.
 Классы `Circle` и `Triangle`: наследуются от `Figure` и реализуют метод `area()`
 для вычисления площади соответствующей фигуры.
 Дополнительные фигуры могут быть добавлены путем создания новых классов,
 наследующихся от `Figure` и реализующих метод `area()`.
 Вычисление площади без знания типа фигуры в compile-time осуществляется
 с помощью функции calculate_area() - для этого используется полиморфизм.
"""
import math


class Figure:
    """ Базовый класс для геометрических фигур """

    def area(self):
        """ Вычисление площади фигуры """

        raise (NotImplementedError("""Метод area должен быть переопределен в подклассах"""))


class Circle(Figure):
    """ Класс для круга """

    def __init__(self, radius):
        self.radius = radius

        # Проверка неотрицательности радиуса круга
        if radius < 0:
            raise(ValueError("Радиус круга не может быть отрицательным"))

    def area(self):
        return math.pi * self.radius * self.radius


class Triangle(Figure):
    """ Класс для треугольника """

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        # Проверка возможности построения треугольника
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise (ValueError("Невозможно построить треугольник с данными сторонами"))

    def area(self):
        # Вычисление площади по формуле Герона
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        """ Проверка, является ли треугольник прямоугольным """
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2


def calculate_area(figure):
    """ Вычисление площади фигуры без знания ее типа """
    return figure.area()
