from datetime import datetime
from typing import Any

from aggregate.backend import _aggregate_data, _generate_dataset_and_labels


def aggregate_salary_data(
        dt_from: str, dt_upto: str,
        group_type: str, data: list[dict[str, Any]]
) -> dict[str, list[Any]]:
    """
        Агрегирует статистические данные о зарплатах сотрудников компании по временным промежуткам.
        :param dt_from: Начало отсчета.
        :param dt_upto: Дата окончания.
        :param group_type: Группировка по (hour, day....).
        :param data: массив с агрегируемыми данными
        :return: Словарь с агрегированными данными и метками.
        """
    dt_from = datetime.fromisoformat(dt_from)
    dt_upto = datetime.fromisoformat(dt_upto)
    aggregated_data = _aggregate_data(dt_from, dt_upto, group_type, data)
    dataset, labels = _generate_dataset_and_labels(dt_from, dt_upto, group_type, aggregated_data)
    return {"dataset": dataset, "labels": labels}
