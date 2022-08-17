WITH 
podium AS
(
SELECT position, CONCAT('Podium: ', team) as name
FROM league
ORDER BY position
LIMIT 3
), 
demoted AS
(
SELECT position, CONCAT('Demoted: ', team) as name
FROM league
ORDER BY position DESC
LIMIT 2
)

SELECT name 
FROM (SELECT position, name FROM podium
	  UNION 
	  SELECT position, name FROM demoted
	  ORDER BY position) AS tmp;

$$ language plpgsql;