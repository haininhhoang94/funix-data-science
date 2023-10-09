# # Test Grade Calculator
# Requirement:
# 1. Open all file in data directory for reading and WITH EXCEPTION-HANDLER
# 2. Readline in each file, find suitable data and reports those
# 3. Grade based on rubic provide in ASM2
# 4. Create result file with suitable name


# 0. Supplimental function and import suitable library
import re
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
import sys

# For debug mode
if len(sys.argv) == 1:
    arg1 = ""
else:
    arg1 = sys.argv[1]


# NOTE: Use functions with global variable instead of return something is because our
# functions doesn't really serve as traditional input-output data, instead it is just
# a way to refactoring our code


# 1.2 + 1.3 + 1.4. Write a program allow user to enter name of a file and read
def read_file():
    while True:
        try:
            print("\n**** INITIALIZNG ****\n")
            global output
            global file_name
            file_name = input(
                "Enter a class file to grade (i.e. class1 for class1.txt) : "
            )
            with open("./data/" + file_name + ".txt", "r") as file:
                content = file.read()
            print("Successfully opened " + file_name + ".txt")
            content_split = content.split("\n")
            output = content_split
            # NOTE: fix reading an empty line
            for line_raw in output:
                if line_raw == "":
                    output.remove(line_raw)
            break  # Exit the loop if no exception occurs
        except FileNotFoundError:
            print("File cannot be found.")
        pass


# 2.1. Reports all line in file
# 2.2. Reports invalid line in file
def analyzing():
    print("\n**** ANALYZING ****\n")
    invalid_lines_by_grades_count = []
    invalid_lines_by_student_id = []
    global output_split
    output_split = []
    line = ""
    i = 0
    try:
        for line in output:
            i += 1
            # Debug mode:
            if arg1 == "--debug":
                print("Read line {}".format(i))
            line_split = line.split(",")

            # Check if a line contain 26 values
            if len(line_split) != 26:
                invalid_lines_by_grades_count.append(line_split)
                # Pop the value out due invalid
                output.remove(line)
                print(
                    "Invalid line of data: does not contain exactly 26 values ({})"
                    ":\n{}\n".format(len(line_split), line_split)
                )
            elif re.match(r"^N\d{8}$", line_split[0]) is None:
                # Check if a student ID contain N and 8 numbers
                invalid_lines_by_student_id.append(line_split)
                # Pop the value out due invalid
                output.remove(line)
                print("Invalid line of data: N# is invalid:\n{}\n".format(line_split))
            else:
                output_split.append(line_split)

    except Exception as e:
        # Exception handling code
        print("An error while execute code occurred:\n", str(e))

    # If no line error, print
    if len(invalid_lines_by_student_id) == 0 & len(invalid_lines_by_grades_count) == 0:
        print("No errors found\n")

    print("\n**** REPORT ****\n")
    print("Total number of lines in file: {}\n".format(len(output)))
    print(
        "Total number of valid lines in file: {}\n".format(
            len(output)
            - len(invalid_lines_by_student_id)
            - len(invalid_lines_by_grades_count)
        )
    )
    if (len(invalid_lines_by_student_id) + len(invalid_lines_by_grades_count)) != 0:
        print(
            "Total number of invalid lines in file: {}\n".format(
                len(invalid_lines_by_grades_count) + len(invalid_lines_by_student_id)
            )
        )
    if len(invalid_lines_by_grades_count) == 0:
        print(
            "Total number of invalid lines by grades count: {}\n".format(
                len(invalid_lines_by_grades_count)
            )
        )

    if len(invalid_lines_by_student_id) == 0:
        print(
            "Total number of invalid lines by student id: {}\n".format(
                len(invalid_lines_by_student_id)
            )
        )
    pass


