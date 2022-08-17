WITH tmp_sender AS
(
	SELECT packages.id_package AS id, users.name AS sender
    FROM packages, users
    WHERE packages.id_user_sender = users.id
    AND (packages.color = 'blue' OR packages.year = 2015)
    AND users.address <> 'Taiwan'
), tmp_receiver AS
(
	SELECT packages.id_package AS id, users.name AS receiver
    FROM packages, users
    WHERE packages.id_user_receiver = users.id
    AND (packages.color = 'blue' OR packages.year = 2015)
    AND users.address <> 'Taiwan'
)

SELECT packages.year, tmp_sender.sender, tmp_receiver.receiver
FROM packages, tmp_sender
INNER JOIN tmp_receiver ON tmp_sender.id = tmp_receiver.id
WHERE tmp_sender.id = packages.id_package
ORDER BY packages.year DESC, tmp_sender.id DESC;

$$ language plpgsql;