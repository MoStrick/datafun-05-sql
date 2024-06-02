-- query_aggregation.sql

SELECT user_id, COUNT(order_id) as order_count FROM Orders GROUP BY user_id;
SELECT AVG(amount) as average_amount FROM Orders;
SELECT SUM(amount) as total_amount FROM Orders;
-- Add more aggregations as needed
