SELECT max(price) AS price, min(price) AS price
FROM products;

$$ language plpgsql;
