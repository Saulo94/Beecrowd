WITH tmp AS 
(SELECT teams.name as name_tmp,
	   (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
        AND teams.name = name_tmp) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
        AND teams.name = name_tmp) AS matches_tmp,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = name_tmp
        AND matches.team_1_goals > matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = name_tmp
        AND matches.team_2_goals > matches.team_1_goals) AS victories,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = name_tmp
        AND matches.team_1_goals < matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = name_tmp
        AND matches.team_2_goals < matches.team_1_goals) AS defeats,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = name_tmp
        AND matches.team_1_goals = matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = name_tmp
        AND matches.team_2_goals = matches.team_1_goals) AS draws
FROM teams)

SELECT name_tmp as name, 
	   matches_tmp as matches,
       victories, 
       defeats, 
       draws,
	   (SELECT victories * 3 + draws
        FROM tmp
        WHERE name_tmp = name) AS score
FROM tmp
ORDER BY score DESC, name;

$$ language plpgsql;