# Data Engineer test case for SQL using

## Task 1

For each product, get the minimum and maximum cost from the product_price table. Output the columns:

- product_id - product identifier;
- price_min - the minimum cost of the product;
- price_max - the maximum cost of the product.

As a result, leave only those products for which the minimum and maximum cost are different.

Sort the result by the product ID.

## Результат

Создала итоговый запрос в несколько итераций, присоединяя по кусочку и выводя результат, чтобы убедиться в корректности.
1. Собрала подзапрос с группировкой `min/max` цен по `product_id` из `product_price`;
2. Приджойнила к `product` подзапрос с группировкой;
3. Указала условие фильтрации (различия между ценами) и порядок отображения записей. 

```bash
'''
WITH prices_agg
     AS (SELECT p.product_id,
                Min(p.price) AS price_min,
                Max(p.price) AS price_max
         FROM   product_price p
         GROUP  BY p.product_id)
SELECT t.product_id,
       p.price_min,
       p.price_max
FROM   product t
       LEFT JOIN prices_agg p
              ON t.product_id = p.product_id
WHERE  p.price_min != p.price_max
ORDER  BY t.product_id 
'''
```