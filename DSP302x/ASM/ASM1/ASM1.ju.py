# %% [markdown]
# # Project Overview
#
# You receive a European Soccer Database that has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016. The goal is you walk through this database to do analysis include some steps for exploring our dataset, some steps for basics statistics and then you visualize the result. To complete all your steps, you need to query your data in the database using SQL statement. This project practices you write SQL command to pull data and extrac it.

# %% [markdown]
# # Database Description
#
# This European Soccer Database has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016, 11 European Countries with their lead championship. Players and Teams' attributes sourced from EA Sports' FIFA video game series, including the weekly updates.

# %% [markdown]
# # Import Python package

# %%
# Import libraries
import numpy as np
import pandas as pd
import sqlite3
from datetime import timedelta
import warnings

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 100)

# %% [markdown]
# ## Question 1: Connect to database and get information of all tables
#
# Read https://docs.python.org/2/library/sqlite3.html
#
# You write only SQL statement to get the result, should not use Pandas to manipulate result.

# %%
# Connect to database
conn = sqlite3.connect("./database.sqlite")

# and get information of all tables
tables = pd.read_sql(
    """SELECT *
                        FROM sqlite_master
                        WHERE type='table';""",
    conn,
)
tables

# %% [markdown]
# ## Question 2: Select data in "Country" table

# %%
# Normal Table Select
q2 = pd.read_sql("SELECT * FROM COUNTRY;", conn)
q2

# %% [markdown]
# ## Question 3: Select data in "League" table

# %%
# Normal Table Select
q3 = pd.read_sql("SELECT * FROM LEAGUE;", conn)
q3

# %% [markdown]
# ## Question 4: Select League data with country information
# The League table has relation with Country table by country_id. Use the join sql statement to join two tables.

# %%
# Join 2 tables with Inner Join on country id
# Can use left outer join as well
q4 = pd.read_sql(
    """
    SELECT
        *
    FROM
        LEAGUE
        INNER JOIN COUNTRY ON LEAGUE.country_id = COUNTRY.id;
    """,
    conn,
)
q4

# %% [markdown]
# ## Question 5: Select data from _Match_ table
# - When a team is serving as host of a contest, it is designated as the "home team". The opposing team is said to be the "away
# team"
# - In Match table, each row is a match with one home team and one away team including home team goal and away team goal respectively

# %%
# Normal Table Select
q5 = pd.read_sql("SELECT * FROM MATCH;", conn)
q5

# %% [markdown]
# ## Question 6: Select match data includes league and country information
#
# The Match table has relation with:
#  - Country table by country_id
#  - League table by League_id

# %%
# As the q6 implied, there are 3 tables joined together: Match, Country, League
# Use Match as base, Left outer join Country and League based on ID
q6 = pd.read_sql(
    """
    SELECT
        MATCH.id,
        MATCH.country_id,
        MATCH.league_id,
        Country.name,
        League.name
    FROM
        MATCH
        LEFT OUTER JOIN Country ON MATCH.country_id = Country.id
        LEFT OUTER JOIN League ON MATCH.league_id = League.id;
    """,
    conn,
)
q6

# %% [markdown]
# ## Question 7: Get number of match by each league including league name, order the number of match by descending

# %%
# Using order by for sorting
q7 = pd.read_sql(
    """
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
    """,
    conn,
)
q7

# %% [markdown]
# ## Question 8: Get total goal of home team and away team in each league
# - use Group By statement

# %%
# Using Sum with Group by to get total home goal
q8 = pd.read_sql(
    """
SELECT
    LEAGUE.name AS "League Name",
    SUM(MATCH.home_team_goal) AS "Total Home Team Goal",
    SUM(MATCH.away_team_goal) AS "Total Away Team Goal"
FROM
    MATCH
    LEFT OUTER JOIN LEAGUE ON MATCH.league_id = LEAGUE.id
GROUP BY
    league_id;
    """,
    conn,
)
q8

# %% [markdown]
# ## Question 9: Select data from Team table

# %%
q9 = pd.read_sql("Select * from Team", conn)
q9

