SELECT cust.id, cust.name
FROM customers as cust
WHERE NOT EXISTS(SELECT * FROM customers, locations
                 WHERE customers.id = locations.id_customers
                 AND customers.id = cust.id)
ORDER BY cust.id;

$$ language plpgsql;