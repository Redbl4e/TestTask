from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any


def _aggregate_data(
        dt_from: datetime, dt_upto: datetime,
        group_type: str, data: list[dict[str, Any]]
) -> dict[datetime, int]:
    """
        Агрегирует данные в соответствии с указанным типом группировки.
        :param dt_from: Начало отсчета.
        :param dt_upto: Дата окончания.
        :param group_type: Тип группировки (hour, day, month).
        :param data: Статистические данные.
        :return: Словарь с агрегированными данными.
        """
    aggregated_data = defaultdict(int)
    for item in data:
        record_date = item['dt']
        if dt_from <= record_date <= dt_upto:
            key = _get_key(record_date, group_type)
            aggregated_data[key] += item['value']
    return aggregated_data


def _get_key(record_date: datetime, group_type: str) -> datetime:
    """
    Определяет ключ для агрегации данных в зависимости от типа группировки.
    :param record_date: Дата записи.
    :param group_type: Тип группировки (hour, day, month).
    :return: Ключ для агрегации данных(час|день|месяц).
    """

    if group_type == 'hour':
        return record_date.replace(minute=0, second=0, microsecond=0)
    elif group_type == 'day':
        return record_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elif group_type == 'month':
        return record_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def _generate_dataset_and_labels(
        dt_from: datetime, dt_upto: datetime, group_type: str,
        aggregated_data: dict[datetime, int]) -> tuple[list[int], list[str]]:
    """
        Агригирует датасет и метки в соответствии с типом группировки.
        :param dt_from: Начало отсчета.
        :param dt_upto: Дата окончания.
        :param group_type: Тип группировки (hour, day, month).
        :param aggregated_data: Агрегированные данные.
        :return: Датасет и метки.
        """
    dataset = []
    labels = []
    if group_type == 'month':
        labels = [dt.isoformat() for dt in aggregated_data.keys()]
        dataset = list(aggregated_data.values())
    else:
        delta = timedelta(days=1) if group_type == 'day' else timedelta(hours=1)
        current_date = dt_from
        while current_date <= dt_upto:
            dataset.append(aggregated_data[current_date])
            labels.append(current_date.isoformat())
            if group_type == 'day':
                current_date += timedelta(days=1)
            elif group_type == 'hour':
                current_date += timedelta(hours=1)
    return dataset, labels