# %% [markdown]
# ## Question 10: Get top 20 teams with highest home goal
# - Use GROUP BY, LIMIT statement

# %%
# Get top 20 teams by sorting with Total Home Team Goal Descending,
# Then limit 20
# Need an Left Outer Join with TEAM to get Team name
q10 = pd.read_sql(
    """
    SELECT
        MATCH.home_team_api_id AS "Team ID",
        TEAM.team_long_name AS "Team Name",
        SUM(MATCH.home_team_goal) AS "Total Home Team Goal"
    FROM
        MATCH
        LEFT OUTER JOIN TEAM ON MATCH.home_team_api_id = TEAM.team_api_id
    GROUP BY
        MATCH.home_team_api_id
    ORDER BY
        "Total Home Team Goal" DESC
    LIMIT
        20;
    """,
    conn,
)
q10

# %% [markdown]
# ## Question 11: Get top 20 teams with highest away goal
# - Use GROUP BY, LIMIT statement

# %%
# Get top 20 teams by sorting with Total Home Team Goal Descending,
# Then limit 20
# Need an Left Outer Join with TEAM to get Team name
q11 = pd.read_sql(
    """
    SELECT
        MATCH.away_team_api_id AS "Team ID",
        TEAM.team_long_name AS "Team Name",
        SUM(MATCH.away_team_goal) AS "Total Away Team Goal"
    FROM
        MATCH
        LEFT OUTER JOIN TEAM ON MATCH.away_team_api_id = TEAM.team_api_id
    GROUP BY
        MATCH.away_team_api_id
    ORDER BY
        "Total Away Team Goal" DESC
    LIMIT
        20;
    """,
    conn,
)
q11

# %% [markdown]
# ## Question 12: Get team long name with total of goal, order the total number by descending
#
# - Total of goal of a team is added up from both away and home games
# - Use UNION statement

# %%
# First, we create a table that conists of a Union between Home team and its goal,
# and Away team and its goal. Since a team can sometimes be Home and Away, we need
# Union
# Secondly, we create another table that select from the previous table, but with
# GROUP By in Team ID and Sum in Total goals
q12 = pd.read_sql(
    """
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
            ALL
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
    """,
    conn,
)
q12


# %% [markdown]
# ## Question 13: Get team long name with total of matches, order the total number by descending

# %%
# This questions is similar to Q12
# First, we create a table that conists of a Union between Home team and its matches,
# and Away team and its matches. Since a team can sometimes be Home and Away, we need
# Union
# Secondly, we create another table that select from the previous table, but with
# GROUP By in Team ID and Sum in Total matches
q13 = pd.read_sql(
    """
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
    """,
    conn,
)
q13

# %% [markdown]
# ## Question 14: Get numbers of win, lost and draw matches of each team
#
# - If a team has home goal > away goal , team is “win” in this match
# - If a team has home goal < away goal , team is “lost” in this match
# - If a team has home goal = away goal , team is “draw” in this match
# - Use Case When statement

# %%
# Create Match_Result View - which store result win - lost -draw in each match
# (With respectively Home as references)
conn.execute("DROP VIEW IF EXISTS Match_Result;")
conn.execute(
    """
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
    """
)
# Create individual team result with union between 2 tables Home and Away,
# with Away as a inverse of win and lost
conn.execute("DROP VIEW IF EXISTS Team_Result;")
conn.execute(
    """
    CREATE VIEW IF NOT EXISTS Team_Result AS
    SELECT
        home_team_api_id AS "Team ID",
        "H_Win" AS "Win",
        "H_Lost" AS "Lost",
        "H_Draw" AS "Draw"
    FROM
        Match_Result
    UNION
    ALL
    SELECT
        away_team_api_id AS "Team ID",
        "H_Win" AS "Lost",
        "H_Lost" AS "Win",
        "H_Draw" AS "Draw"
    FROM
        Match_Result;
    """
)

# Finally, select the result with left outer join teams and group by team ID
#
q14 = pd.read_sql(
    """
    SELECT
        "Team ID",
        Team.team_long_name AS "Full Name",
        Sum("Win") AS "Total Win",
        Sum("Lost") AS "Total Lost",
        Sum("Draw") AS "Total Draw"
    FROM
        Team_Result
        LEFT OUTER JOIN Team ON Team.team_api_id = Team_Result."Team ID"
    GROUP BY
        "Team ID"
    ORDER BY
        "Total Win" DESC;
    """,
    conn,
)
q14

