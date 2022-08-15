SELECT products.name
FROM products, providers
WHERE products.id_providers = providers.id
AND products.amount >= 10
AND products.amount <= 20
and providers.name LIKE 'P%';

$$ language plpgsql;