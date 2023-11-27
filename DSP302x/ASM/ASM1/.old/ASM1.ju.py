# %% [markdown]
"""
# Project Overview

You receive a European Soccer Database that has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016. The goal is you walk through this database to do analysis include some steps for exploring our dataset, some steps for basics statistics and then you visualize the result. To complete all your steps, you need to query your data in the database using SQL statement. This project practices you write SQL command to pull data and extrac it.
"""

# %% [markdown]
"""
# Database Description

This European Soccer Database has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016, 11 European Countries with their lead championship. Players and Teams' attributes sourced from EA Sports' FIFA video game series, including the weekly updates.
"""

# %% [markdown]
"""
# Import Python package
"""

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
"""
## Question 1: Connect to database and get information of all tables

Read https://docs.python.org/2/library/sqlite3.html

You write only SQL statement to get the result, should not use Pandas to manipulate result.
"""

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

# %%
# helpers: Let's define each tables as variable in Pandas
player_attributes = pd.read_sql("Select * from Player_Attributes", conn)
player = pd.read_sql("Select * from Player", conn)
match = pd.read_sql("Select * from Match", conn)
league = pd.read_sql("Select * from League", conn)
country = pd.read_sql("Select * from Country", conn)
team = pd.read_sql("Select * from Team", conn)
team_attributes = pd.read_sql("Select * from Team_Attributes", conn)

# %% [markdown]
"""
## Question 2: Select data in "Country" table
"""

# %%
result = pd.read_sql("SELECT * FROM COUNTRY;", conn)
result

# %% [markdown]
"""
## Question 3: Select data in "League" table
"""

# %%
league = pd.read_sql("SELECT * FROM LEAGUE;", conn)
league

# %% [markdown]
"""
## Question 4: Select League data with country information
The League table has relation with Country table by country_id. Use the join sql statement to join two tables.
"""

# %%
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
"""
## Question 5: Select data from _Match_ table
- When a team is serving as host of a contest, it is designated as the "home team". The opposing team is said to be the "away 
team"
- In Match table, each row is a match with one home team and one away team including home team goal and away team goal respectively
"""

# %%
q5 = pd.read_sql("SELECT * FROM MATCH;", conn)
q5

# %% [markdown]
"""
Seems like home_api_id and away_api_id will be helpful later
"""

# %% [markdown]
"""
## Question 6: Select match data includes league and country information

The Match table has relation with:
 - Country table by country_id
 - League table by League_id
"""

# %%
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
"""
## Question 7: Get number of match by each league including league name, order the number of match by descending
"""

# %%
q7 = pd.read_sql(
    """
    SELECT
        league_id,
        LEAGUE.name,
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
"""
## Question 8: Get total goal of home team and away team in each league
- use Group By statement
"""

# %%
q8 = pd.read_sql(
    """
    SELECT
        MATCH.league_id,
        LEAGUE.name,
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
"""
## Question 9: Select data from Team table
"""

# %%
team = pd.read_sql("Select * from Team", conn)
team

# %% [markdown]
"""
## Question 10: Get top 20 teams with highest home goal
- Use GROUP BY, LIMIT statement
"""

# %%
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
"""
## Question 11: Get top 20 teams with highest away goal
- Use GROUP BY, LIMIT statement
"""

# %%
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
"""
## Question 12: Get team long name with total of goal, order the total number by descending

- Total of goal of a team is added up from both away and home games
- Use UNION statement
"""

# %%
# TODO: Explain later
# There is some note here:
# - First, there should be a Self-Join from the
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

# %%
# Check unique
# np.shape(q12['Match ID'].unique())
# q12["Match ID"].duplicated().sum()

# %% [markdown]
"""
## Question 13: Get team long name with total of matches, order the total number by descending
"""

# %%
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
"""
## Question 14: Get numbers of win, lost and draw matches of each team

- If a team has home goal > away goal , team is “win” in this match
- If a team has home goal < away goal , team is “lost” in this match
- If a team has home goal = away goal , team is “draw” in this match
- Use Case When statement
"""

# %%
# Create Match_Result View
conn.execute("DROP VIEW IF EXISTS Match_Result;")
conn.execute("""
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
    """)
# Create individual team result with union
conn.execute("DROP VIEW IF EXISTS Team_Result;")
conn.execute("""
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
    """)

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
"""
## Question 15: Get top 10 team with highest numbers of win matches
"""
# %%
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
"""
## Question 16: Get percentage of each league total matches versus all leagues
"""

# %%

# %% [markdown]
"""
## Question 17: Get percentage of score in each league
"""

# %%
# write your query

# %% [markdown]
"""
## Question 18: Get total numbers of goals for each league in each season
"""

# %%
# write your query

# %% [markdown]
"""
## Question 19: Get player attributes

- Convert weight to kilogram
- Convert height to meter
- Calculuate bmi = ( (weight* 0.453592) / (height/100)^2)
- Get Age of player
"""

# %%
# write your query

# %% [markdown]
"""
## Question 20: Get oldest player
"""

# %%
# write your query

# %% [markdown]
"""
## Question 21: Get players who played highest number of matches
"""

# %%
# write your query

# %% [markdown]
"""
## Question 22: Get players who had overall_rating larger than 80
"""

# %%
# write your query
