SELECT emp.cpf, emp.enome, dep.dnome
FROM empregados AS emp, departamentos AS dep
WHERE emp.dnumero = dep.dnumero
AND NOT EXISTS(SELECT DISTINCT empregados.enome 
               FROM empregados, trabalha
               WHERE empregados.cpf = trabalha.cpf_emp
               AND empregados.cpf = emp.cpf)
ORDER BY emp.cpf;

$$ language plpgsql;