# 3. Grading based on the following criteria
# +4 for each CORRECT answer
# 0 for each BLANK answer
# -1 for each INCORRECT answer
# Answer key:
def grading():
    answer_key = [
        "B",
        "A",
        "D",
        "D",
        "C",
        "B",
        "D",
        "A",
        "C",
        "C",
        "D",
        "B",
        "A",
        "B",
        "A",
        "C",
        "B",
        "D",
        "A",
        "C",
        "A",
        "A",
        "B",
        "D",
        "D",
    ]

    # First, after filtering like above, we have our output with no invalid line
    # Let's create a new list as grade storage
    # Remember that grades key has 25, line have 26 (contain student id as well)
    global grades_grid
    grades_grid = []
    # grades_series is a sub-element of grades
    global grades_series
    grades_series = []
    # Create a series of grades, contain only the final grades
    global final_grades
    final_grades = []
    i = 0

    for line in output_split:
        for i in range(0, len(answer_key)):
            if line[i + 1] == answer_key[i]:
                grades_series.append(4)
            elif line[i + 1] == "":
                grades_series.append(0)
            else:
                grades_series.append(-1)
        grades_grid.append(grades_series)
        # Calculate the final grades
        final_grades.append(sum(grades_series))
        # Return the cache to empty
        grades_series = []

    # 3.1. Count the numbers of high score's student (>80)
    final_grades = np.array(final_grades)
    print(
        "Total student of high scores: {}\n".format(np.count_nonzero(final_grades > 80))
    )

    # 3.2. Mean of the scores
    print("Mean (average) score: {}\n".format(final_grades.mean()))
    # 3.3. Highest score:
    print("Highest score: {}\n".format(final_grades.max()))
    # 3.4. Lowest score:
    print("Lowest score: {}\n".format(final_grades.min()))
    # 3.5. Range of score:
    print("Range of score: {}\n".format(final_grades.max() - final_grades.min()))
    # 3.6. Median score:
    print("Median score: {}\n".format(np.median(final_grades)))
    # 3.7 + 3.8. Question that most people skip or incorrectly:
    # In order to do this, first we need to see the variable final grades
    # Final grades does not contain the specific answer-question, thus
    # We need to used grade grid. We need to count the ocurrance of 0
    # in each questions
    # Create a series contains number of questions first
    # columns is the score of each student with columns name is student id
    global col_id
    col_id = []
    for i in range(0, len(output_split)):
        col_id.append(output_split[i][0])

    q_a = pd.DataFrame(
        data=np.array(grades_grid).transpose(),
        columns=col_id,
    )
    # Set index to begin with 1 instead of 0
    q_a.index = q_a.index + 1

    # 3.7. Question that most people skip
    count_skip = q_a.eq(0).sum(axis=1)
    most_skip = count_skip.nlargest(1, keep="all")
    most_skip = pd.DataFrame(
        data=most_skip, columns=["Number of people skip"]
    ).rename_axis(index="Question number")
    most_skip["%"] = round(most_skip / len(output), 4) * 100
    print("Question that most people skip:")
    print(tabulate(most_skip, headers="keys", tablefmt="psql"))
    print("\n")

    # 3.8. Question that most people answer incorrectly
    count_incorr = q_a.eq(-1).sum(axis=1)
    most_incorr = count_incorr.nlargest(1, keep="all")
    most_incorr = pd.DataFrame(
        data=most_incorr, columns=["Number of people ans wrong"]
    ).rename_axis(index="Question number")
    most_incorr["%"] = round(most_incorr / len(output), 4) * 100
    print("Question that most people incorr:")
    print(tabulate(most_incorr, headers="keys", tablefmt="psql"))
    print("\n")
    pass


# 4. Store grades
def print_and_output():
    print("\n**** SAVING ****\n")
    # Create the result folder in case it is not exist
    folder_path = "./results/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Store data to file
    # Create Pandas Dataframe to store the result
    final_grades_pd = pd.DataFrame(
        {"Grade": final_grades, "Student ID": col_id}
    ).set_index("Student ID")
    # Save to file
    final_grades_pd.to_csv(
        "./results/" + file_name + "_grades.txt", index=True, sep=","
    )
    print("Successfully saved to {}_grades.txt\n".format(file_name))

    pass


# Main function
# checks if the special variable `__name__` is equal to `"__main__"`. This condition is
# true when the script is run directly, and false when the script is imported as a
# module.
if __name__ == "__main__":
    read_file()
    analyzing()
    grading()
    print_and_output()
