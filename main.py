import json


def display_last_operations():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Функция для получения статуса операции из словаря
        def get_state(operation):
            return operation.get('state', '')

        # Сортируем операции по дате в обратном порядке
        sorted_operations = sorted(data, key=lambda x: x.get('date', ''), reverse=True)

        # Отображаем только последние 5 выполненных операций
        last_operations = [operation for operation in sorted_operations if get_state(operation) == 'EXECUTED'][:5]

        for operation in last_operations:
            date = operation.get('date', '').split('T')[0]  # Получаем дату без времени
            description = operation['description']
            from_account = operation.get('from', '')
            to_account = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            masked_from_account = from_account.replace(from_account[:6], '******') if from_account else ''
            masked_to_account = '**** ' + to_account[-4:]

            print(f"{date} {description}")
            print(f"{masked_from_account} -> {masked_to_account}")
            print(f"{amount} {currency}\n")

# Пример использования
display_last_operations()
