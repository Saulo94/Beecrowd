LOAD 'plpgsql';

SELECT name FROM customers WHERE state = 'RS';
$$ language plpgsql;
