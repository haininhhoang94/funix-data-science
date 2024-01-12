-- Task 0:
DROP TABLE IF EXISTS INSTRUCTOR;

-- Task 1:
CREATE TABLE
  IF NOT EXISTS INSTRUCTOR (
    ins_id INT PRIMARY KEY,
    lastname VARCHAR(600),
    firstname VARCHAR(600),
    city VARCHAR(600),
    country CHAR(2)
  );

-- Task 2A:
INSERT INTO
  INSTRUCTOR (ins_id, lastname, firstname, city, country)
VALUES
  (1, "Ahuja", "Rav", "Toronto", "CA");

-- Task 2B:
INSERT INTO
  INSTRUCTOR (ins_id, lastname, firstname, city, country)
VALUES
  (2, "Chong", "Raul", "Toronto", "CA"),
  (3, "Vasudevan", "Hima", "Chicago", "US");

-- -- Task 3
-- -- View all of our table
-- SELECT
--   *
-- FROM
--   INSTRUCTOR;
--
-- -- Task 3B:
-- SELECT
--   firstname,
--   lastname
-- FROM
--   INSTRUCTOR
-- WHERE
--   city = 'Toronto';
--
-- Task 4:
UPDATE INSTRUCTOR
SET
  city = 'Markham'
WHERE
  firstname = "Rav"
  AND lastname = "Ahuja";

-- Task 5:
DELETE FROM INSTRUCTOR
WHERE
  ins_id = 2;

-- Task 5B:
-- View all of our table
SELECT
  *
FROM
  INSTRUCTOR;
