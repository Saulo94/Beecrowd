WITH tmp AS 
(
SELECT teams_tmp.name,
	   (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
        AND teams.name = teams_tmp.name) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
        AND teams.name = teams_tmp.name) AS matches_tmp,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = teams_tmp.name
        AND matches.team_1_goals > matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = teams_tmp.name
        AND matches.team_2_goals > matches.team_1_goals) AS victories,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = teams_tmp.name
        AND matches.team_1_goals < matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = teams_tmp.name
        AND matches.team_2_goals < matches.team_1_goals) AS defeats,
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_1
       	AND teams.name = teams_tmp.name
        AND matches.team_1_goals = matches.team_2_goals) +
       (SELECT COUNT(*)
        FROM teams, matches
        WHERE teams.id = matches.team_2
       	AND teams.name = teams_tmp.name
        AND matches.team_2_goals = matches.team_1_goals) AS draws
FROM teams AS teams_tmp
)

SELECT teams_tmp2.name,
	   matches_tmp AS matches,
       victories,
       defeats,
       draws,
      (SELECT victories * 3 + draws
       FROM tmp WHERE tmp.name = teams_tmp2.name) AS score
FROM tmp as teams_tmp2
ORDER BY score DESC, name;

$$ language plpgsql;