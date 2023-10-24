-- SELECT
--     *
-- FROM
--     LEAGUE
--     INNER JOIN COUNTRY ON LEAGUE.country_id = COUNTRY.id;
--
-- SELECT
--     MATCH.id,
--     MATCH.country_id,
--     MATCH.league_id,
--     Country.name,
--     League.name
-- FROM
--     MATCH
--     LEFT OUTER JOIN Country ON MATCH.country_id = Country.id
--     LEFT OUTER JOIN League ON MATCH.league_id = League.id;
--
-- SELECT
--     league_id,
--     LEAGUE.name,
--     count(*) AS "Number of match"
-- FROM
--     MATCH
--     LEFT OUTER JOIN LEAGUE ON MATCH.league_id = LEAGUE.id
-- GROUP BY
--     league_id
-- ORDER BY
--     count(*) DESC;
--
-- SELECT
--     MATCH.league_id,
--     LEAGUE.name,
--     SUM(MATCH.home_team_goal) AS "Total Home Team Goal",
--     SUM(MATCH.away_team_goal) AS "Total Away Team Goal"
-- FROM
--     MATCH
--     LEFT OUTER JOIN LEAGUE ON MATCH.league_id = LEAGUE.id
-- GROUP BY
--     league_id;
--
-- SELECT
--     MATCH.home_team_api_id AS "Team ID",
--     TEAM.team_long_name AS "Team Name",
--     SUM(MATCH.home_team_goal) AS "Total Home Team Goal"
-- FROM
--     MATCH
--     LEFT OUTER JOIN TEAM ON MATCH.home_team_api_id = TEAM.team_api_id
-- GROUP BY
--     MATCH.home_team_api_id
-- ORDER BY
--     "Total Home Team Goal" DESC
-- LIMIT
--     20;
--
-- --
-- SELECT
--     MATCH.away_team_api_id AS "Team ID",
--     TEAM.team_long_name AS "Team Name",
--     SUM(MATCH.away_team_goal) AS "Total Away Team Goal"
-- FROM
--     MATCH
--     LEFT OUTER JOIN TEAM ON MATCH.away_team_api_id = TEAM.team_api_id
-- GROUP BY
--     MATCH.away_team_api_id
-- ORDER BY
--     "Total Away Team Goal" DESC
-- LIMIT
--     20;
--
-- --
-- SELECT
--     MATCH.match_api_id AS "Match ID",
--     MATCH.home_team_api_id AS "Team ID",
--     TEAM.team_long_name AS "Team Name",
--     MATCH.home_team_goal AS "home_goal",
--     MATCH.away_team_goal AS "away_goal",
--     (MATCH.home_team_goal + MATCH.away_team_goal) AS team_goal -- SUM(MATCH.team_goal) AS "Total Team Goal"
-- FROM
--     MATCH
--     LEFT OUTER JOIN TEAM ON MATCH.home_team_api_id = TEAM.team_api_id
-- UNION
-- ALL
-- SELECT
--     MATCH.match_api_id AS "Match ID",
--     MATCH.away_team_api_id AS "Team ID",
--     TEAM.team_long_name AS "Team Name",
--     MATCH.home_team_goal AS "home_goal",
--     MATCH.away_team_goal AS "away_goal",
--     (MATCH.home_team_goal + MATCH.away_team_goal) AS team_goal -- SUM(MATCH.team_goal) AS "Total Team Goal"
-- FROM
--     MATCH
--     LEFT OUTER JOIN TEAM ON MATCH.away_team_api_id = TEAM.team_api_id,
--     --
--     -- SELECT product, SUM(amount) AS total_sales
--     -- FROM (
--     --     SELECT product, amount FROM sales_2020
--     --     UNION ALL
--     --     SELECT product, amount FROM sales_2021
--     -- ) AS combined_sales
--     -- GROUP BY product;
--     --
-- SELECT
--     MATCH.match_api_id AS "Match ID",
--     MATCH.home_team_api_id AS "Home Team ID",
--     MATCH.away_team_api_id AS "Away Team ID",
--     MATCH.home_team_goal,
--     MATCH.away_team_goal,
--     (MATCH.home_team_goal + MATCH.away_team_goal) AS team_goal
-- FROM
--     MATCH
-- UNION
-- ALL
-- SELECT
--     MATCH.match_api_id AS "Match ID",
--     MATCH.home_team_api_id AS "Home Team ID",
--     MATCH.away_team_api_id AS "Team ID",
--     MATCH.home_team_goal,
--     MATCH.away_team_goal,
--     (MATCH.home_team_goal + MATCH.away_team_goal) AS team_goal
-- FROM
--     MATCH;
--
-- -- LEFT OUTER JOIN TEAM ON MATCH.home_team_api_id = TEAM.team_api_id
-- -- LEFT OUTER JOIN TEAM ON MATCH.away_team_api_id = TEAM.team_api_id;
-- -- TEAM.team_long_name AS "Team Name",
-- -- TEAM.team_long_name AS "Team Name",
--
-- Q12:
SELECT
    "Team ID",
    TEAM.team_long_name AS "Full Name",
    SUM("Goals") AS "Total Goals (Both Away and Home)"
