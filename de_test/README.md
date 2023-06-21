# Data Engineer test case 

## Data Engineer test case for API parsing

### Task 1.
You need to research data from Itunes API of TOP paid applications in Russia for next tasks:
- define the model of data by spliting them to main data - some kind of daily rate of definite market research and guides which could present additional attributes of main data with relation's information for storing into DB
- make presentation of which tool you choose for scheduled ETL process into DB
[Task 1. Solution](https://github.com/sllivswl/Tests/blob/main/de_test/api/Task_1_parser_for_API_solutions.ipynb)

## Data Engineer test case for pandas using

### Task 1.
The task involves developing a data pipeline to complete the user story above using sample data sources that will be provided.

Our data science team has reached out to our data engineering team requesting we pre-process
some of the data for them at scale so that they can make better use of it in their downstream algorithms.

The input data sources are comprised of customers (in CSV format), transactions (in JSON Lines format) and products (in CSV format). Their details are presented below
[Task 1. Solution](https://github.com/sllivswl/Tests/blob/main/de_test/pandas/Task_1_Pandas_using_solutions.ipynb)

## Data Engineer test case for SQL using

### Task 1.
For each product, get the minimum and maximum cost from the product_price table. Output the columns:

- product_id - product identifier;
- price_min - the minimum cost of the product;
- price_max - the maximum cost of the product.

As a result, leave only those products for which the minimum and maximum cost are different.

Sort the result by the product ID.
[Task 1. Solution](https://github.com/sllivswl/Tests/blob/main/de_test/sql/Task_1_SQL_using_solution.ipynb)
