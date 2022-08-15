SELECT doc.name, 
       SUM(ROUND(((150 * att.hours) * (1 + (ws.bonus / 100))), 1)) as salary
FROM doctors AS doc, work_shifts AS ws, attendances AS att
WHERE doc.id = att.id_doctor
AND ws.id = att.id_work_shift
GROUP BY doc.name
ORDER BY salary DESC;

$$ language plpgsql;