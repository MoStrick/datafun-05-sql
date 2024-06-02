-- query_group_by.sql

SELECT user_id, COUNT(order_id) as order_count FROM Orders GROUP BY user_id;
-- Add more group by queries as needed
