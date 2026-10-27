"""Учебный модуль для контроля выполнения задач проекта"""


def completion_percent(done: int, total: int) -> int:
    """Вычисляет процент выполненных задач."""
    if total <= 0:
        raise ValueError("Общее число задач должно быть больше нуля")
    if not 0 <= done <= total:
        raise ValueError("Число выполненных задач некорректно")
    return round(done * 100 / total)
