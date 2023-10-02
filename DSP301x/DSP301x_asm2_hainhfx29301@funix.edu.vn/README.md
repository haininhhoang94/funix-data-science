# User Manual for Assignment 2

This program reads a class file, analyzes the data, calculates grades based on a rubric, and saves the results to a file.

## Requirements:
1. Open all files in the data directory for reading and handle exceptions.
2. Read each line in the file, identify suitable data, and report any invalid lines.
3. Grade the data based on a rubric provided in ASM2.
4. Create a result file with a suitable name.

## Usage:
- Run the program with an optional "--debug" argument to enable debug mode.
## Input:
- class name (without *.txt)

## Output:
- Print the designed rubric with statistical metric
- Save the grades in *.txt file (with header)

## Functions:
1. read_file():
  - Prompts the user to enter the name of a file to grade.
  - Opens the file for reading and stores the content in the 'output' variable.
  - Removes empty lines from the content.

2. analyzing():
  - Analyzes the content of the file.
  - Reports the total number of lines, valid lines, and invalid lines.
  - Prints any invalid lines found.

3. grading():
  - Grades the data based on a provided answer key.
  - Calculates the final grades for each student.
  - Reports statistics such as the number of high scores, mean score, highest score,

4. print_and_output():
  - print the grades in *.txt file, with header

## Supplemental functions and libraries:
- re: Regular expression operations
- pandas: Data manipulation and analysis library
- numpy: Scientific computing library
- tabulate: Pretty-print tabular data
- os: Operating system interface
- sys: System-specific parameters and functions
