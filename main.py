from area_library import Circle, Triangle, calculate_area
from pyspark.sql import SparkSession
import SparkAlgorithm

# Пример использования библиотеки геометрических фигур
circle = Circle(7)
area_circle = calculate_area(circle)
print(f"Площадь круга: {area_circle}")

triangle = Triangle(6, 8, 10)
area_triangle = calculate_area(triangle)
print(f"Площадь треугольника: {area_triangle}")

# Пример использования Spark-алгоритма
spark = SparkSession.builder.appName("ProductCategories").getOrCreate()

# Датафрейм продуктов
products_data = [
    (1, "Product 1"),
    (2, "Product 2"),
    (3, "Product 3"),
    (4, "Product 4")
]
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

# Датафрейм категорий
categories_data = [
    (1, "Category 1"),
    (2, "Category 2"),
    (3, "Category 3")
]
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])

# Датафрейм связей продуктов и категорий
product_categories_data = [
    (1, 2),
    (1, 3),
    (2, 2),
    (4, 3)
]
product_categories_df = spark.createDataFrame(product_categories_data, ["product_id", "category_id"])

# Вывод результата
result_df = SparkAlgorithm.get_product_category_pairs(products_df, categories_df, product_categories_df)
result_df.show()
spark.stop()
