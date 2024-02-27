from typing import Literal

from aggregate.agregate import aggregate_salary_data
from aggregate.data import get_data_for_bson


def aggregate_main(
        input_data: dict[Literal["dt_from", "dt_upto", "group_type"], str]
) -> dict[str, list]:
    """
            Агрегирует статистические данные о зарплатах сотрудников компании по временным промежуткам.
            :param input_data: Словарь с входными данными
            :return: Словарь с агрегированными данными и метками.
            """
    get_data = get_data_for_bson()
    result = aggregate_salary_data(
        input_data["dt_from"], input_data["dt_upto"],
        input_data["group_type"], get_data
    )
    return result

