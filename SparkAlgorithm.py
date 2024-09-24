from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit


def get_product_category_pairs(products: DataFrame, categories: DataFrame, product_categories: DataFrame) -> DataFrame:
    """
    Возвращает датафрейм с парами "Имя продукта - Имя категории" и именами продуктов без категорий.

    Args:
        products: Датафрейм с информацией о продуктах
        categories: Датафрейм с информацией о категориях
        product_categories: Датафрейм с связями между продуктами и категориями

    Returns:
        Датафрейм с парами "Имя продукта - Имя категории" и именами продуктов без категорий (для
        удобства продукты без категорий добавляются вниз списка).
    """

    # Соединяем таблицы для получения пар "Имя продукта - Имя категории"
    product_category_pairs = products.join(product_categories, on='product_id', how='left') \
                                    .join(categories, on='category_id', how='left') \
                                    .filter(col('category_id').isNotNull()) \
                                    .select('product_name', 'category_name') \
                                    .orderBy('product_name', 'category_name')

    # Получаем список продуктов без категорий
    products_without_categories = products.join(product_categories, on='product_id', how='left') \
                                        .filter(col('category_id').isNull()) \
                                        .select('product_name') \
                                        .withColumn('category_name', lit(None)) \
                                        .orderBy('product_name', 'category_name')

    # Объединяем два датафрейма
    result_df = product_category_pairs.union(products_without_categories)

    return result_df
