SELECT categories.name, sum(products.amount) AS sum
FROM categories, products
WHERE products.id_categories = categories.id
GROUP BY categories.id;

$$ language plpgsql;
