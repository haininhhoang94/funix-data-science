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
  (1, "Ahuja", "Rav", NULL, NULL);

-- Task 2B:
INSERT INTO
  INSTRUCTOR (ins_id, lastname, firstname, city, country)
VALUES
  (1, "Ahuja", "Rav", NULL, NULL),
  (2, "Chong", "Raul", NULL, NULL),
  (3, "Vasudevan", "Hima", NULL, NULL);
