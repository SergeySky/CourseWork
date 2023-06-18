import json
import re

from datetime import datetime


def load_operations():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


operations_data = load_operations()


def filter_executed_operations(operations):
    executed_operations = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


executed_operations = filter_executed_operations(operations_data)


def sort_operations_by_date(operations):
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations


sorted_operations = sort_operations_by_date(executed_operations)


def format_operation(operation):
    raw_date = operation['date']
    formatted_date = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

    description = operation['description']
    from_account = operation.get('from', ' ')
    to_account = operation['to']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    formatted_operation = f"{formatted_date} {description}\n{mask_card_number(from_account)} -> {mask_card_number(to_account)}\n{amount} {currency} "
    return formatted_operation


def mask_card_number(card_number):
    if isinstance(card_number, list) and not card_number:
        # Код для обработки пустого списка card_number
        masked_number = "Список номеров карт пуст"
    elif card_number:
        # Код для обработки непустого значения card_number
        if "Счет " in card_number:
            account_number = re.search(r'\d+', card_number).group()
            masked_number = "Счет " + mask_account_number(account_number)
        else:
            sender = card_number.split()
            if sender:
                from_bill = sender.pop(-1)
                from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
                from_info = " ".join(sender)
                masked_number = f"{from_info} {from_bill}"
            else:
                masked_number = "Пополнение счета"
    else:
        # Код для обработки других случаев
        masked_number = "Номер карты не указан"
    return masked_number


def mask_account_number(account_number):
    # Маскирование номера счета
    masked_number = '**' + account_number[-4:]
    return masked_number


def display_last_5_operations(operations):
    last_5_operations = operations[:5]
    for operation in last_5_operations:
        formatted_operation = format_operation(operation)
        print(formatted_operation)
        print()


display_last_5_operations(sorted_operations)
