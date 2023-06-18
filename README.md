# CourseWork
Отслеживание банковских операций
Отслеживание банковских операций - это скрипт на языке Python, который загружает и обрабатывает данные о банковских операциях из файла JSON. Он фильтрует выполненные операции, сортирует их по дате и выводит последние 5 операций в форматированном виде.

Установка
Склонируйте репозиторий или загрузите файл скрипта (utils.py) на ваше локальное устройство.

Убедитесь, что у вас установлена Python версии 3.x.

Использование
Поместите файл с данными операций (operations.json) в ту же директорию, где находится скрипт utils.py.

Запустите скрипт utils.py с помощью команды python utils.py.

Результаты выполнения скрипта будут выведены в консоль. Будут отображены последние 5 операций, отсортированные по дате.

Зависимости
Скрипт не имеет зависимостей от сторонних библиотек.

Примечания
Входные данные должны быть в формате JSON и соответствовать структуре, ожидаемой скриптом.

Если данные операций содержат некорректные или отсутствующие значения, скрипт может вызвать ошибки или выдать неправильные результаты.

Убедитесь, что файл с данными операций (operations.json) находится в той же директории, где находится скрипт utils.py, и имеет правильное имя и формат.

Для получения более подробной информации о каждой операции и ее форматировании, обратитесь к комментариям внутри скрипта utils.py.