-- query_join.sql

SELECT Users.username, Orders.order_date, Orders.amount
FROM Users
INNER JOIN Orders ON Users.user_id = Orders.user_id;
-- Add more joins as needed