FROM
    (
        SELECT
            MATCH.match_api_id AS "Match ID",
            MATCH.home_team_api_id AS "Team ID",
            MATCH.home_team_goal AS "Goals"
        FROM
            MATCH
        UNION
        SELECT
            MATCH.match_api_id AS "Match ID",
            MATCH.away_team_api_id AS "Team ID",
            MATCH.away_team_goal AS "Goals"
        FROM
            MATCH
    )
    LEFT OUTER JOIN TEAM ON "Team ID" = TEAM.team_api_id
GROUP BY
    "Team ID"
ORDER BY
    "Total Goals (Both Away and Home)" DESC;

-- Q13: Get team long name with total of matches, order the total number by descending
SELECT
    "Team ID",
    TEAM.team_long_name AS "Full Name",
    COUNT("Team ID") AS "Total Matches (Both Away and Home)"
FROM
    (
        SELECT
            MATCH.match_api_id AS "Match ID",
            MATCH.home_team_api_id AS "Team ID"
        FROM
            MATCH
        UNION
        SELECT
            MATCH.match_api_id AS "Match ID",
            MATCH.away_team_api_id AS "Team ID"
        FROM
            MATCH
    )
    LEFT OUTER JOIN TEAM ON "Team ID" = TEAM.team_api_id
GROUP BY
    "Team ID"
ORDER BY
    "Total Matches (Both Away and Home)" DESC;

--
-- Q14: Get numbers of win, lost and draw matches of each team
-- - If a team has home goal > away goal , team is “win” in this match
-- - If a team has home goal < away goal , team is “lost” in this match
-- - If a team has home goal = away goal , team is “draw” in this match
-- - Use Case When statement
-- Tables needed: Match
-- Tables process: (Home View column: match_id, home_team_api_id)
DROP VIEW IF EXISTS Match_View;

CREATE VIEW IF NOT EXISTS Match_View AS
SELECT
    match_api_id,
    home_team_api_id,
    home_team_goal,
    away_team_api_id,
    away_team_goal
FROM
    MATCH;

SELECT
    *
FROM
    Match_View;

-- Tables results: a View with match_api_id, home_team_api_id, away_team_api_id, results
-- Merge from 2 views
DROP VIEW IF EXISTS Match_Result;

CREATE VIEW IF NOT EXISTS Match_Result AS
SELECT
    m.match_api_id,
    m.home_team_api_id,
    m.away_team_api_id,
    CASE
        WHEN m.home_team_goal > m.away_team_goal THEN 'Win'
        WHEN m.home_team_goal == m.away_team_goal THEN 'Draw'
        WHEN m.home_team_goal < m.away_team_goal THEN 'Lost'
        ELSE NULL
    END AS result
FROM
    Match_View AS m;

CREATE VIEW IF NOT EXISTS Team_Result AS
SELECT
    m.home_team_api_id AS "TEAM ID",
    m.result
FROM
    Match_Result AS m
UNION
ALL
SELECT
    m.home_team_api_id AS "TEAM ID",
    CASE
        WHEN m.result == 'Lost' THEN 'Win'
        WHEN m.result == 'Draw' THEN 'Draw'
        WHEN m.result == 'Win' THEN 'Lost'
        ELSE NULL
    END AS result
FROM
    Match_Result AS m;

SELECT
    "Team ID",
    Team.team_long_name AS "Full Name",
    result
FROM
    Team_Result
    LEFT OUTER JOIN Team ON Team_Result."Team ID" = Team.team_api_id
GROUP BY
    "Team ID";

SELECT
    "Team ID",
    Team.team_long_name AS "Full Name",
    COUNT(*) AS count
FROM
    Team_Result
    LEFT OUTER JOIN Team ON "Team ID" = Team.team_api_id
GROUP BY
    "Team ID",
    result
ORDER BY
    count DESC;