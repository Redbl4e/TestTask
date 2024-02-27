from typing import Any

import bson


def get_data_for_bson() -> list[dict[str, Any]]:
    """
    Получает данные из bson файла.
    :return Список со словарями.
    """
    with open("aggregate/sample_collection.bson", "rb") as f:
        bson_data = bson.decode_all(f.read())
    return bson_data