# %% [markdown]
# ## Question 15: Get top 10 team with highest numbers of win matches

# %%
# This is just a simple query, consists of Team_Result left outer join with Team
q15 = pd.read_sql(
    """
    SELECT
        "Team ID",
        Team.team_long_name AS "Full Name",
        Sum("Win") AS "Total Win"
    FROM
        Team_Result
        LEFT OUTER JOIN Team ON Team.team_api_id = Team_Result."Team ID"
    GROUP BY
        "Team ID"
    ORDER BY
        "Total Win" DESC
    LIMIT 10;
    """,
    conn,
)
q15

# %% [markdown]
# ## Question 16: Get percentage of each league total matches versus all leagues

# %%
# First, we create a view that consists of Total Matches per leagues
conn.execute("""DROP VIEW IF EXISTS League_Total_Matches;""")

conn.execute(
    """
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
"""
)

# Secondly, we create a view (variable) for Sum of League Total Matches
conn.execute("DROP VIEW IF EXISTS League_Total_Matches_All;")
conn.execute(
    """
CREATE VIEW IF NOT EXISTS League_Total_Matches_All AS
SELECT
        Sum("Total Matches") "Total Matches All"
        FROM
            League_Total_Matches;
"""
)

# Finally, calculate Percentage by using League_Total_Matches * 100 / League_Total_Matches_All
q16 = pd.read_sql(
    """
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
""",
    conn,
)
q16

# %% [markdown]
# ## Question 17: Get percentage of score in each league

# %%
# First, we create a view that consists of Total Goals per leagues
conn.execute("DROP VIEW IF EXISTS League_Total_Goals;")

# Secondly, we create a view (variable) for Sum of League Total Goals
conn.execute(
    """
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
"""
)


# Finally, calculate Percentage by using League_Total_Goals * 100 / League_Total_Goals_All
q17 = pd.read_sql(
    """
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
    """,
    conn,
)
q17

# %% [markdown]
# ## Question 18: Get total numbers of goals for each league in each season

# %%
# Create Match_Goal view with combination of home and away team goal
conn.execute("DROP VIEW IF EXISTS Match_Goal;")
conn.execute(
    """
CREATE VIEW IF NOT EXISTS Match_Goal AS
SELECT
    match_api_id,
    season,
    home_team_goal + away_team_goal AS "Goals"
FROM
    MATCH;
"""
)

# Using sum with group by season
q18 = pd.read_sql(
    """
SELECT
    season,
    Sum("Goals") AS "Total Goals"
FROM
    Match_goal
GROUP BY
    season;
    """,
    conn,
)
q18

# %% [markdown]
# ## Question 19: Get player attributes
#
# - Convert weight to kilogram
# - Convert height to meter
# - Calculuate bmi = ( (weight* 0.453592) / (height/100)^2)
# - Get Age of player

# %%
# Convert player attributes like the above, with kg = 0.454*lb, bmi formula
# For Age, get year from now minus year from birthday with strftime
q19 = pd.read_sql(
    """
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
    """,
    conn,
)
q19

# %% [markdown]
# ## Question 20: Get oldest player

# %%
# Based on above query, but with limit = 1 and order by Age DESC
q20 = pd.read_sql(
    """
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
""",
    conn,
)
q20

# %% [markdown]
# ## Question 21: Get players who played highest number of matches

# %%
# Since the Player_Attributes is per matches for each player, we would use 
# count with groupby player_id to count number of matches for each player
# then use orderby player_id with Limit 1
q21 = pd.read_sql(
    """
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
""",
    conn,
)
q21

# %% [markdown]
# ## Question 22: Get players who had overall_rating larger than 80

# %%
# Similar with above, but with Overall rating Average calculate groupby 
# And select from the calculation table with Average Overall Rating >= 80
q22 = pd.read_sql(
    """
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
""",
    conn,
)
q22
