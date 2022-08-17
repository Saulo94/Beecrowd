SELECT life_registry.name, CAST((life_registry.omega * 1.618) AS decimal(10,3)) AS fator
FROM life_registry, dimensions
WHERE life_registry.dimensions_id = dimensions.id
AND dimensions.name IN ('C774', 'C875')
AND life_registry.name LIKE 'Richard%'
ORDER BY fator;

$$ language plpgsql;