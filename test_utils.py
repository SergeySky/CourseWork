
from utils import *


def test_filter_executed_operations():
    operations = [
        {"id": 1, "state": "EXECUTED", "description": "Operation 1"},
        {"id": 2, "state": "PENDING", "description": "Operation 2"},
        {"id": 3, "state": "EXECUTED", "description": "Operation 3"}
    ]
    expected_result = [
        {"id": 1, "state": "EXECUTED", "description": "Operation 1"},
        {"id": 3, "state": "EXECUTED", "description": "Operation 3"}
    ]

    executed_operations = filter_executed_operations(operations)

    assert executed_operations == expected_result


def test_sort_operations_by_date():
    operations = [
        {"id": 1, "date": "2022-01-02T00:00:00.000000"},
        {"id": 2, "date": "2022-01-01T00:00:00.000000"},
        {"id": 3, "date": "2022-01-03T00:00:00.000000"}
    ]
    expected_result = [
        {"id": 3, "date": "2022-01-03T00:00:00.000000"},
        {"id": 1, "date": "2022-01-02T00:00:00.000000"},
        {"id": 2, "date": "2022-01-01T00:00:00.000000"}
    ]

    sorted_operations = sort_operations_by_date(operations)

    assert sorted_operations == expected_result


def test_format_operation():
    operation = {
        "date": "2022-01-01T00:00:00.000000",
        "description": "Test Operation",
        "from": "123456789012345",
        "to": "123456789012345",
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD"}
        }
    }
    expected_result = "01.01.2022 Test Operation\n 1234 56** **** 2345 ->  1234 56** **** 2345\n100.00 USD "

    formatted_operation = format_operation(operation)

    assert formatted_operation == expected_result


def test_mask_card_number():
    card_number = "123456789012345"

    # Проверка для непустого значения card_number
    masked_number = mask_card_number(card_number)
    assert masked_number == " 1234 56** **** 2345"

    # Проверка для пустого значения card_number (список)
    card_number = []
    masked_number = mask_card_number(card_number)
    assert masked_number == "Список номеров карт пуст"

    # Проверка для пустого значения card_number (пустая строка)
    card_number = ""
    masked_number = mask_card_number(card_number)
    assert masked_number == "Номер карты не указан"


def test_display_last_5_operations(capsys):
    operations = [
        {"id": 1, "date": "2022-01-01T00:00:00.000000", "description": "Operation 1"},
        {"id": 2, "date": "2022-01-01T00:00:00.000000", "description": "Operation 2"},
        {"id": 3, "date": "2022-01-01T00:00:00.000000", "description": "Operation 3"},
        {"id": 4, "date": "2022-01-01T00:00:00.000000", "description": "Operation 4"},
        {"id": 5, "date": "2022-01-01T00:00:00.000000", "description": "Operation 5"}
    ]
    expected_output = (
        "Operation 5\n\n"
        "Operation 4\n\n"
        "Operation 3\n\n"
        "Operation 2\n\n"
        "Operation 1\n\n"
    )

    display_last_5_operations(operations)

    captured = capsys.readouterr()
    assert captured.out == expected_output
