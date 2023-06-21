# Data Engineer test case for pandas using

## Task 1

The task involves developing a data pipeline to complete the user story above using sample data sources that will be provided.

Our data science team has reached out to our data engineering team requesting we pre-process
some of the data for them at scale so that they can make better use of it in their downstream algorithms.

The input data sources are comprised of customers (in CSV format), transactions (in JSON Lines format) and products (in CSV format). Their details are presented below

## Результат 

Я вытащила покупки из таблицы транзакций, сгруппировала их по пользователям и посчитала количество для каждого типа продукта. Затем вновь разбила их, чтобы присоединить категории продукта и данные о лояльности пользователей. 

Для передачи данных я написала скрипт с пайплайном `customers_transactions.py`, который преобразует данные и сохраняет итоговый датасет в формте `.csv`.

Generate output_data:
```bash
python generate_data/generator.py
python generate_data/customers_transactions.py
```
