SELECT CONCAT(SUBSTRING(np.cpf,  1,  3), '.', 
              SUBSTRING(np.cpf,  4,  3), '.', 
              SUBSTRING(np.cpf,  7,  3), '-', 
              SUBSTRING(np.cpf, 10, 2)) AS CPF
FROM customers, natural_person as np
WHERE customers.id = np.id_customers;

$$ language plpgsql;