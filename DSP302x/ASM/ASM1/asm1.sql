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
-- Q7:  
SELECT
    LEAGUE.name AS "League Name",
    count(*) AS "Number of match"
FROM
    MATCH
    LEFT OUTER JOIN LEAGUE ON MATCH.league_id = LEAGUE.id
GROUP BY
    league_id
ORDER BY
    count(*) DESC;

-- Q8:
SELECT
    LEAGUE.name AS "League Name",
    SUM(MATCH.home_team_goal) AS "Total Home Team Goal",
    SUM(MATCH.away_team_goal) AS "Total Away Team Goal"
FROM
    MATCH
    LEFT OUTER JOIN LEAGUE ON MATCH.league_id = LEAGUE.id
GROUP BY
    league_id;

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
-- Merging 3 tables into 1 -> Match Result
DROP VIEW IF EXISTS Match_Result;

CREATE VIEW IF NOT EXISTS Match_Result AS
SELECT
    match_api_id,
    home_team_api_id,
    away_team_api_id,
    home_team_goal,
    away_team_goal,
    CASE
        WHEN home_team_goal > away_team_goal THEN 1
        ELSE 0
    END AS H_Win,
    CASE
        WHEN home_team_goal < away_team_goal THEN 1
        ELSE 0
    END AS H_Lost,
    CASE
        WHEN home_team_goal == away_team_goal THEN 1
        ELSE 0
    END AS H_Draw
FROM
    MATCH;

DROP VIEW IF EXISTS Team_Result;

CREATE VIEW IF NOT EXISTS Team_Result AS
SELECT
    home_team_api_id AS "Team ID",
    CAST("H_Win" AS DECIMAL(10, 0)) AS "Win",
    CAST("H_Lost" AS DECIMAL(10, 0)) AS "Lost",
    CAST("H_Draw" AS DECIMAL(10, 0)) AS "Draw"
FROM
    Match_Result
UNION
ALL
SELECT
    away_team_api_id AS "Team ID",
    CAST("H_Win" AS DECIMAL(10, 0)) AS "Lost",
    CAST("H_Lost" AS DECIMAL(10, 0)) AS "Win",
    CAST("H_Draw" AS DECIMAL(10, 0)) AS "Draw"
FROM
    Match_Result;

SELECT
    "Team ID",
    Team.team_long_name AS "Full Name",
    CAST(Sum("Win") AS DECIMAL(10, 0)) AS "Total Win",
    CAST(Sum("Lost") AS DECIMAL(10, 0)) AS "Total Lost",
    CAST(Sum("Draw") AS DECIMAL(10, 0)) AS "Total Draw"
FROM
    Team_Result
    LEFT OUTER JOIN Team ON Team.team_api_id = Team_Result."Team ID"
GROUP BY
    "Team ID"
ORDER BY
    "Total Win" DESC;

-- Q15 contain only in ipynb
-- Q16: Get percentage of each league total matches versus all leagues
DROP VIEW IF EXISTS League_Total_Matches;

CREATE VIEW IF NOT EXISTS League_Total_Matches AS
SELECT
    league_id AS "League ID",
    League.name AS "League Name",
    CAST(Count("Match ID") AS DECIMAL(10, 0)) AS "Total Matches"
FROM
    MATCH
    LEFT OUTER JOIN League ON League.id = "League ID"
GROUP BY
    "League ID";

SELECT
    "League ID",
    "League Name",
    CAST("Total Matches" * 100 AS DECIMAL(10, 2)) / CAST(
        (
            SELECT
                Sum("Total Matches")
            FROM
                League_Total_Matches
        ) AS DECIMAL(10, 2)
    ) AS "Total Matches Percentage"
FROM
    League_Total_Matches;

-- Q17: Get percentage of goal in each league
DROP VIEW IF EXISTS League_Total_Goals;

CREATE VIEW IF NOT EXISTS League_Total_Goals AS
SELECT
    league_id AS "League ID",
    League.name AS "League Name",
    Sum(home_team_goal + away_team_goal) AS "Total Goals"
FROM
    MATCH
    LEFT OUTER JOIN League ON MATCH.league_id = League.id
GROUP BY
    league_id
ORDER BY
    "Total Goals" DESC;

SELECT
    "League ID",
    "League Name",
    CAST("Total Goals" * 100 AS DECIMAL(10, 2)) / CAST(
        (
            SELECT
                Sum("Total Goals")
            FROM
                League_Total_Goals
        ) AS DECIMAL(10, 2)
    ) AS "Total Goals Percentage"
FROM
    League_Total_Goals;

-- Q18: Get total numbers of goals for each league in each season
DROP VIEW IF EXISTS Match_Goal;

CREATE VIEW IF NOT EXISTS Match_Goal AS
SELECT
    match_api_id,
    season,
    home_team_goal + away_team_goal AS "Goals"
FROM
    MATCH;

SELECT
    season,
    Sum("Goals") AS "Total Goals"
FROM
    Match_goal
GROUP BY
    season;

-- Q19: Get player attributes
-- - Convert weight to kilogram
-- - Convert height to meter
-- - Calculuate bmi = ( (weight* 0.453592) / (height/100)^2)
-- - Get Age of player
SELECT
    player_api_id AS "Player ID",
    player_name AS "Player Name",
    weight * 0.454 AS "Weight (kg)",
    height / 100 AS "Height (meter)",
    (
        weight * 0.454 / (height * height / 10000)
    ) AS "BMI",
    (
        strftime('%Y', 'now') - strftime('%Y', birthday)
    ) AS "Age"
FROM
    Player;

-- Q20: Get oldest player
-- Doing by sort and limit
SELECT
    player_api_id AS "Player ID",
    player_name AS "Player Name",
    (
        strftime('%Y', 'now') - strftime('%Y', birthday)
    ) AS "Age"
FROM
    Player
ORDER BY
    "Age" DESC
LIMIT
    1;

-- Q21: Get players who played highest number of matches
-- Moi doi co 2 luot di - ve. UNION ALL query data tu luot di luot ve
-- Su dung ID 11 cau thu Join voi bang Player
SELECT
    Player_Attributes.player_api_id AS "Player ID",
    Player.player_name AS "Full Name",
    Count(*) AS "Number of Matches"
FROM
    Player_Attributes
    LEFT OUTER JOIN Player ON Player_Attributes.player_api_id = Player.player_api_id
GROUP BY
    "Player ID"
ORDER BY
    "Number of matches" DESC
LIMIT
    1;

-- Question 22: Get players who had overall_rating larger than 80
SELECT
    "Player ID",
    "Full Name",
    "Average Overall Rating"
FROM
    (
        SELECT
            Player_Attributes.player_api_id AS "Player ID",
            Player.player_name AS "Full Name",
            AVG(overall_rating) AS "Average Overall Rating"
        FROM
            Player_Attributes
            LEFT OUTER JOIN Player ON Player_Attributes.player_api_id = Player.player_api_id
        GROUP BY
            "Player ID"
    )
WHERE
    "Average Overall Rating" >= 80
ORDER BY
    "Average Overall Rating" DESC;