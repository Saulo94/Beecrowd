SELECT candidate.name, 
       ROUND(((sc.math * 2) + (sc.specific * 3) + (sc.project_plan * 5)) / 10, 2) AS avg
FROM candidate, score AS sc
WHERE candidate.id = sc.candidate_id
ORDER BY avg DESC;

$$ language plpgsql;
