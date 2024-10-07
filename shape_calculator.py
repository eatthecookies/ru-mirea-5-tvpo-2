import math

# Функция для вычисления площади круга
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Функция для вычисления периметра прямоугольника
def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

# Функция для вычисления площади треугольника
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Функция для вычисления объема сферы
def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

# Функция для вычисления объема цилиндра (с ошибкой)
def calculate_cylinder_volume(radius, height):
    return 2 * math.pi * radius * height
